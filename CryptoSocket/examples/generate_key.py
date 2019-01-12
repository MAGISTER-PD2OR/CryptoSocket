#!/usr/bin/env python

from CryptoSocket.Crypto import RSA
import argparse
import sys
import os


if __name__ == '__main__':


  description = "RSA generate key"
  parser = argparse.ArgumentParser(description = description)
  parser.add_argument('-k', required=True,  dest='private', action='store', help='Private KeyFile')
  parser.add_argument('-u', required=True,  dest='public',  action='store', help='Public  KeyFile')
  parser.add_argument('-p', required=False, dest='p',       action='store', help='P value', default=73)
  parser.add_argument('-q', required=False, dest='q',       action='store', help='Q value', default=11)

  if len(sys.argv) <= 2:
    parser.print_help()
    sys.exit(1)
  else:
    args = parser.parse_args()

  private = args.private
  public  = args.public
  p       = int(args.p)
  q       = int(args.q)

  private += '.priv'
  public  += '.pub'

  if os.path.exists(private):
    raise UserWarning('Private keyfile already exists. Cannot override')
    exit(0)

  if os.path.exists(public):
    raise UserWarning('Public keyfile already exists. Cannot override')
    exit(0)

  rsa = RSA(p, q)

  with open(public, 'w') as f:
    f.write("%d %d"%(rsa.n, rsa.e))
  with open(private, 'w') as f:
    f.write("%d %d"%(rsa.n, rsa.d))
