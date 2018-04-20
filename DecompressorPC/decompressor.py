#!/usr/bin/env python

import sys
import tos
from datetime import datetime

if '-h' in sys.argv:
  print "Usage:", sys.argv[0], "serial@/dev/ttyUSB0:115200"
  print "      ", sys.argv[0], "network@host:port"
  sys.exit()

AM_TRANSMIT_BEGIN_MSG = 0x40
AM_TRANSMIT_BEGIN_ACK_MSG = 0x41
AM_PARTIAL_DATA_MSG = 0x42
AM_TRANSMIT_END_MSG = 0x43

am = tos.AM()

while True:
  print 'Listening...'
  p = am.read()
  if p:
    if p.type == AM_TRANSMIT_BEGIN_MSG:
      print 'Received TRANSMIT BEGIN message. Sending acknowledgement'
      msg = tos.ActiveMessage([9], AM_TRANSMIT_BEGIN_ACK_MSG)
      am.write(msg, AM_TRANSMIT_BEGIN_ACK_MSG)
      print ' - Acknowledgement sent'
      file_name = datetime.now().strftime('received-file-%Y%m%d%H%M%S.bin')
      f = open(file_name, 'wb')
    elif p.type == AM_PARTIAL_DATA_MSG:
      print 'Received partial data'
      if f:
        f.write(bytearray(p.data))
      else:
        print 'File not open'
    elif p.type == AM_TRANSMIT_END_MSG:
      print 'Received TRANSMIT END data'
      if f:
        f.close()
      else:
        print 'File not open'
    else:
      print 'Received unknown packet'
    #print '\n\n   PACKET OUTOUT'
    #print '====================='
    #print p
    #print '=====================\n\n'
  else:
    print 'Did not receive any packet!'