#!/usr/bin/env python

import numpy as np

class Encrypter:

  def __init__(self, n, e):
    self.n = n
    self.e = e

  def encrypt(self, msg):
    enc = np.empty(shape=(len(msg),), dtype=np.uint)
    for i, l in enumerate(msg):
      k = 1

      try:
        p = np.uint(ord(l))
      except:
        p = np.uint(l)

      for _ in range(self.e):
        k = np.uint((k * p) % self.n)
      enc[i] = k
    return enc

  def __repr__(self):
    fmt_str = "Encrypter object\n"
    members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
    for m in members:
      fmt_str += '    %s: %s\n'%(m, eval('self.%s'%m))
    return fmt_str
