import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.nat.configure import unconfigure_nat64_v4_list_pool


class TestUnconfigureNat64V4ListPool(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Starfleet:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Starfleet']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_nat64_v4_list_pool(self):
        result = unconfigure_nat64_v4_list_pool(self.device, 'acl_3', 'n64_pool')
        expected_output = None
        self.assertEqual(result, expected_output)
