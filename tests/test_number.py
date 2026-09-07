"""Test the go-eController (MQTT) number platform."""

import pytest
from pytest_homeassistant_custom_component.common import (
    MockConfigEntry,
    async_fire_mqtt_message,
)

from custom_components.goecontroller_mqtt.const import DOMAIN

ENTITY_ID = "number.go_econtroller_012345_awp"
TOPIC = "/go-eController/012345/awp"


@pytest.fixture(autouse=True)
def expected_lingering_timers():
    """The MQTT integration keeps a periodic timer of its own alive."""
    return True


async def _setup(hass):
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={"serial_number": "012345", "topic_prefix": "/go-eController"},
        title="go-eController 012345",
        unique_id="012345",
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    assert hass.states.get(ENTITY_ID) is not None


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ("1.5", 1.5),
        ("-12", -12.0),
        ("null", None),
        ("err", None),
    ],
)
async def test_payload_is_coerced_to_a_number(hass, mqtt_mock, payload, expected) -> None:
    """Only numeric payloads may reach the state machine as a value."""
    await _setup(hass)

    async_fire_mqtt_message(hass, TOPIC, payload)
    await hass.async_block_till_done()

    entity = hass.data["number"].get_entity(ENTITY_ID)
    assert entity.native_value == expected
