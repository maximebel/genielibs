import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.mld_snooping.configure import unconfigure_ipv6_mld_snooping_vlan_querier_version


class TestUnconfigureIpv6MldSnoopingVlanQuerierVersion(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          Cat9300_VTEP1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Cat9300_VTEP1']
        self.device.connect()

    def test_unconfigure_ipv6_mld_snooping_vlan_querier_version(self):
        result = unconfigure_ipv6_mld_snooping_vlan_querier_version(self.device, 100, 2)
        expected_output = None
        self.assertEqual(result, expected_output)
