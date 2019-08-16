#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from ObjectToTransfer import ObjectToTransfer
from CryptoSocket import Socket
from CryptoSocket.Crypto import Decrypter

__package__ = 'Server example'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

def parse_args ():

  description = "Server script"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-l', type=str, required=True,  dest='local_address',  action='store', help='Local Address')
  parser.add_argument('-r', type=str, required=True,  dest='remote_address', action='store', help='Remote Address')
  parser.add_argument('-a', type=int, required=True,  dest='local_port',     action='store', help='Local Port')
  parser.add_argument('-t', type=int, required=True,  dest='remote_port',    action='store', help='Remote Port')
  parser.add_argument('-k', type=str, required=False, dest='keyfile',        action='store', help='Private KeyFile', default='')

  args = parser.parse_args()

  return args


if __name__ == '__main__':

  args = parse_args()

  if args.keyfile:
    with open(args.keyfile, 'r') as f:
      row = f.readline()

    n, d = tuple(map(int, row.split(' ')))
    dec = Decrypter(n, d)
  else:
    dec = None

  with Socket(args.local_address, args.local_port, args.remote_address, args.remote_port) as sock:

    try:
      while True:
        obj = sock.recv(dec)
        print(obj)

    except KeyboardInterrupt:
      print('\nServer closed by user')
      pass

