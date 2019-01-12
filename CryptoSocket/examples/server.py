#!/usr/bin/env python

from ObjectToTransfer import ObjectToTransfer
from CryptoSocket import Socket
from CryptoSocket.Crypto import Decrypter

import argparse
import sys

if __name__ == '__main__':


  description = "Server script"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-l', required=True,  dest='local_address',  action='store', help='Local Address')
  parser.add_argument('-r', required=True,  dest='remote_address', action='store', help='Remote Address')
  parser.add_argument('-a', required=True,  dest='local_port',     action='store', help='Local Port')
  parser.add_argument('-t', required=True,  dest='remote_port',    action='store', help='Remote Port')
  parser.add_argument('-k', required=False, dest='keyfile',        action='store', help='Private KeyFile', default='')

  if len(sys.argv) <= 4:
    parser.print_help()
    sys.exit(1)
  else:
    args = parser.parse_args()

  local_address = args.local_address
  local_port    = int(args.local_port)

  remote_address = args.remote_address
  remote_port    = int(args.remote_port)

  keyfile  = args.keyfile

  if keyfile:
    with open(keyfile, 'r') as f:
      row = f.readline()

    n, d = tuple(map(int, row.split(' ')))
    dec = Decrypter(n, d)
  else:
    dec = None

  with Socket(local_address, local_port, remote_address, remote_port) as sock:

    try:
      while True:
        obj = sock.recv(dec)
        print(obj)

    except KeyboardInterrupt:
      print('\nServer closed by user')
      pass

