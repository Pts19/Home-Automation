# Definitions
* [Home Assistant](https://www.home-assistant.io/hassio/) - Home automation OS 
* [Integration](https://www.home-assistant.io/components/#search/light) - App that can interface with appliances like lights, coffee maker, change channel on TV, unlock door, etc
* [PHA](https://github.com/CS3398-Bolians-Booleans/CS3398-Bolians-S2019) - Predictive Home Automation - Integration manager developed by Boolean Inc

# Integration Architectue

* Web UI (Hass.io)
* Backend (Flask) (scikit-learn, pandas) (Home Assistant integration)
* Hardware (Raspberry Pi)

# Table of contents
* [Data In](#API-to-provide-data-to-PHA)
* [Integrations](#Integrations)

# API to provide data to PHA

## [Openweather](https://openweathermap.org/appid)

Sample response: https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1


## [Google Maps](https://developers.google.com/maps/documentation/directions/start)


Sample response:
https://developers.google.com/maps/documentation/directions/intro#sample-response


## [Iphone location](https://apps.apple.com/us/app/home-assistant-open-source-home-automation/id1099568401)

Home Assistant app can share geolocation on IOS


## [Android Geofence](https://developer.android.com/training/location/geofencing#java) 

Sample response: https://blog.bitsrc.io/how-to-perform-mobile-geolocation-testing-and-why-you-need-it-b391181e1d45



# Integrations
https://www.home-assistant.io/components/#search/light

