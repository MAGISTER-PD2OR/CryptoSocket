#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import warnings

from lib.Crypto.RSA import _rsa

__package__ = 'RSA object'

__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

class RSA (object):

  def __init__ (self, p, q):

    if not isinstance(p, int) or not isinstance(q, int):
      warnings.warn('P and Q are supposed to be integers.')

    p, q = int(p), int(q)

    self._obj = _rsa(p, q)

  @property
  def public_key(self):
    return self._obj.public_key


  @property
  def private_key(self):
    return self._obj.private_key
