import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.aaa.configure import configure_common_criteria_policy


class TestConfigureCommonCriteriaPolicy(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          HCR_pk:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9200
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['HCR_pk']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_common_criteria_policy(self):
        result = configure_common_criteria_policy(device=self.device, policy_name='enable_test')
        expected_output = None
        self.assertEqual(result, expected_output)
