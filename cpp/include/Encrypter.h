#ifndef ENC_H
#define ENC_H
#include <vector>
#include <string>

using Uint = long unsigned int;

class Encrypter
{
  Uint n, e;

public:

  Encrypter(){};
  Encrypter(const Uint &n, const Uint &e) : n(n), e(e) {};
  ~Encrypter() = default;

  // members

  std::vector<Uint> encrypt(const std::string &enc);
};

#endif // ENC_H
