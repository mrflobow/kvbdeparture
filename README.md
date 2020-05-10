# KVB Departure
HomeAssistant custom sensor for Cologne, Germany public transportation (KVB)

# Installation
Copy content to ../config/custom_components/

Add sensor to your configuration.yaml

```yaml
sensors:
- platform: kvbdeparture
  stationname: Main Station
  stationid: 308

```