# KVB Depature Sensor
KVB Departure Sensor for using with Home Assistant

# Installation
Copy content to ../config/custom_components/

Add sensor to your configuration.yaml

```yaml
sensors:
- platform: kvbdeparture
  stationname: Main Station
  stationid: 308

```