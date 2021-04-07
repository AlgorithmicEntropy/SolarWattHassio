# SolarWattHassio
Home Assistant (hass.io) custom component for SolarWatt solar system



#### Description
The integration will provide multiple sensors, which provide stats about your solar installation.

#### Installation

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

The easiest way to install it is through [HACS (Home Assistant Community Store)](https://hacs.xyz/), add this repository as a custom one in the HACS settings and download the integration.

If you want to install it manually,  
Download the custom_components/solar_watt_energy_manager folder and place into your $homeassistant_config_dir/custom_components directory.

Once downloaded restart your Home Assistant installation.
After the restart you should be able to add it from the integrations screen.

#### Configuration

The integration provides a config flow, in which you need to enter the IP address (host) of your energy manager device.  
No further changes are required.

But you can optionally change its name and the update (pull) delay.  
I advise to not change the update time below one minute, otherwise it could overload the device  
(Further testing required)
