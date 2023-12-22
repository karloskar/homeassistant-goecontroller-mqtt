"""Definitions for go-eController sensors exposed via MQTT."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging

from homeassistant.helpers.entity import EntityDescription

_LOGGER = logging.getLogger(__name__)


class GoEControllerStatusCodes:
    """Status code container."""

    psm = {
        1: "1 Phase",
        2: "3 Phases",
    }


@dataclass
class GoEControllerEntityDescription(EntityDescription):
    """Generic entity description for go-eController."""

    state: Callable | None = None
    attribute: str = "0"
    domain: str = "generic"
    disabled: bool | None = None
    disabled_reason: str | None = None
