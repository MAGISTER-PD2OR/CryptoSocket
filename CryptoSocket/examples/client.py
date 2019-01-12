#!/usr/bin/env python

from ObjectToTransfer import ObjectToTransfer
from CryptoSocket import Socket
from CryptoSocket.Crypto import Encrypter

import argparse
import sys

if __name__ == '__main__':


  description = "Client script"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-l', required=True,  dest='local_address',  action='store', help='Local Address')
  parser.add_argument('-r', required=True,  dest='remote_address', action='store', help='Remote Address')
  parser.add_argument('-a', required=True,  dest='local_port',     action='store', help='Local Port')
  parser.add_argument('-t', required=True,  dest='remote_port',    action='store', help='Remote Port')
  parser.add_argument('-k', required=False, dest='keyfile',        action='store', help='Public KeyFile', default='')

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

    n, e = tuple(map(int, row.split(' ')))
    enc = Encrypter(n, e)
  else:
    enc = None

  message = "This is the message."
  number  = 3.14
  array   = list(range(10))

  obj = ObjectToTransfer(message, number, array)

  with Socket(local_address, local_port, remote_address, remote_port) as sock:

    try:
      sock.send(obj, enc)

    except Exception as e:
      print("Unexpected error:", str(e))
      exit(1)

    finally:
      pass
