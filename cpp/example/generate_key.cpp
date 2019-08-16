#define _GLIBCXX_USE_C99 1

#include <RSA.h>
#include <iostream>
#include <fstream>
#include <string>

static void show_usage ()
{
  std :: cerr << "Usage: RSA generate keys <option(s)>"                                            << std :: endl
              << "Option:"                                                                         << std :: endl
              << "   -h,--help       Show this help message"                                       << std :: endl
              << " keygen  <string> public_keyfile   <string> private_keyfile [<int> p] [<int> q]" << std :: endl
              << "      where   p   and   q   prime number"                                        << std :: endl
              << "      default   (p := 73 q := 11)"                                               << std :: endl
              << std :: endl;
}

int main (int argc, char ** argv)
{
  long unsigned int p;
  long unsigned int  q;

  std :: string pub;
  std :: string priv;

  if (
       argc == 1                          ||
       std :: string(argv[1]) == "--help" ||
       std :: string(argv[1]) == "-h"     ||
       argc == 2
      )
    {
      show_usage();
      return 0;
    }

  if ( argc < 2 )
  {
    std :: cerr << "Missing public_keyfile" << std :: endl;
    show_usage();
    return 1;
  }

  if ( argc < 3 )
  {
    std :: cerr << "Missing private_keyfile" << std :: endl;
    show_usage();
    return 1;
  }

  if ( argc == 3 )
  {
    p = 73;
    q = 11;
  }

  else if ( argc == 4 )
  {
    p = std :: stoul(argv[3]);
    q = 11;
  }

  else
  {
    p = std :: stoul(argv[3]);
    q = std :: stoul(argv[4]);
  }

  pub  = argv[1];
  priv = argv[2];

  std :: ifstream is (pub.c_str());

  if (is.is_open())
  {
    std :: cerr << "Public keyfile already exist. Cannot override" << std :: endl;
    std :: exit(1);
  }

  is.close();
  is.open(priv.c_str());

  if (is.is_open())
  {
    std :: cerr << "Private keyfile already exist. Cannot override" << std :: endl;
    std :: exit(1);
  }
  is.close();

  RSA rsa;

  try
  {
    rsa = RSA(p, q);
  }
  catch ( std :: exception & e)
  {
    std :: cerr << "EXC: " << e.what() << std :: endl;
    std :: exit(1);
  }

  std :: ofstream os (pub.c_str());
  os << rsa.n << " " << rsa.e << std :: endl;
  os.close();
  os.open(priv);
  os << rsa.n << " " << rsa.d << std :: endl;
  os.close();

  return 0;
}
