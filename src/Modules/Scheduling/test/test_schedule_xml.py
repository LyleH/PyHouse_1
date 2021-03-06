"""
@name:      PyHouse/src/Modules/Scheduling/test/test_schedule_xml.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com>
@copyright: (c) 2014-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Sep 2, 2014
@Summary:

Passed all 13 tests - DBK - 2016-07-05

"""

# Import system type stuff
import xml.etree.ElementTree as ET
from twisted.trial import unittest

# Import PyMh files and modules.
from Modules.Core.data_objects import ScheduleBaseData
from Modules.Scheduling.schedule_xml import Xml as scheduleXml
from test.xml_data import XML_LONG
from test.testing_mixin import SetupPyHouseObj
from Modules.Lighting.test.xml_lights import TESTING_LIGHT_NAME_0
from Modules.Scheduling.test.xml_schedule import TESTING_SCHEDULE_NAME_0, TESTING_SCHEDULE_KEY_0, \
    TESTING_SCHEDULE_MODE_0, TESTING_SCHEDULE_ACTIVE_0, TESTING_SCHEDULE_TYPE_0, TESTING_SCHEDULE_TIME_0, \
    TESTING_SCHEDULE_DOW_0, \
    TESTING_SCHEDULE_NAME_1, \
    TESTING_SCHEDULE_NAME_2, \
    TESTING_SCHEDULE_NAME_3, \
    TESTING_SCHEDULE_DOW_1, \
    TESTING_SCHEDULE_DOW_2, \
    TESTING_SCHEDULE_DOW_3, \
    TESTING_SCHEDULE_UUID_0, TESTING_SCHEDULE_ROOM_NAME_0, TESTING_SCHEDULE_ROOM_UUID_0, TESTING_SCHEDULE_LIGHT_UUID_0, \
    TESTING_SCHEDULE_LIGHT_NAME_0, TESTING_SCHEDULE_LEVEL_0, TESTING_SCHEDULE_RATE_0
from Modules.Utilities.debug_tools import PrettyFormatAny
from Modules.Housing.test.xml_housing import TESTING_HOUSE_NAME, TESTING_HOUSE_ACTIVE, TESTING_HOUSE_KEY, \
    TESTING_HOUSE_UUID


class SetupMixin(object):
    """
    """

    def setUp(self, p_root):
        self.m_pyhouse_obj = SetupPyHouseObj().BuildPyHouseObj(p_root)
        self.m_xml = SetupPyHouseObj().BuildXml(p_root)
        self.m_schedule_obj = ScheduleBaseData()
        self.m_api = scheduleXml()


class A1_Setup(SetupMixin, unittest.TestCase):
    """
    This section tests the reading and writing of XML used by schedules.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_1_BuildObjects(self):
        """ Test to be sure the compound object was built correctly - Rooms is an empty dict.
        """
        # print(PrettyFormatAny.form(self.m_xml, 'Tags'))
        self.assertEqual(self.m_pyhouse_obj.House.Schedules, None)

    def test_2_FindXML(self):
        """ Be sure that the XML contains the right stuff.
        """
        # print(PrettyFormatAny.form(self.m_xml, 'A1-1-A - Tags'))
        self.assertEqual(self.m_xml.root.tag, 'PyHouse')
        self.assertEqual(self.m_xml.house_div.tag, 'HouseDivision')
        self.assertEqual(self.m_xml.schedule_sect.tag, 'ScheduleSection')
        self.assertEqual(self.m_xml.schedule.tag, 'Schedule')


class A2_XML(SetupMixin, unittest.TestCase):
    """
    Be sure that we load the data properly as a whole test.
    Detailed test of xml is in the test_schedule_xml module.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_1_HouseDiv(self):
        """ Test
        """
        l_xml = self.m_xml.house_div
        # print(PrettyFormatAny.form(l_xml, 'House'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_HOUSE_NAME)
        self.assertEqual(l_xml.attrib['Active'], TESTING_HOUSE_ACTIVE)
        self.assertEqual(l_xml.attrib['Key'], TESTING_HOUSE_KEY)
        self.assertEqual(l_xml.find('UUID').text, TESTING_HOUSE_UUID)

    def test_2_ScheduleSect(self):
        """ Test
        """
        l_xml = self.m_xml.schedule_sect
        l_len = len(l_xml)
        # print(PrettyFormatAny.form(l_xml, 'A2-2-A - Schedule Sect'))
        self.assertEqual(l_len, 4)

    def test_3_Schedule(self):
        """ Test
        """
        l_xml = self.m_xml.schedule
        # print(PrettyFormatAny.form(l_xml, 'A2-3-A - Schedule'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_SCHEDULE_NAME_0)
        self.assertEqual(l_xml.attrib['Active'], TESTING_SCHEDULE_ACTIVE_0)
        self.assertEqual(l_xml.attrib['Key'], TESTING_SCHEDULE_KEY_0)
        self.assertEqual(l_xml.find('UUID').text, TESTING_SCHEDULE_UUID_0)


class B1_Read(SetupMixin, unittest.TestCase):
    """
    This section tests the reading of XML used by schedules.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_1_OneBase(self):
        """ Read in the xml file and fill in x
        """
        l_obj = scheduleXml._read_one_base_schedule(self.m_xml.schedule)
        # print(PrettyFormatAny.form(l_obj, 'B1-1-A - OneBase'))
        self.assertEqual(l_obj.Name, TESTING_SCHEDULE_NAME_0)
        self.assertEqual(str(l_obj.Key), TESTING_SCHEDULE_KEY_0)
        self.assertEqual(str(l_obj.Active), TESTING_SCHEDULE_ACTIVE_0)
        self.assertEqual(l_obj.UUID, TESTING_SCHEDULE_UUID_0)
        #
        self.assertEqual(str(l_obj.DOW), TESTING_SCHEDULE_DOW_0)
        self.assertEqual(l_obj.ScheduleType, TESTING_SCHEDULE_TYPE_0)
        self.assertEqual(l_obj.ScheduleMode, TESTING_SCHEDULE_MODE_0)
        self.assertEqual(l_obj.Time, TESTING_SCHEDULE_TIME_0)

    def test_2_OneLight(self):
        l_obj = scheduleXml._read_one_lighting_schedule(self.m_xml.schedule)
        # print(PrettyFormatAny.form(l_obj, 'B1-2-A - One Light'))
        self.assertEqual(l_obj.Name, TESTING_SCHEDULE_NAME_0)
        self.assertEqual(str(l_obj.Key), TESTING_SCHEDULE_KEY_0)
        self.assertEqual(str(l_obj.Active), TESTING_SCHEDULE_ACTIVE_0)
        self.assertEqual(l_obj.UUID, TESTING_SCHEDULE_UUID_0)
        #
        self.assertEqual(str(l_obj.Level), TESTING_SCHEDULE_LEVEL_0)
        self.assertEqual(l_obj.LightName, TESTING_SCHEDULE_LIGHT_NAME_0)
        self.assertEqual(l_obj.LightUUID, TESTING_SCHEDULE_LIGHT_UUID_0)
        self.assertEqual(str(l_obj.Rate), TESTING_SCHEDULE_RATE_0)
        self.assertEqual(l_obj.RoomName, TESTING_SCHEDULE_ROOM_NAME_0)
        self.assertEqual(l_obj.RoomUUID, TESTING_SCHEDULE_ROOM_UUID_0)

    def test_3_OneSchedule(self):
        l_sched = scheduleXml._read_one_schedule(self.m_xml.schedule)
        # print(PrettyFormatAny.form(l_sched, 'B1-3-A - One Schedule'))
        self.assertEqual(l_sched.Name, 'Evening 1')
        self.assertEqual(l_sched.LightName, TESTING_LIGHT_NAME_0)
        self.assertEqual(l_sched.RoomName, TESTING_SCHEDULE_ROOM_NAME_0)

    def test_4_AllSchedules(self):
        l_schedules = scheduleXml.read_schedules_xml(self.m_pyhouse_obj)
        # print(PrettyFormatAny.form(l_schedules, 'B1-4-A - Schedules'))
        # print(PrettyFormatAny.form(l_schedules[0], 'Schedules'))
        # print(PrettyFormatAny.form(l_schedules[1], 'Schedules'))
        # print(PrettyFormatAny.form(l_schedules[2], 'Schedules'))
        # print(PrettyFormatAny.form(l_schedules[3], 'Schedules'))
        self.assertEqual(len(l_schedules), 4)


class B2_Write(SetupMixin, unittest.TestCase):
    """
    This section tests the reading and writing of XML used by schedules.
    """

    def setUp(self):
        SetupMixin.setUp(self, ET.fromstring(XML_LONG))

    def test_1_OneBase(self):
        l_schedule = scheduleXml._read_one_schedule(self.m_xml.schedule)
        l_xml = scheduleXml._write_one_base_schedule(l_schedule)
        # print(PrettyFormatAny.form(l_xml, 'B2-1-A - One Interface'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_SCHEDULE_NAME_0)
        self.assertEqual(l_xml.attrib['Key'], TESTING_SCHEDULE_KEY_0)
        self.assertEqual(l_xml.attrib['Active'], TESTING_SCHEDULE_ACTIVE_0)
        self.assertEqual(l_xml.find('UUID').text, TESTING_SCHEDULE_UUID_0)
        self.assertEqual(l_xml.find('DayOfWeek').text, TESTING_SCHEDULE_DOW_0)
        self.assertEqual(l_xml.find('ScheduleMode').text, TESTING_SCHEDULE_MODE_0)
        self.assertEqual(l_xml.find('ScheduleType').text, TESTING_SCHEDULE_TYPE_0)
        self.assertEqual(l_xml.find('Time').text, TESTING_SCHEDULE_TIME_0)

    def test_2_OneLight(self):
        l_schedule = scheduleXml._read_one_schedule(self.m_xml.schedule)
        l_xml = scheduleXml._write_one_base_schedule(l_schedule)
        scheduleXml._write_one_light_schedule(l_schedule, l_xml)
        # print(PrettyFormatAny.form(l_xml, 'B2-2-A - One Light'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_SCHEDULE_NAME_0)
        self.assertEqual(l_xml.attrib['Key'], TESTING_SCHEDULE_KEY_0)
        self.assertEqual(l_xml.attrib['Active'], TESTING_SCHEDULE_ACTIVE_0)
        self.assertEqual(l_xml.find('UUID').text, TESTING_SCHEDULE_UUID_0)
        self.assertEqual(l_xml.find('DayOfWeek').text, TESTING_SCHEDULE_DOW_0)
        self.assertEqual(l_xml.find('ScheduleMode').text, TESTING_SCHEDULE_MODE_0)
        self.assertEqual(l_xml.find('ScheduleType').text, TESTING_SCHEDULE_TYPE_0)
        self.assertEqual(l_xml.find('Time').text, TESTING_SCHEDULE_TIME_0)
        self.assertEqual(l_xml.find('Level').text, TESTING_SCHEDULE_LEVEL_0)
        self.assertEqual(l_xml.find('LightName').text, TESTING_SCHEDULE_LIGHT_NAME_0)
        self.assertEqual(l_xml.find('LightUUID').text, TESTING_SCHEDULE_LIGHT_UUID_0)
        self.assertEqual(l_xml.find('Rate').text, TESTING_SCHEDULE_RATE_0)
        self.assertEqual(l_xml.find('RoomName').text, TESTING_SCHEDULE_ROOM_NAME_0)
        self.assertEqual(l_xml.find('RoomUUID').text, TESTING_SCHEDULE_ROOM_UUID_0)

    def test_3_OneSchedule(self):
        l_schedule = scheduleXml._read_one_schedule(self.m_xml.schedule)
        l_xml = scheduleXml._write_one_schedule(l_schedule)
        # print(PrettyFormatAny.form(l_xml, 'B2-3-A - One Schedule'))
        self.assertEqual(l_xml.attrib['Name'], TESTING_SCHEDULE_NAME_0)

    def test_4_AllSchedules(self):
        l_schedules = scheduleXml.read_schedules_xml(self.m_pyhouse_obj)
        l_xml, l_count = scheduleXml.write_schedules_xml(l_schedules)
        # print(PrettyFormatAny.form(l_xml, 'B2-4-A - All Interfaces'))
        self.assertEqual(l_count, len(l_schedules))
        self.assertEqual(l_xml[0].attrib['Name'], TESTING_SCHEDULE_NAME_0)
        self.assertEqual(l_xml[0][1].text, TESTING_SCHEDULE_DOW_0)
        self.assertEqual(l_xml[1].attrib['Name'], TESTING_SCHEDULE_NAME_1)
        self.assertEqual(l_xml[1][1].text, TESTING_SCHEDULE_DOW_1)
        self.assertEqual(l_xml[2].attrib['Name'], TESTING_SCHEDULE_NAME_2)
        self.assertEqual(l_xml[2][1].text, TESTING_SCHEDULE_DOW_2)
        self.assertEqual(l_xml[3].attrib['Name'], TESTING_SCHEDULE_NAME_3)
        self.assertEqual(l_xml[3][1].text, TESTING_SCHEDULE_DOW_3)

# ## END DBK
