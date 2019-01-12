#!/usr/bin/env python

import numpy as np

class Decrypter:

  def __init__(self, n, d):
    self.n = n
    self.d = d

  def decrypt(self, enc):
    msg = ''
    for l in enc:
      k = 1
      c = np.uint(l)
      for _ in range(self.d):
        k = np.uint((k * c) % self.n)
      msg += chr(k)
    return msg

  def __repr__(self):
    fmt_str = "Encoder object\n"
    members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
    for m in members:
      fmt_str += '    %s: %s\n'%(m, eval('self.%s'%m))
    return fmt_str
