"""
@name:      PyHouse/src/Modules/families/Insteon/Insteon_PLM.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2013-2014 by D. Brian Kimmel
@note:      Created on Apr 8, 2013
@license:   MIT License
@summary:   This module is for driving serial devices

Passed all 10 tests - DBK - 2015-08-08

"""

# Import system type stuff
import xml.etree.ElementTree as ET
from twisted.trial import unittest

# Import PyMh files
from Modules.Core.data_objects import ControllerData
from test.xml_data import XML_LONG
from test.testing_mixin import SetupPyHouseObj


ADR_16C9D0 = '16.C9.D0'
ADR_17C272 = '17.C2.72'
BA_17C272 = bytearray(b'\x17\xc2\x72')
BA_1B4781 = bytearray(b'\x1b\x47\x81')
MSG_50 = bytearray(b'\x02\x50\x16\xc9\xd0\x1b\x47\x81\x27\x09\x00')
MSG_62 = bytearray(b'\x02\x62\x17\xc2\x72\x0f\x19\x00\x06')
MSG_99 = bytearray(b'\x02\x99')
MT_12345 = bytearray(b'\x02\x50\x14\x93\x6f\xaa\xaa\xaa\x07\x6e\x4f')
STX = 0x02


class SetupMixin(object):

    def setUp(self, p_root):
        self.m_pyhouse_obj = SetupPyHouseObj().BuildPyHouseObj(p_root)
        self.m_xml = SetupPyHouseObj().BuildXml(p_root)


class C01_Utility(SetupMixin, unittest.TestCase):

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_02_ExtractAddress(self):
        # self.assertEqual(self.m_api._get_addr_from_message(MSG_50, 2), conversions.dotted_hex2int(ADR_16C9D0))
        # self.assertEqual(self.m_api._get_addr_from_message(MSG_62, 2), conversions.dotted_hex2int(ADR_17C272))
        pass

    def test_04_Obj(self):
        l_house = self.m_pyhouse_obj.House
        self.assertEqual(l_house.Name, 'Test House')

    def test_05_Obj(self):
        pass


class C02_Cmds(SetupMixin, unittest.TestCase):

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))
        # self.m_pyhouse_obj.House.FamilyData = family.API(self.m_pyhouse_obj).build_lighting_family_info()

    # def test_01_get_message_length(self):
    #    self.assertEqual(utilUtil._get_message_length(MSG_50), 11)
    #    self.assertEqual(utilUtil._get_message_length(MSG_62), 9)
    #    self.assertEqual(utilUtil._get_message_length(MSG_99), 1)

    # def test_02_Command(self):
    #    l_cmd = utilUtil._create_command_message('insteon_send')
    #    self.assertEqual(l_cmd[0], 0x02)
    #    self.assertEqual(l_cmd[1], 0x62)

    def test_03_63Cmd(self):
        l_obj = self.m_pyhouse_obj.House.Lighting.Controllers
        # insteonPlmAPI._put_controller(l_obj)
        # l_cmd = self.m_api.queue_62_command(l_obj, 0x02, 0x04)
        pass


class C03_Driver(SetupMixin, unittest.TestCase):
    """
    """

    def setUp(self):
        pass

    def test_01_Driver(self):
        pass


class C04_Thermostat(SetupMixin, unittest.TestCase):

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))
        self.m_controller_obj = ControllerData()

    def test_01_x(self):
        pass

# ## END DBK
