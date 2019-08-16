#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from CryptoSocket.Crypto import Decrypter

__package__ = 'Decrypter'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

def parse_args ():

  description = "Decrypter"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-k', type=str, required=True, dest='public', action='store', help='Public KeyFile')
  parser.add_argument('-f', type=str, required=False, dest='filename', action='store', help='Filename of encrypted message', default='')
  parser.add_argument('-c', type=int, required=False, dest='code', action='store', nargs='+', help='List of integers to decrypt', default=[])

  args = parser.parse_args()

  if not args.code and not args.filename:
    raise ValueError('Missing parameter! Give a text filename or a code in a list')

  return args


if __name__ == '__main__':

  args = parse_args()

  with open(args.public, 'r') as fp:
    row = fp.readline()
    n, d = tuple(map(int, row.split(' ')))

  dec = Decrypter(n, d)

  if os.path.exists(args.filename):

    with open(args.filename, 'r') as fp:
      args.filename = fp.readlines()

    text = map(int, args.filename.split(' '))

  else:

    text = args.code

  decoded = dec.decrypt(text)

  print(decoded)
