"""Config flow for LIFX."""
from homeassistant import config_entries
from .const import box2

class ExampleConfigFlow(config_entries.ConfigFlow, domain=box2):

import aiolifx

from .const import box2


async def _async_has_devices(hass):
    """Return if there are devices that can be discovered."""
    lifx_ip_addresses = await aiolifx.LifxScan(hass.loop).scan()
    return len(lifx_ip_addresses) > 0


config_entry_flow.register_discovery_flow(
    # Domain of your integration
    box2,
    # Title of the created config entry
    'box2',
    # async method that returns a boolean if devices/services are found
    _async_has_devices,
    # Connection class of the integration
    config_entries.CONN_CLASS_LOCAL_POLL
)