"""
-*- test-case-name: PyHouse/src/Modules/Core/test/test_conversions.py -*-

@name:      PyHouse/src/Modules/Core/conversions.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2014-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Jul 14, 2014
@summary:   This module is for conversion routines.

"""

# Import system type stuff
import math

# Import PyMh files
from Modules.Computer import logging_pyh as Logger

LOG = Logger.getLogger('PyHouse.CoreConvert ')


"""
Internally, things are stored as integers but when working with humans dotted hex is easier to remember.

So for 1 to 4 bytes we convert 123456 to 'A1.b2.C3' and visa-versa.
"""

def _get_factor(p_size):
    """Internal utility to get a power of 256 (1 byte)
    """
    if p_size <= 1:
        return 0
    return int(math.pow(256, (p_size - 1)))

def _get_int(p_str):
    """Convert 2 hex chars into a 1 byte int.
    a3 --> 163
    """
    l_int = 0
    try:
        l_int = int(p_str, 16)
    except:
        l_int = 0
    return l_int

def dotted_hex2int(p_hex):
    """
    @param p_hex: is a str like 'A1.B2.C3'
    @return: an int
    """
    p_hex.replace(':', '.')
    l_ary = p_hex.split('.')
    l_hexn = ''.join(["%02X" % _get_int(l_ix) for l_ix in l_ary])
    return int(l_hexn, 16)

def int2dotted_hex(p_int, p_size):
    """
    @param p_int: is the integer to convert to a dotted hex string such as 'A1.B2' or 'C4.D3.E2'
    @param p_size: is the number of bytes to convert - either 2 or 3
    """
    l_ix = _get_factor(p_size)
    l_hex = []
    l_int = int(p_int)
    try:
        while l_ix > 0:
            l_byte, l_int = divmod(l_int, l_ix)
            l_hex.append("{:02X}".format(l_byte))
            l_ix = l_ix / 256
        return str('.'.join(l_hex))
    except TypeError as e_err:
        LOG.error('ERROR in converting int to dotted Hex {} - Type:{} - {}'.format(p_int, type(p_int), e_err))

def getbool(p_bool):
    if p_bool == 'True':
        return True
    return False

# ## END DBK
