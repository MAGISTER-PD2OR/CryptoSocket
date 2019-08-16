#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from CryptoSocket import Socket
from CryptoSocket.Crypto import Encrypter
from ObjectToTransfer import ObjectToTransfer


__package__ = 'Client example'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

def parse_args ():

  description = "Client script"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-l', required=True,  type=str, dest='local_address',  action='store', help='Local Address')
  parser.add_argument('-r', required=True,  type=str, dest='remote_address', action='store', help='Remote Address')
  parser.add_argument('-a', required=True,  type=int, dest='local_port',     action='store', help='Local Port')
  parser.add_argument('-t', required=True,  type=int, dest='remote_port',    action='store', help='Remote Port')
  parser.add_argument('-k', required=False, type=str, dest='keyfile',        action='store', help='Public KeyFile', default='')

  args = parser.parse_args()

  return args


if __name__ == '__main__':

  args = parse_args()

  if args.keyfile:

    with open(args.keyfile, 'r') as f:
      row = f.readline()

    n, e = tuple(map(int, row.split(' ')))
    enc = Encrypter(n, e)

  else:
    enc = None

  message = "This is the message."
  number  = 3.14
  array   = list(range(10))

  obj = ObjectToTransfer(message, number, array)

  with Socket(args.local_address, args.local_port, args.remote_address, args.remote_port) as sock:

    try:
      sock.send(obj, enc)

    except Exception as e:
      print("Unexpected error:", str(e))
      exit(1)

    finally:
      pass
