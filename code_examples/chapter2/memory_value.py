from ctypes import string_at
from sys import getsizeof
from binascii import hexlify



# account for little and big endian - will only work in CPython
a = 0b01010000_01000001_01010100
bytestring = hexlify(string_at(id(a), getsizeof(a)))
assert b'544150' in bytestring or b'504154' in bytestring


text = "PAT"
bytestring = hexlify(string_at(id(text), getsizeof(text)))
assert b'544150' in bytestring or b'504154' in bytestring
