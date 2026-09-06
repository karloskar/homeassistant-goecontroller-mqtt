"""Test setting up the go-eController (MQTT) integration."""

import pytest
from homeassistant.exceptions import ServiceValidationError
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.goecontroller_mqtt.const import DOMAIN


@pytest.fixture(autouse=True)
def expected_lingering_timers():
    """The MQTT integration keeps a periodic timer of its own alive."""
    return True


def _add_entry(hass, topic_prefix="/go-eController"):
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={"serial_number": "012345", "topic_prefix": topic_prefix},
        title="go-eController 012345",
        unique_id="012345",
    )
    entry.add_to_hass(hass)
    return entry


async def test_setup_loads_every_platform(hass, mqtt_mock) -> None:
    """Every platform listed in PLATFORMS must produce entities."""
    entry = _add_entry(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    domains = {state.entity_id.split(".")[0] for state in hass.states.async_all()}
    assert {"button", "number", "sensor"} <= domains


async def test_unload_and_setup_again(hass, mqtt_mock) -> None:
    """Unloading must not leave entities behind or break a second setup."""
    entry = _add_entry(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    before = len(hass.states.async_all())

    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
    assert all(state.state == "unavailable" for state in hass.states.async_all())

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    assert len(hass.states.async_all()) == before


async def test_service_uses_configured_topic_prefix(hass, mqtt_mock) -> None:
    """The service must publish under the prefix stored on the config entry."""
    entry = _add_entry(hass, topic_prefix="/custom-prefix")
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    mqtt_mock.async_publish.reset_mock()

    await hass.services.async_call(
        DOMAIN,
        "set_config_key",
        {"serial_number": "012345", "key": "fna", "value": "hello"},
        blocking=True,
    )

    topics = [call.args[0] for call in mqtt_mock.async_publish.call_args_list]
    assert topics == ["/custom-prefix/012345/fna/set"]


async def test_service_rejects_unknown_serial_number(hass, mqtt_mock) -> None:
    """A serial number without a config entry must raise instead of publishing."""
    entry = _add_entry(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    with pytest.raises(ServiceValidationError):
        await hass.services.async_call(
            DOMAIN,
            "set_config_key",
            {"serial_number": "999999", "key": "fna", "value": "hello"},
            blocking=True,
        )
