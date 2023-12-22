"""Definitions for go-eController numbers exposed via MQTT."""
from __future__ import annotations

import logging
from dataclasses import dataclass

from homeassistant.components.number import NumberEntityDescription
from homeassistant.const import (
    CURRENCY_CENT,
)
from homeassistant.helpers.entity import EntityCategory

from . import GoEControllerEntityDescription

_LOGGER = logging.getLogger(__name__)


@dataclass
class GoEControllerNumberEntityDescription(GoEControllerEntityDescription, NumberEntityDescription):
    """Number entity description for go-eController."""

    domain: str = "number"


NUMBERS: tuple[GoEControllerNumberEntityDescription, ...] = (
    GoEControllerNumberEntityDescription(
        key="awp",
        name="Awattar maximum price threshold",
        entity_category=EntityCategory.CONFIG,
        device_class=None,
        native_unit_of_measurement=CURRENCY_CENT,
        entity_registry_enabled_default=True,
        disabled=False,
        native_max_value=100,
        native_min_value=-100,
        native_step=0.1,
    ),
)
