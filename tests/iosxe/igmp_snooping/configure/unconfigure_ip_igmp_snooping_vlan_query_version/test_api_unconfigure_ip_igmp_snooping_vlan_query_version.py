import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.igmp_snooping.configure import unconfigure_ip_igmp_snooping_vlan_query_version


class TestUnconfigureIpIgmpSnoopingVlanQueryVersion(unittest.TestCase):

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

    def test_unconfigure_ip_igmp_snooping_vlan_query_version(self):
        result = unconfigure_ip_igmp_snooping_vlan_query_version(self.device, 100, 2)
        expected_output = None
        self.assertEqual(result, expected_output)
