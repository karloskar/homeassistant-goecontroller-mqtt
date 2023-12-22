"""Definitions for go-eController buttons exposed via MQTT."""
from __future__ import annotations

import logging
from dataclasses import dataclass

from homeassistant.components.button import ButtonEntityDescription
from homeassistant.helpers.entity import EntityCategory

from . import GoEControllerEntityDescription

_LOGGER = logging.getLogger(__name__)


@dataclass
class GoEControllerButtonEntityDescription(GoEControllerEntityDescription, ButtonEntityDescription):
    """Button entity description for go-eController."""

    domain: str = "button"
    payload_press: str = "true"


BUTTONS: tuple[GoEControllerButtonEntityDescription, ...] = (
    GoEControllerButtonEntityDescription(
        key="rst",
        name="Restart device",
        payload_press="true",
        entity_category=EntityCategory.CONFIG,
        device_class=None,
        icon="mdi:restart",
        entity_registry_enabled_default=True,
        disabled=False,
    ),
)
