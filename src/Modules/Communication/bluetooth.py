"""
-*- test-case-name: PyHouse.src.Modules.communication.test.test_bluetooth -*-

@name:      PyHouse/src/Modules/communication/bluteooth.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2013-2016 by D. Brian Kimmel
@note:      Created on Nov 18, 2013
@license:   MIT License
@summary:   Provides PyHouse bluetooth.


interface a bluetooth usb dongle to connect with cell phones and other devices.
"""

#  Import system type stuff


class API(object):

    def __init__(self, p_pyhouse_obj):
        self.m_pyhouse_obj = p_pyhouse_obj

    def LoadXml(self, p_pyhouse_obj):
        p_pyhouse_obj.Computer.Communication = Utility().read_xml(p_pyhouse_obj)

    def Start(self):
        pass

    def SaveXml(self, p_xml):
        l_xml = ET.Element('CommunicationSection')
        p_xml.append(l_xml)
        LOG.info("Saved XML.")
        return p_xml

    def Stop(self):
        pass

# ## END DBK
