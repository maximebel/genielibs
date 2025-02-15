import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.inventory.get import get_component_details


class TestGetComponentDetails(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          9600_Switch:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: iosxe
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['9600_Switch']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_get_component_details(self):
        result = get_component_details(self.device)
        expected_output = {'descr_raw': ['Cisco Catalyst 9600 Series 6 Slot Chassis',
               'Cisco Catalyst 9600 Series 6 Slot Chassis Backplane',
               'Cisco Catalyst 9600 Series Carrier Card Module Container',
               'Cisco Catalyst 9600 Series Carrier Card Module Container',
               'Cisco Catalyst 9600 Series Carrier Card Module Container',
               'Cisco Catalyst 9600 Series Carrier Card Module Container',
               'Cisco Catalyst 9600 Series Carrier Card Module Container',
               'Cisco Catalyst 9600 Series Carrier Card Module Container',
               'Cisco Catalyst 9600 Series Routing Processor Module Container',
               'Supervisor 1 Module',
               'USB Port',
               'Hard Disk Container',
               'USB Port',
               'Network Management Ethernet',
               'Network Management TenGigEthernet',
               'Intel CPU x86-64',
               'Cisco Catalyst 9600 Series Routing Processor Module Container',
               'Cisco Catalyst 9600 Series Slot',
               'Cisco Catalyst 9600 Series Slot',
               'Cisco Catalyst 9600 Series Power Supply Bay Module Container',
               'Cisco Catalyst 9600 Series 2000W AC Power Supply',
               'Cisco Catalyst 9600 Series Power Supply',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Power Supply Bay Module Container',
               'Cisco Catalyst 9600 Series 2000W AC Power Supply',
               'Cisco Catalyst 9600 Series Power Supply',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Power Supply Bay Module Container',
               'Cisco Catalyst 9600 Series Power Supply Bay Module Container',
               'Cisco Catalyst 9600 Series Fan Tray Bay Module Container',
               'Cisco Catalyst 9600 Series C9606 Chassis Fan Tray',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan',
               'Cisco Catalyst 9600 Series Fan'],
 'hardware_version': ['V01',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'V02',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'V01',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'V01',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'V01',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL',
                      'NULL'],
 'name': ['Chassis',
          'Backplane',
          'slot 1',
          'slot 2',
          'slot 3',
          'slot 4',
          'slot 5',
          'slot 6',
          'slot R0',
          'Slot 3 Supervisor',
          'Slot 3 - USB Port0',
          'Hard Disk Container R0',
          'Slot 3 - USB Port1',
          'Slot 3 - NME',
          'R0 - NMTGE',
          'Slot 3 CPU',
          'slot R1',
          'slot F0',
          'slot F1',
          'PowerSupplyContainer1',
          'PowerSupplyModule1',
          'PowerSupply1',
          'Fan1/1',
          'Fan1/2',
          'PowerSupplyContainer2',
          'PowerSupplyModule2',
          'PowerSupply2',
          'Fan2/1',
          'Fan2/2',
          'PowerSupplyContainer3',
          'PowerSupplyContainer4',
          'FanContainer',
          'FanTray',
          'Fan5/1',
          'Fan5/2',
          'Fan5/3',
          'Fan5/4',
          'Fan5/5',
          'Fan5/6',
          'Fan5/7',
          'Fan5/8',
          'Fan5/9'],
 'part_number': ['C9606R',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'C9600-SUP-1',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'C9600-PWR-2KWAC',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'C9600-PWR-2KWAC',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'C9606-FAN',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL',
                 'NULL'],
 'serial_number': ['FXS2429Q4HV',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'FDO24261BQN',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'QCS24274X53',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'QCS24274X4L',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'DCH2413W086',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL',
                   'NULL']}
        self.assertEqual(result, expected_output)
