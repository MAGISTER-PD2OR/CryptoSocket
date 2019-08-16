#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import warnings

from lib.Crypto.Decrypter import _decrypter

__package__ = 'Decrypter object'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

class Decrypter (_decrypter):

  def __init__ (self, n, d):

    if not isinstance(n, int) or not isinstance(d, int):
      warnings.warn('N and D are supposed to be integers.')

    n, d = int(n), int(d)

    self._dec = _decrypter(n, d)


  def decrypt (self, enc):

    # convert enc to vector of long ints
    if isinstance(enc, str):
      enc = list(map(ord, enc))

    elif isinstance(enc, list):
      enc = list(map(int, enc))

    else:
      raise ValueError('Unrecognized input type. Please give a string or a list')

    enc = np.asarray(enc, dtype=np.int64)
    enc = np.ascontiguousarray(enc)

    return self._dec.decrypt(enc)

  def __repr__(self):

    fmt_str = "Encoder object\n"
    members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
    for m in members:
      fmt_str += '    {}: {}\n'.format(m, eval('self.{}'.format(m)))
    return fmt_str
