import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.interface.configure import unconfigure_eapol_eth_type_interface


class TestUnconfigureEapolEthTypeInterface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          LG-PK:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['LG-PK']
        self.device.connect()

    def test_unconfigure_eapol_eth_type_interface(self):
        result = unconfigure_eapol_eth_type_interface(self.device, 'GigabitEthernet1/0/10', '876F')
        expected_output = None
        self.assertEqual(result, expected_output)
