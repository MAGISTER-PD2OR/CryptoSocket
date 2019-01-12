#include <Encrypter.h>

std::vector<Uint> Encrypter::encrypt(const std::string &msg)
{
  std::vector<Uint> enc;
  Uint k, p;
  for (auto &&l : msg)
  {
    k = static_cast<Uint>(1);
    p = static_cast<Uint>(l);
    for (Uint i = 0; i < this->e; ++i)
      k = (k * p) % this->n;
    enc.push_back(k);
  }

  return enc;
}
