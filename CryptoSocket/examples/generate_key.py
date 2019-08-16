#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from CryptoSocket.Crypto import RSA

__package__ = 'RSA key generator'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

def parse_args ():

  description = "RSA generate key"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-k', type=str, required=True,  dest='private', action='store', help='Private KeyFile')
  parser.add_argument('-u', type=str, required=True,  dest='public',  action='store', help='Public  KeyFile')
  parser.add_argument('-p', type=int, required=False, dest='p',       action='store', help='P value', default=73)
  parser.add_argument('-q', type=int, required=False, dest='q',       action='store', help='Q value', default=11)

  args = parser.parse_args()

  args.private += '.priv'
  args.public  += '.pub'

  return args


if __name__ == '__main__':

  args = parse_args()

  if os.path.exists(args.private):
    raise UserWarning('Private keyfile already exists. Cannot override')
    exit(0)

  if os.path.exists(args.public):
    raise UserWarning('Public keyfile already exists. Cannot override')
    exit(0)

  rsa = RSA(args.p, args.q)

  with open(args.public, 'w') as f:
    f.write("{} {}".format(rsa.n, rsa.e))

  with open(arg.sprivate, 'w') as f:
    f.write("{} {}".format(rsa.n, rsa.d))
