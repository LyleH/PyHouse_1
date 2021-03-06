"""
@name:      PyHouse/src/Modules/Computer/Nodes/test/test_nodes_xml.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2014-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Dec 15, 2014
@Summary:

Passed all 11 tests - DBK - 2016-06-07

"""

# Import system type stuff
import xml.etree.ElementTree as ET
from twisted.trial import unittest

# Import PyMh files and modules.
from Modules.Core.data_objects import NodeData, NodeInterfaceData
from Modules.Computer.Nodes.nodes_xml import Xml as nodesXml
from Modules.Computer.Nodes.test.xml_nodes import \
        TESTING_NODES_NODE_NAME_0, \
        TESTING_NODES_NODE_NAME_1, \
        TESTING_NODES_NODE_KEY_0, \
        TESTING_NODES_NODE_KEY_1, \
        TESTING_NODES_NODE_ACTIVE_0, \
        TESTING_NODES_NODE_ACTIVE_1, \
        TESTING_NODES_NODE_UUID_0, \
        TESTING_NODES_NODE_UUID_1, \
        TESTING_NODES_INTERFACE_NAME_0_0, \
        TESTING_NODES_INTERFACE_KEY_0_0, \
        TESTING_NODES_INTERFACE_ACTIVE_0_0, \
        TESTING_NODES_INTERFACE_MAC_ADDRESS_0_0, \
        TESTING_NODES_INTERFACE_ADDRESS_V4_0_0, \
        TESTING_NODES_INTERFACE_ADDRESS_V6_0_0, \
        TESTING_NODES_INTERFACE_NAME_0_1, \
        TESTING_NODES_INTERFACE_KEY_0_1, \
        TESTING_NODES_INTERFACE_ACTIVE_0_1, \
        TESTING_NODES_INTERFACE_NAME_0_2, \
        TESTING_NODES_INTERFACE_KEY_0_2, \
        TESTING_NODES_INTERFACE_ACTIVE_0_2, \
        TESTING_NODES_INTERFACE_UUID_0_0, \
        TESTING_NODES_INTERFACE_UUID_0_1, \
        TESTING_NODES_INTERFACE_UUID_0_2, \
        TESTING_NODES_INTERFACE_MAC_ADDRESS_0_1, \
        TESTING_NODES_INTERFACE_ADDRESS_V4_0_1, \
        TESTING_NODES_INTERFACE_ADDRESS_V6_0_1, \
        TESTING_NODES_INTERFACE_MAC_ADDRESS_0_2, \
        TESTING_NODES_INTERFACE_ADDRESS_V4_0_2, \
        TESTING_NODES_INTERFACE_ADDRESS_V6_0_2, \
        TESTING_NODES_CONNECTION_ADDRESS_V4_0, \
        TESTING_NODES_CONNECTION_ADDRESS_V6_0, \
        TESTING_NODES_INTERFACE_TYPE_0_0, \
        TESTING_NODES_NODE_ROLL_0, \
        TESTING_NODES_NODE_ROLL_1
from test.testing_mixin import SetupPyHouseObj
from test.xml_data import XML_LONG
from Modules.Utilities.debug_tools import PrettyFormatAny

DIVISION = 'ComputerDivision'
NODE_SECTION = 'NodeSection'


class SetupMixin(object):
    """
    """

    def setUp(self, p_root):
        self.m_pyhouse_obj = SetupPyHouseObj().BuildPyHouseObj(p_root)
        self.m_xml = SetupPyHouseObj().BuildXml(p_root)
        self.m_api = nodesXml()


class FakeNetiface(object):
    """
    """


class A1_Setup(SetupMixin, unittest.TestCase):
    """
    This section tests the reading and writing of XML used by node_local.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))
        self.m_interface_obj = NodeInterfaceData()
        self.m_node_obj = NodeData()

    def test_01_FindXml(self):
        """ Be sure that the XML contains the right stuff.
        Test some scattered things so we don't end up with hundreds of asserts.
        """
        # print(PrettyFormatAny.form(self.m_xml, 'Xml'))
        self.assertEqual(self.m_xml.root.tag, 'PyHouse')
        self.assertEqual(self.m_xml.computer_div.tag, DIVISION)

    def test_02_Computer(self):
        # print(PrettyFormatAny.form(self.m_pyhouse_obj.Computer, 'PyHouse'))
        self.assertEqual(self.m_xml.computer_div.tag, 'ComputerDivision')


class A2_Xml(SetupMixin, unittest.TestCase):
    """
    This section tests the reading and writing of XML used by node_local.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))
        self.m_interface_obj = NodeInterfaceData()
        self.m_node_obj = NodeData()

    def test_01_FindXML(self):
        """ Be sure that the XML contains the right stuff.
        Test some scattered things so we don't end up with hundreds of asserts.
        """
        # print(PrettyFormatAny.form(self.m_xml, 'Xml'))
        self.assertEqual(self.m_xml.root.tag, 'PyHouse')
        self.assertEqual(self.m_xml.computer_div.tag, DIVISION)
        self.assertEqual(self.m_xml.node_sect.tag, NODE_SECTION)


class B1_Read(SetupMixin, unittest.TestCase):
    """
    This section tests the reading and writing of XML used by node_local.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_1_OneInterface(self):
        l_interface = nodesXml._read_one_interface_xml(self.m_xml.interface)
        # print(PrettyFormatAny.form(l_interface, 'Interface'))
        self.assertEqual(l_interface.Name, TESTING_NODES_INTERFACE_NAME_0_0)
        self.assertEqual(l_interface.Key, int(TESTING_NODES_INTERFACE_KEY_0_0))
        self.assertEqual(l_interface.Active, bool(TESTING_NODES_INTERFACE_ACTIVE_0_0))
        self.assertEqual(l_interface.UUID, TESTING_NODES_INTERFACE_UUID_0_0)
        self.assertEqual(l_interface.NodeInterfaceType, TESTING_NODES_INTERFACE_TYPE_0_0)
        self.assertEqual(l_interface.MacAddress, TESTING_NODES_INTERFACE_MAC_ADDRESS_0_0)
        self.assertEqual(l_interface.V4Address, TESTING_NODES_INTERFACE_ADDRESS_V4_0_0)
        self.assertEqual(l_interface.V6Address, TESTING_NODES_INTERFACE_ADDRESS_V6_0_0)

    def test_2_AllInterfaces(self):
        l_interfaces = nodesXml._read_interfaces_xml(self.m_xml.interface_sect)
        # print(PrettyFormatAny.form(l_interfaces, 'Interfaces'))
        self.assertEqual(len(l_interfaces), 3)
        self.assertEqual(l_interfaces[0].Name, TESTING_NODES_INTERFACE_NAME_0_0)
        self.assertEqual(l_interfaces[0].Key, int(TESTING_NODES_INTERFACE_KEY_0_0))
        self.assertEqual(l_interfaces[0].Active, bool(TESTING_NODES_INTERFACE_ACTIVE_0_0))
        self.assertEqual(l_interfaces[0].UUID, TESTING_NODES_INTERFACE_UUID_0_0)
        self.assertEqual(l_interfaces[0].NodeInterfaceType, TESTING_NODES_INTERFACE_TYPE_0_0)
        self.assertEqual(l_interfaces[0].MacAddress, TESTING_NODES_INTERFACE_MAC_ADDRESS_0_0)
        self.assertEqual(l_interfaces[0].V4Address, TESTING_NODES_INTERFACE_ADDRESS_V4_0_0)
        self.assertEqual(l_interfaces[0].V6Address, TESTING_NODES_INTERFACE_ADDRESS_V6_0_0)
        self.assertEqual(l_interfaces[1].Name, TESTING_NODES_INTERFACE_NAME_0_1)
        self.assertEqual(l_interfaces[2].Name, TESTING_NODES_INTERFACE_NAME_0_2)
        self.assertEqual(len(l_interfaces), 3)

    def test_3_Node_0(self):
        print(PrettyFormatAny.form(self.m_xml.node, 'B1-3-A One Node XML'))
        l_node = nodesXml._read_one_node_xml(self.m_xml.node)
        print(PrettyFormatAny.form(l_node, 'B1-3-B One Node', 108))
        self.assertEqual(l_node.Name, TESTING_NODES_NODE_NAME_0)
        self.assertEqual(l_node.Key, int(TESTING_NODES_NODE_KEY_0))
        self.assertEqual(l_node.Active, bool(TESTING_NODES_NODE_ACTIVE_0))
        self.assertEqual(l_node.NodeRole, int(TESTING_NODES_NODE_ROLL_0))

    def test_4_Node_1(self):
        l_ix = self.m_xml.node_sect[1]
        print(PrettyFormatAny.form(l_ix, 'B1-4-A One Node XML'))
        l_node = nodesXml._read_one_node_xml(l_ix)
        print(PrettyFormatAny.form(l_node, 'B1-4-B One Node', 108))
        self.assertEqual(l_node.Name, TESTING_NODES_NODE_NAME_1)
        self.assertEqual(l_node.Key, int(TESTING_NODES_NODE_KEY_1))
        self.assertEqual(l_node.Active, bool(TESTING_NODES_NODE_ACTIVE_1))
        self.assertEqual(l_node.NodeRole, int(TESTING_NODES_NODE_ROLL_1))

    def test_5_AllNodes(self):
        l_nodes = nodesXml.read_all_nodes_xml(self.m_pyhouse_obj)
        print(PrettyFormatAny.form(l_nodes, 'B1-5 All Nodes', 108))
        # print(PrettyFormatAny.form(l_nodes[TESTING_NODES_NODE_NAME_0], 'Node 0', 10))
        # print(PrettyFormatAny.form(l_nodes[TESTING_NODES_NODE_NAME_0].NodeInterfaces, 'All Nodes', 10))
        self.assertEqual(len(l_nodes), 2)
        self.assertEqual(l_nodes[TESTING_NODES_NODE_UUID_0].Name, TESTING_NODES_NODE_NAME_0)
        self.assertEqual(l_nodes[TESTING_NODES_NODE_UUID_1].Name, TESTING_NODES_NODE_NAME_1)


class C1_Write(SetupMixin, unittest.TestCase):
    """
    This section tests the reading and writing of XML used by node_local.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_1_OneInterface(self):
        l_interface = nodesXml._read_one_interface_xml(self.m_xml.interface)
        l_xml = nodesXml._write_one_interface_xml(l_interface)
        # print(PrettyFormatAny.form(l_xml, 'C1-1 One Interface'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_NODES_INTERFACE_NAME_0_0)
        self.assertEqual(l_xml.attrib['Key'], TESTING_NODES_INTERFACE_KEY_0_0)
        self.assertEqual(l_xml.attrib['Active'], TESTING_NODES_INTERFACE_ACTIVE_0_0)
        self.assertEqual(l_xml[0].text, TESTING_NODES_INTERFACE_UUID_0_0)
        self.assertEqual(l_xml[1].text, TESTING_NODES_INTERFACE_MAC_ADDRESS_0_0)
        self.assertEqual(l_xml[2].text, TESTING_NODES_INTERFACE_ADDRESS_V4_0_0)
        self.assertEqual(l_xml[3].text, TESTING_NODES_INTERFACE_ADDRESS_V6_0_0)

    def test_2_AllInterfaces(self):
        l_interfaces = nodesXml._read_interfaces_xml(self.m_xml.interface_sect)
        l_xml = nodesXml._write_interfaces_xml(l_interfaces)
        # print(PrettyFormatAny.form(l_xml, 'C1-2 All Interfaces'))
        self.assertEqual(l_xml[0].attrib['Name'], TESTING_NODES_INTERFACE_NAME_0_0)
        self.assertEqual(l_xml[0].attrib['Key'], TESTING_NODES_INTERFACE_KEY_0_0)
        self.assertEqual(l_xml[0].attrib['Active'], TESTING_NODES_INTERFACE_ACTIVE_0_0)
        self.assertEqual(l_xml[0][0].text, TESTING_NODES_INTERFACE_UUID_0_0)
        self.assertEqual(l_xml[0][1].text, TESTING_NODES_INTERFACE_MAC_ADDRESS_0_0)
        self.assertEqual(l_xml[0][2].text, TESTING_NODES_INTERFACE_ADDRESS_V4_0_0)
        self.assertEqual(l_xml[0][3].text, TESTING_NODES_INTERFACE_ADDRESS_V6_0_0)
        self.assertEqual(l_xml[1].attrib['Name'], TESTING_NODES_INTERFACE_NAME_0_1)
        self.assertEqual(l_xml[1].attrib['Key'], TESTING_NODES_INTERFACE_KEY_0_1)
        self.assertEqual(l_xml[1].attrib['Active'], TESTING_NODES_INTERFACE_ACTIVE_0_1)
        self.assertEqual(l_xml[1][0].text, TESTING_NODES_INTERFACE_UUID_0_1)
        self.assertEqual(l_xml[1][1].text, TESTING_NODES_INTERFACE_MAC_ADDRESS_0_1)
        self.assertEqual(l_xml[1][2].text, TESTING_NODES_INTERFACE_ADDRESS_V4_0_1)
        self.assertEqual(l_xml[1][3].text, TESTING_NODES_INTERFACE_ADDRESS_V6_0_1)
        self.assertEqual(l_xml[2].attrib['Name'], TESTING_NODES_INTERFACE_NAME_0_2)
        self.assertEqual(l_xml[2].attrib['Key'], TESTING_NODES_INTERFACE_KEY_0_2)
        self.assertEqual(l_xml[2].attrib['Active'], TESTING_NODES_INTERFACE_ACTIVE_0_2)
        self.assertEqual(l_xml[2][0].text, TESTING_NODES_INTERFACE_UUID_0_2)
        self.assertEqual(l_xml[2][1].text, TESTING_NODES_INTERFACE_MAC_ADDRESS_0_2)
        self.assertEqual(l_xml[2][2].text, TESTING_NODES_INTERFACE_ADDRESS_V4_0_2)
        self.assertEqual(l_xml[2][3].text, TESTING_NODES_INTERFACE_ADDRESS_V6_0_2)

    def test_3_OneNode(self):
        l_node = nodesXml._read_one_node_xml(self.m_xml.node)
        l_xml = nodesXml._write_one_node_xml(l_node)
        # print(PrettyFormatAny.form(l_xml, 'C1-3-A One Node'))
        # print(PrettyFormatAny.form(l_xml[4][0], 'C1-3-B One Node 4-0'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_NODES_NODE_NAME_0)
        self.assertEqual(l_xml.attrib['Key'], TESTING_NODES_NODE_KEY_0)
        self.assertEqual(l_xml.attrib['Active'], TESTING_NODES_NODE_ACTIVE_0)
        self.assertEqual(l_xml[0].text, TESTING_NODES_NODE_UUID_0)
        self.assertEqual(l_xml[1].text, TESTING_NODES_CONNECTION_ADDRESS_V4_0)
        self.assertEqual(l_xml[2].text, TESTING_NODES_CONNECTION_ADDRESS_V6_0)
        self.assertEqual(l_xml[3].text, TESTING_NODES_NODE_ROLL_0)

    def test_4_AllNodes(self):
        l_nodes = nodesXml.read_all_nodes_xml(self.m_pyhouse_obj)
        print(PrettyFormatAny.form(l_nodes, 'C1-4-A All Nodes'))
        self.m_pyhouse_obj.Computer.Nodes = l_nodes
        l_xml, l_count = nodesXml.write_nodes_xml(self.m_pyhouse_obj)
        print(PrettyFormatAny.form(l_xml, 'C1-4-B All Nodes'))
        self.assertEqual(l_count, 2)
        self.assertEqual(l_xml[0].attrib['Name'], TESTING_NODES_NODE_NAME_1)
        self.assertEqual(l_xml[1].attrib['Name'], TESTING_NODES_NODE_NAME_0)
        self.assertEqual(l_xml[0].attrib['Key'], TESTING_NODES_NODE_KEY_1)
        self.assertEqual(l_xml[1].attrib['Key'], TESTING_NODES_NODE_KEY_0)
        self.assertEqual(l_xml[1].attrib['Active'], TESTING_NODES_NODE_ACTIVE_0)
        self.assertEqual(l_xml[4][0].attrib['Name'], TESTING_NODES_INTERFACE_NAME_0_0)
        self.assertEqual(l_xml[4][0].attrib['Key'], TESTING_NODES_INTERFACE_KEY_0_0)
        self.assertEqual(l_xml[4][0].attrib['Active'], TESTING_NODES_INTERFACE_ACTIVE_0_0)
        self.assertEqual(l_xml[4][1].attrib['Name'], TESTING_NODES_INTERFACE_NAME_0_1)
        self.assertEqual(l_xml[4][1].attrib['Key'], TESTING_NODES_INTERFACE_KEY_0_1)
        self.assertEqual(l_xml[4][1].attrib['Active'], TESTING_NODES_INTERFACE_ACTIVE_0_1)
        self.assertEqual(l_xml[4][2].attrib['Name'], TESTING_NODES_INTERFACE_NAME_0_2)
        self.assertEqual(l_xml[4][2].attrib['Key'], TESTING_NODES_INTERFACE_KEY_0_2)
        self.assertEqual(l_xml[4][2].attrib['Active'], TESTING_NODES_INTERFACE_ACTIVE_0_2)
        self.assertEqual(l_xml[1][0].text, TESTING_NODES_NODE_UUID_0)

# ## END DBK
