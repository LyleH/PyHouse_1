"""
This package is developing into two different areas.

The first area is for communication from external devices to the PyHouse Node system.
By this I mean devices such as a IR controller for various household devices and bluetooth receivers.

Remote controls come in two different flavors although some remotes may incorporate both modes.
Infra-Red remotes (IR) require a line of sight from the remote to it's receiver.
Radio Frequency (RF) remotes can control thru walls and other light structures.

IR remotes are setup using LIRC commands.  The remote requires a custom configuration file to translate
the key presses into a usable code.  irrecord is the LIRC program that creates this file.

The second area is for humans to communicate with humans.



I now live in two different houses, one for a little more than 6 or 7 months a year and in the other house 5 to 6 months each year.
Why should we have to give out several phone numbers and the people calling us have to guess which number to call?
So this communication module was born.

Cell phones changed the way we communicate and I believe that our communications will continue to change as we grow more technological.
I am not going to wait for the established utility companies give us new 'stuff'; it is time to invent it on our own.

I expect this module to change completely, several times even, as we invent different paradigms for communication.

Modules planned:
  Telephone - Primarily land line.
  Cellular - Cell Phones
  Fax - Getting obsolete methinks.
  Email - Home collection of various email accounts.

Perhaps these should go in here or perhaps in entertainment:
  Books - Collections of e-books for various family members
  Videos
  Music
  Photos


"""

__version_info__ = (1, 6, 0)
__version__ = '.'.join(map(str, __version_info__))

# ## END DBK
