"""Definitions for go-eController switches exposed via MQTT."""
from __future__ import annotations

import logging
from dataclasses import dataclass

from homeassistant.components.switch import SwitchEntityDescription
from homeassistant.helpers.entity import EntityCategory

from . import GoEControllerEntityDescription

_LOGGER = logging.getLogger(__name__)


@dataclass
class GoEControllerSwitchEntityDescription(GoEControllerEntityDescription, SwitchEntityDescription):
    """Switch entity description for go-eController."""

    domain: str = "switch"
    payload_on: str = "true"
    payload_off: str = "false"
    optimistic: bool = False


SWITCHES: tuple[GoEControllerSwitchEntityDescription, ...] = (
    GoEControllerSwitchEntityDescription(
        key="tse",
        name="Time server enabled",
        entity_category=EntityCategory.CONFIG,
        device_class=None,
        entity_registry_enabled_default=False,
        disabled=True,
        disabled_reason="Not exposed via MQTT in firmware 053.1",
    ),
    GoEControllerSwitchEntityDescription(
        key="hsa",
        name="HTTP STA authentication",
        entity_category=EntityCategory.CONFIG,
        device_class=None,
        entity_registry_enabled_default=False,
        disabled=True,
        disabled_reason="Not exposed via MQTT in firmware 053.1",
    ),
    GoEControllerSwitchEntityDescription(
        key="cwe",
        name="Cloud websocket enabled",
        entity_category=EntityCategory.CONFIG,
        device_class=None,
        entity_registry_enabled_default=False,
        disabled=True,
        disabled_reason="Not exposed via MQTT in firmware 053.1",
    ),
)
