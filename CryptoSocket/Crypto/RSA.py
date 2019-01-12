#!/usr/bin/env python

import numpy as np

class RSA:

  def __init__(self, p, q):
    self.p = p
    self.q = q

    if not self.is_prime(self.p):
      raise UserWarning('p is not prime. Please insert a prime number')
      exit(1)

    if not self.is_prime(self.q):
      raise UserWarning('p is not prime. Please insert a prime number')
      exit(1)

    self.n   = self.p * self.q
    self.phi = (p - 1) * (q - 1)

    self.compute_public_key()
    self.compute_private_key()

  def is_prime(self, n):
    j = np.uint(np.sqrt(n))
    for i in range(2, j + 1):
      if n % i == 0:
        return False
    return True

  def compute_public_key(self):
    i = 2
    while True:
      if self.phi % i == 0:
        i += 1
        continue
      if self.is_prime(i):
        self.e = i
        break
      i += 1

  def compute_private_key(self):
    k = 1
    while True:
      k += self.phi
      if k % self.e == 0:
        self.d = k / self.e
        break

  def __repr__(self):
    fmt_str = "RSA params\n"
    members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
    for m in members:
      fmt_str += '    %s: %s\n'%(m, eval('self.%s'%m))
    return fmt_str
