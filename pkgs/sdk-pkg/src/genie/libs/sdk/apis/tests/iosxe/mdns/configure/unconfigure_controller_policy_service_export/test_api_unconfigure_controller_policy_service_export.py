import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.mdns.configure import unconfigure_controller_policy_service_export


class TestUnconfigureControllerPolicyServiceExport(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          C9500H_Sathya:
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
        self.device = self.testbed.devices['C9500H_Sathya']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_controller_policy_service_export(self):
        result = unconfigure_controller_policy_service_export(self.device, 'DNAC', ['cntrl_policy'])
        expected_output = None
        self.assertEqual(result, expected_output)
