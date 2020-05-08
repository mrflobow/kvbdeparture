"""The KVB Departure Sensor integration."""

import voluptuous as vol


PLATFORM_SCHEMA = vol.Schema({"stationid": int, "stationname": str})
PLATFORMS = ["sensor"]
