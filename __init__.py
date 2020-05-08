"""The KVB Departure Sensor integration."""

import voluptuous as vol
import asyncio


PLATFORM_SCHEMA = vol.Schema({"stationid": int})
PLATFORMS = ["sensor"]
