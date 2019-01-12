#ifndef DEC_H
#define DEC_H
#include <vector>
#include <string>

using Uint = long unsigned int;

class Decrypter
{
  Uint n, d;

public:

  Decrypter(){};
  Decrypter(const Uint &n, const Uint &d) : n(n), d(d) {};
  ~Decrypter() = default;

  // members

  std::string decrypt(const std::vector<Uint> &enc);
};

#endif // DEC_H
