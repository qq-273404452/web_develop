from snap7.client import Client
import struct

plc=Client()
plc.connect('192.168.14.100',0,1)
data=plc.db_read('16',)