#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

from lib.Crypto.Encrypter import _encrypter

__package__ = 'Encrypter object'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

class Encrypter (_encrypter):

  def __init__ (self, n, e):

    if not isinstance(n, int) or not isinstance(e, int):
      warnings.warn('N and E are supposed to be integers.')

    n, e = int(n), int(e)

    self._enc = _encrypter(n, e)


  def encrypt (self, dec):
    '''
    Encrypt text message

    Parameters
    ----------
      dec : string
        Plain text to encrypt with RSA algorithm

    Returns
    -------
      encrypt : list of integers
        Encrypted version of the text
    '''

    if not isinstance(dec, str):
      raise ValueError('Unrecognized input type. Please give a string')

    return self._enc.encrypt(dec)

  def __repr__(self):

    fmt_str = "Encoder object\n"
    members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
    for m in members:
      fmt_str += '    {}: {}\n'.format(m, eval('self.{}'.format(m)))
    return fmt_str
