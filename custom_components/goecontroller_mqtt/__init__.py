"""The go-eController (MQTT) integration."""
from __future__ import annotations

import logging

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components import mqtt
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady, ServiceValidationError
from homeassistant.helpers.typing import ConfigType

from .const import (
    ATTR_KEY,
    ATTR_SERIAL_NUMBER,
    ATTR_VALUE,
    CONF_SERIAL_NUMBER,
    CONF_TOPIC_PREFIX,
    DEFAULT_TOPIC_PREFIX,
    DOMAIN,
)

PLATFORMS: list[Platform] = [
    Platform.BUTTON,
    Platform.NUMBER,
    Platform.SENSOR,
    Platform.SWITCH,
]

_LOGGER = logging.getLogger(__name__)

SERVICE_SCHEMA_SET_CONFIG_KEY = vol.Schema(
    {
        vol.Required(ATTR_SERIAL_NUMBER): cv.string,
        vol.Required(ATTR_KEY): cv.string,
        vol.Required(ATTR_VALUE): cv.string,
    }
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up go-eController (MQTT) from a config entry."""
    if not await mqtt.async_wait_for_mqtt_client(hass):
        raise ConfigEntryNotReady("MQTT integration is not available")

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


def _topic_prefix_for_serial(hass: HomeAssistant, serial_number: str) -> str:
    """Return the topic prefix configured for a serial number."""
    for entry in hass.config_entries.async_entries(DOMAIN):
        if entry.data.get(CONF_SERIAL_NUMBER) == serial_number:
            return entry.data.get(CONF_TOPIC_PREFIX, DEFAULT_TOPIC_PREFIX)

    raise ServiceValidationError(f"No go-eController configured with serial number {serial_number}")


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up integration."""

    async def set_config_key_service(call: ServiceCall) -> None:
        serial_number = call.data[ATTR_SERIAL_NUMBER]
        key = call.data[ATTR_KEY]
        value = call.data[ATTR_VALUE]

        topic_prefix = _topic_prefix_for_serial(hass, serial_number)
        topic = f"{topic_prefix}/{serial_number}/{key}/set"

        if not value.isnumeric():
            if value in ["true", "True"]:
                value = "true"
            elif value in ["false", "False"]:
                value = "false"
            else:
                value = f'"{value}"'

        await mqtt.async_publish(hass, topic, value)

    hass.services.async_register(
        DOMAIN,
        "set_config_key",
        set_config_key_service,
        schema=SERVICE_SCHEMA_SET_CONFIG_KEY,
    )

    return True
