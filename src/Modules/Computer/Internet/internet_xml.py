"""
-*- test-case-name: PyHouse.src.Modules.Computer.Internet.test.test_internet_xml -*-

@name:      PyHouse/src/Modules/Computer/Internet/internet_xml.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2014-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Sep 29, 2014
@Summary:

"""
#  Import system type stuff
import xml.etree.ElementTree as ET

#  Import PyMh files and modules.
from Modules.Core.data_objects import InternetConnectionData
from Modules.Utilities.xml_tools import PutGetXML
from Modules.Computer import logging_pyh as Logger

LOG = Logger.getLogger('PyHouse.Internet_xml   ')


class Util(object):
    """
    This section is fairly well tested by the unit test module.
    """

    @staticmethod
    def _read_locates_xml(p_locater_sect_xml):
        l_dict = {}
        l_count = 0
        try:
            for l_xml in p_locater_sect_xml.iterfind('LocateUrl'):
                l_url = str(l_xml.text)
                l_dict[l_count] = l_url
                l_count += 1
        except AttributeError as e_err:
            LOG.error('ERROR in read_locates_xml - {}'.format(e_err))
        return l_dict

    @staticmethod
    def _read_updates_xml(p_updater_sect_xml):
        l_dict = {}
        l_count = 0
        try:
            for l_xml in p_updater_sect_xml.iterfind('UpdateUrl'):
                l_url = str(l_xml.text)
                l_dict[l_count] = l_url
                l_count += 1
        except AttributeError as e_err:
            LOG.error('ERROR in read_updates_xml - {}'.format(e_err))
        return l_dict

    @staticmethod
    def _read_derived(p_internet_sect_xml):
        l_icd = InternetConnectionData()
        try:
            l_icd.ExternalIPv4 = PutGetXML.get_ip_from_xml(p_internet_sect_xml, 'ExternalIPv4')
            l_icd.ExternalIPv6 = PutGetXML.get_ip_from_xml(p_internet_sect_xml, 'ExternalIPv6')
            l_icd.LastChanged = PutGetXML.get_date_time_from_xml(p_internet_sect_xml, 'LastChanged')
        except:
            pass
        return l_icd


    @staticmethod
    def _write_locates_xml(p_internet_obj):
        l_xml = ET.Element('LocaterUrlSection')
        for l_url in p_internet_obj.LocateUrls.itervalues():
            PutGetXML.put_text_element(l_xml, 'LocateUrl', l_url)
        return l_xml

    @staticmethod
    def _write_updates_xml(p_dns_obj):
        l_xml = ET.Element('UpdaterUrlSection')
        for l_url in p_dns_obj.UpdateUrls.itervalues():
            PutGetXML.put_text_element(l_xml, 'UpdateUrl', l_url)
        return l_xml

    @staticmethod
    def _write_derived_xml(p_internet_obj, p_xml):
        PutGetXML.put_text_element(p_xml, 'ExternalIPv4', p_internet_obj.ExternalIPv4)
        PutGetXML.put_text_element(p_xml, 'ExternalIPv6', p_internet_obj.ExternalIPv6)
        PutGetXML.put_text_element(p_xml, 'LastChanged', p_internet_obj.LastChanged)



class API(object):

    def read_internet_xml(self, p_pyhouse_obj):
        """Reads zero or more <Internet> entries within the <InternetSection>
        @param p_internet_section_xml: is the <InternetSection> element
        """
        l_icd = InternetConnectionData()
        l_xml = p_pyhouse_obj.Xml.XmlRoot
        try:
            l_xml = l_xml.find('ComputerDivision')
            if l_xml == None:
                return l_icd
            l_internet_sect_xml = l_xml.find('InternetSection')
        except AttributeError as e_err:
            l_internet_sect_xml = None
            LOG.error('Internet section missing from XML - {}'.format(e_err))
        try:
            l_icd = Util._read_derived(l_internet_sect_xml)
            l_icd.LocateUrls = Util._read_locates_xml(l_internet_sect_xml.find('LocaterUrlSection'))
            l_icd.UpdateUrls = Util._read_updates_xml(l_internet_sect_xml.find('UpdaterUrlSection'))
        except AttributeError as e_err:
            LOG.error('ERROR ReadInternet - {}'.format(e_err))
        LOG.info('Loaded Internet XML')
        return l_icd


    def write_internet_xml(self, p_internet_obj):
        """Create a sub tree for 'Internet' - the sub elements do not have to be present.
        @param p_internet_obj: is pyhouse_obj.Computer.InternetConnection
        @return: a sub tree ready to be appended to tree
        """
        l_xml = ET.Element('InternetSection')
        Util._write_derived_xml(p_internet_obj, l_xml)
        l_xml.append(Util._write_locates_xml(p_internet_obj))
        l_xml.append(Util._write_updates_xml(p_internet_obj))
        return l_xml

#  ## END DBK
