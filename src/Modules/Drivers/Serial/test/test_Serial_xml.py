"""
@name:      PyHouse/src/Modules/Drivers/Serial/test/test_serial_xml.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com>
@copyright: (c) 2014-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Aug 5, 2014
@Summary:

Passed all 7 tests - DBK - 2016-06-25

"""

# Import system type stuff
import xml.etree.ElementTree as ET
from twisted.trial import unittest

# Import PyMh files and modules.
from Modules.Core.data_objects import ControllerData
from Modules.Drivers.Serial.Serial_xml import XML as serialXML
from test.xml_data import XML_LONG
from test.testing_mixin import SetupPyHouseObj
from Modules.Utilities.xml_tools import stuff_new_attrs
from Modules.Utilities.debug_tools import PrettyFormatAny
from Modules.Lighting.test.xml_controllers import \
    TESTING_CONTROLLER_NAME_0, \
    TESTING_CONTROLLER_NAME_1
from Modules.Drivers.Serial.test.xml_serial import \
    TESTING_SERIAL_BAUD_RATE, \
    TESTING_SERIAL_BYTE_SIZE, \
    TESTING_SERIAL_DSR_DTR, \
    TESTING_SERIAL_PARITY, \
    TESTING_SERIAL_RTS_CTS, \
    TESTING_SERIAL_STOP_BITS, \
    TESTING_SERIAL_TIMEOUT, \
    TESTING_SERIAL_XON_XOFF


class SetupMixin(object):
    """
    """

    def setUp(self, p_root):
        self.m_pyhouse_obj = SetupPyHouseObj().BuildPyHouseObj(p_root)
        self.m_xml = SetupPyHouseObj().BuildXml(p_root)
        self.m_controller_obj = ControllerData()
        self.m_controller_obj.InterfaceType = 'Serial'
        self.m_version = '1.4.0'


class A1_Setup(SetupMixin, unittest.TestCase):
    """ This section tests the reading and writing of XML used by lighting_controllers.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))
        # self.m_pyhouse_obj.House.FamilyData = family.API(self.m_pyhouse_obj).build_lighting_family_info()

    def test_1_Tags(self):
        """ Be sure
        """
        # print(PrettyFormatAny.form(self.m_xml, "Tags"))
        self.assertEqual(self.m_xml.root.tag, 'PyHouse')
        self.assertEqual(self.m_xml.house_div.tag, 'HouseDivision')
        self.assertEqual(self.m_xml.lighting_sect.tag, 'LightingSection')
        self.assertEqual(self.m_xml.controller_sect.tag, 'ControllerSection')
        self.assertEqual(self.m_xml.controller.tag, 'Controller')


class A2_Setup(SetupMixin, unittest.TestCase):
    """ This section tests the reading and writing of XML used by lighting_controllers.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))
        # self.m_pyhouse_obj.House.FamilyData = family.API(self.m_pyhouse_obj).build_lighting_family_info()

    def test_1_Xml(self):
        """ Be sure that the XML contains the right stuff.
        """
        # print(PrettyFormatAny.form(XML_LONG, "XML"))
        self.assertEqual(self.m_xml.root.tag, 'PyHouse')
        self.assertEqual(self.m_xml.controller_sect.tag, 'ControllerSection')
        self.assertEqual(self.m_xml.controller.tag, 'Controller')

    def test_2_Controllers(self):
        """ Be sure that the XML contains the right stuff.
        """
        l_xml = self.m_xml.controller_sect
        print(PrettyFormatAny.form(l_xml, 'Controllers'))
        self.assertEqual(l_xml[0].attrib['Name'], TESTING_CONTROLLER_NAME_0)
        self.assertEqual(l_xml[1].attrib['Name'], TESTING_CONTROLLER_NAME_1)

    def test_3_Controller(self):
        """ Be sure that the XML contains the right stuff.
        """
        l_xml = self.m_xml.controller
        print(PrettyFormatAny.form(l_xml, 'Controller'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_CONTROLLER_NAME_0)


class B1_XML(SetupMixin, unittest.TestCase):
    """ This section tests the reading and writing of XML used by lighting_controllers.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))
        self.m_controller_obj.InterfaceType = 'Serial'

    def test_01_FindXml(self):
        """ Be sure that the XML contains the right stuff.
        """
        # print(PrettyFormatAny.form(self.m_xml, "Tags"))
        self.assertEqual(self.m_xml.root.tag, 'PyHouse', 'Invalid XML - not a PyHouse XML config file')
        self.assertEqual(self.m_xml.controller_sect.tag, 'ControllerSection', 'XML - No Controllers section')
        self.assertEqual(self.m_xml.controller.tag, 'Controller', 'XML - No Controller section')

    def test_02_ReadSerialXml(self):
        l_interface = serialXML.read_interface_xml(self.m_xml.controller)
        # print(PrettyFormatAny.form(l_interface, "Interface"))
        self.assertEqual(str(l_interface.BaudRate), TESTING_SERIAL_BAUD_RATE)
        self.assertEqual(str(l_interface.ByteSize), TESTING_SERIAL_BYTE_SIZE)
        self.assertEqual(str(l_interface.DsrDtr), TESTING_SERIAL_DSR_DTR)
        self.assertEqual(l_interface.Parity, TESTING_SERIAL_PARITY)
        self.assertEqual(str(l_interface.RtsCts), TESTING_SERIAL_RTS_CTS)
        self.assertEqual(str(l_interface.StopBits), TESTING_SERIAL_STOP_BITS)
        self.assertEqual(str(l_interface.Timeout), TESTING_SERIAL_TIMEOUT)
        self.assertEqual(str(l_interface.XonXoff), TESTING_SERIAL_XON_XOFF)


class B2_Write(SetupMixin, unittest.TestCase):
    """ This section tests the reading and writing of XML used by lighting_controllers.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_01_WriteSerialXml(self):
        l_interface = serialXML.read_interface_xml(self.m_xml.controller)
        stuff_new_attrs(self.m_controller_obj, l_interface)
        l_xml = ET.Element('TestOutput')
        l_xml = serialXML.write_interface_xml(l_xml, self.m_controller_obj)
        # print(PrettyFormatAny.form(l_xml, "Interface"))
        self.assertEqual(l_xml.find('BaudRate').text, TESTING_SERIAL_BAUD_RATE)
        self.assertEqual(l_xml.find('ByteSize').text, TESTING_SERIAL_BYTE_SIZE)
        self.assertEqual(l_xml.find('DsrDtr').text, TESTING_SERIAL_DSR_DTR)
        self.assertEqual(l_xml.find('Parity').text, TESTING_SERIAL_PARITY)
        self.assertEqual(l_xml.find('RtsCts').text, TESTING_SERIAL_RTS_CTS)
        self.assertEqual(l_xml.find('StopBits').text, TESTING_SERIAL_STOP_BITS)
        self.assertEqual(l_xml.find('Timeout').text, TESTING_SERIAL_TIMEOUT)
        self.assertEqual(l_xml.find('XonXoff').text, TESTING_SERIAL_XON_XOFF)

# ## END
