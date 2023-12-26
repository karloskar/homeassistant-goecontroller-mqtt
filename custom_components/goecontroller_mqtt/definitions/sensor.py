"""Definitions for go-eController sensors exposed via MQTT."""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    SIGNAL_STRENGTH_DECIBELS,
    UnitOfElectricCurrent,
    UnitOfPower,
)
from homeassistant.helpers.entity import EntityCategory

from . import GoEControllerEntityDescription

_LOGGER = logging.getLogger(__name__)


@dataclass
class GoEControllerSensorEntityDescription(GoEControllerEntityDescription, SensorEntityDescription):
    """Sensor entity description for go-eController."""

    domain: str = "sensor"


def remove_quotes(value, unused) -> str:
    """Remove quotes helper."""
    return value.replace('"', "")


def extract_isv(value: str, key: tuple) -> float:
    """Extract isv values from list."""
    list_int, dict_key = key
    if dict_key in ["i", "p"]:
        return round(float(json.loads(value)[int(list_int)][dict_key]), 1)
    if dict_key == "f":
        return round(float(json.loads(value)[int(list_int)][dict_key]) * 100)


def extract_ccp(value: str, key: str) -> float:
    """Extract ccp values from list."""
    try:
        return round(float(json.loads(value)[int(key)]))
    except TypeError:
        return 0


SENSORS: tuple[GoEControllerSensorEntityDescription, ...] = (
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("0", "i"),
        name="Amp 1",
        state=extract_isv,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("1", "i"),
        name="Amp 2",
        state=extract_isv,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("2", "i"),
        name="Amp 3",
        state=extract_isv,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("3", "i"),
        name="Amp 4",
        state=extract_isv,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("4", "i"),
        name="Amp 5",
        state=extract_isv,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("5", "i"),
        name="Amp 6",
        state=extract_isv,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("0", "p"),
        name="Power 1",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("1", "p"),
        name="Power 2",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("2", "p"),
        name="Power 3",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("3", "p"),
        name="Power 4",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("4", "p"),
        name="Power 5",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("5", "p"),
        name="Power 6",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("0", "f"),
        name="Power Factor 1",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("1", "f"),
        name="Power Factor 2",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("2", "f"),
        name="Power Factor 3",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("3", "f"),
        name="Power Factor 4",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("4", "f"),
        name="Power Factor 5",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="isv",
        attribute=("5", "f"),
        name="Power Factor 6",
        state=extract_isv,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="ccp",
        attribute="0",
        name="Power usage home",
        state=extract_ccp,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="ccp",
        name="Power usage grid",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
        attribute="1",
        state=extract_ccp,
    ),
    GoEControllerSensorEntityDescription(
        key="ccp",
        name="Power usage car",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
        attribute="2",
        state=extract_ccp,
    ),
    GoEControllerSensorEntityDescription(
        key="ccp",
        name="Power usage relay",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
        attribute="3",
        state=extract_ccp,
    ),
    GoEControllerSensorEntityDescription(
        key="ccp",
        name="Power usage solar",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
        attribute="4",
        state=extract_ccp,
    ),
    GoEControllerSensorEntityDescription(
        key="ccp",
        name="Power usage battery",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=True,
        disabled=False,
        attribute="5",
        state=extract_ccp,
    ),
    GoEControllerSensorEntityDescription(
        key="fwv",
        name="Firmware version",
        entity_category=EntityCategory.DIAGNOSTIC,
        state=remove_quotes,
        device_class=None,
        native_unit_of_measurement=None,
        state_class=None,
        icon="mdi:numeric",
        entity_registry_enabled_default=False,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="rbc",
        name="Reboot counter",
        entity_category=EntityCategory.DIAGNOSTIC,
        device_class=None,
        native_unit_of_measurement=None,
        state_class=SensorStateClass.TOTAL_INCREASING,
        icon="mdi:counter",
        entity_registry_enabled_default=True,
        disabled=False,
    ),
    GoEControllerSensorEntityDescription(
        key="rbt",
        name="Uptime",
        entity_category=EntityCategory.DIAGNOSTIC,
        device_class=None,
        native_unit_of_measurement=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
        disabled=True,
        disabled_reason="TODO: Convert to a timestamp first",
    ),
    GoEControllerSensorEntityDescription(
        key="rssi",
        name="WiFi signal strength",
        entity_category=EntityCategory.DIAGNOSTIC,
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
        disabled=False,
    ),
)
