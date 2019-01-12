#include <Decrypter.h>

std::string Decrypter::decrypt(const std::vector<Uint> &enc)
{
  Uint k, c;
  std::string msg = "";

  for (auto &&l : enc)
  {
    k = static_cast<Uint>(1);
    c = static_cast<Uint>(l);
    for (Uint j = 0; j < this->d; ++j)
      k = (k * c) % this->n;
    msg += static_cast<char>(k);
  }

  return msg;
}