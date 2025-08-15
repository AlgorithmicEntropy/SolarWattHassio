"""Class to retrive data from the api."""

from local_solar_watt import EnergyManagerApi, EnergyManagerVersion
from local_solar_watt.clients import MockClient
from local_solar_watt.handlers import EmClassic


class ClientWrapper:
    """Stores retrieved data."""

    def __init__(self, host) -> None:
        """Initialize the data object."""
        self.host = host
        api = EnergyManagerApi(EnergyManagerVersion.CLASSIC, host)
        self._api = api
        self._data = None
        self._connection_status = False

    @property
    def data(self):
        """Get latest update if throttle allows. Return status."""
        return self._data

    @property
    def connected(self):
        """Last known state of the connection."""
        return self._connection_status

    def test_connection(self):
        """Test connection to the energy manager api."""
        # TODO: remove me
        self._connection_status = True
        return
        val = self._api.test_connection()
        # TODO remove me, workaround for inconsistent api
        if isinstance(val, bool):
            self._connection_status = val
        else:
            self._connection_status = val[0]

    async def update(self, **kwargs):
        """Fetch the latest status."""

        async def fetch_and_parse():
            """Fetch data and parse it asynchronously."""
            client = MockClient(
                "/workspaces/core/homeassistant/components/local_solar_watt/tmp/energy_manager_classic.json"
            )
            handler = EmClassic()
            return handler.parse(client.fetch_data_json())

        parsed = await fetch_and_parse()
        self._connection_status = parsed is not None
        self._data = parsed
        self._connection_status = parsed is not None
        self._data = parsed
