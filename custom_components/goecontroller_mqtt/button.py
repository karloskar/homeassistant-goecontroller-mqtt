"""The go-eController (MQTT) button."""
import logging

from homeassistant import config_entries, core
from homeassistant.components import mqtt
from homeassistant.components.button import ButtonEntity

from .definitions.button import BUTTONS, GoEControllerButtonEntityDescription
from .entity import GoEControllerEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: core.HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities,
):
    """Config entry setup."""
    async_add_entities(
        GoEControllerButton(config_entry, description)
        for description in BUTTONS
        if not description.disabled
    )


class GoEControllerButton(GoEControllerEntity, ButtonEntity):
    """Representation of a go-eController button that can be toggled using MQTT."""

    entity_description: GoEControllerButtonEntityDescription

    def __init__(
        self,
        config_entry: config_entries.ConfigEntry,
        description: GoEControllerButtonEntityDescription,
    ) -> None:
        """Initialize the button."""
        self.entity_description = description

        super().__init__(config_entry, description)

    async def async_press(self, **kwargs):
        """Turn the device on.

        This method is a coroutine.
        """
        await mqtt.async_publish(
            self.hass, f"{self._topic}/set", self.entity_description.payload_press
        )
