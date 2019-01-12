#ifndef RSA_H
#define RSA_H
#include <iostream>
#include <string>
#include <cmath>

using Uint = long unsigned int;

class RSA
{
  Uint p, q;

  bool is_prime(const Uint &n);

public:

  Uint n, phi, e, d;

  RSA() {};
  RSA(const Uint &p, const Uint &q);

  ~RSA() = default;

  // members

  void compute_public_key(const Uint &phi);
  void compute_private_key(const Uint &phi, const Uint &e);
};

#endif // RSA_H
