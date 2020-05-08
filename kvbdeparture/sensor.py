"""Platform for sensor integration."""
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import requests
from bs4 import BeautifulSoup


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([KVBDepartureSensor(hass, config["stationid"])])


class KVBDepartureSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, hass, stationid):
        """Initialize the sensor."""
        self._state = None
        self._headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36"
        }
        self._stationid = stationid
        self._hass = hass
        self._attributes = {}

    @property
    def name(self):
        """Return the name of the sensor."""
        return "kvbdep_{}".format(self._stationid)

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    """
        @property
        def unit_of_measurement(self):

            return TEMP_CELSIUS
    """

    @property
    def device_state_attributes(self):
        """Return the state attributes of the sensor."""
        return self._attributes

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = False
        url = "https://www.kvb.koeln/qr/{}/".format(self._stationid)
        req = requests.get(url, headers=self._headers)
        soup = BeautifulSoup(req.text, features="html.parser")
        tables = soup.find_all("table", class_="display")
        departures = []
        for row in tables[0].find_all("tr"):
            tds = row.find_all("td")
            (line_id, direction, time) = (tds[0].text, tds[1].text, tds[2].text)
            line_id = line_id.replace("\xa0", "")
            direction = direction.replace("\xa0", "")
            time = time.replace("\xa0", " ").strip().lower()
            if time == "sofort":
                time = "0"
            time = time.replace(" min", "")
            try:
                line_id = int(line_id)
            except ValueError:
                pass
            departures.append(
                {"line_id": line_id, "direction": direction, "wait_time": time}
            )

        self._attributes["departures"] = departures
        self._state = True
