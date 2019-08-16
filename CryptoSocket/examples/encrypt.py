#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from CryptoSocket.Crypto import Encrypter

__package__ = 'Encrypter'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

def parse_args ():

  description = "Encrypter"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-k', type=str, required=True, dest='private', action='store', help='Private KeyFile')
  parser.add_argument('-f', type=str, required=True, dest='text',    action='store', help='Text string or filename')

  args = parser.parse_args()

  return args


if __name__ == '__main__':

  args = parse_args()

  with open(args.private, 'r') as fp:
    row = fp.readline()
    n, e = tuple(map(int, row.split(' ')))

  enc = Encrypter(n, e)

  if os.path.exists(args.text):

    with open(args.text, 'r') as fp:
      args.text = fp.readlines()

  encoded = enc.encrypt(args.text)

  print(encoded)
