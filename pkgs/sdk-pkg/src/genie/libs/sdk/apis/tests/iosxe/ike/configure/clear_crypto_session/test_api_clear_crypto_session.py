import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.ike.configure import clear_crypto_session


class TestClearCryptoSession(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          rad-vtep1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: c9300
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['rad-vtep1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_clear_crypto_session(self):
        result = clear_crypto_session(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
