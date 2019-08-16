#include <Decrypter.h>
#include <iostream>
#include <fstream>

static void show_usage ()
{
  std :: cerr << "Usage: RSA decrypter <option(s)>"         << std :: endl
              << "Option:"                                  << std :: endl
              << "   -h,--help      Show this help message" << std :: endl
              << "   decrypter private_keyfilename -f file" << std :: endl
              << "                 OR"                      << std :: endl
              << "   decrypter private_keyfile text"        << std :: endl
              << std :: endl;
}


int main (int argc, char ** argv)
{
  long unsigned int n;
  long unsigned int d;
  long unsigned int c;

  std :: string filename;
  std :: string keyfile;
  std :: string row;

  std :: vector < long unsigned int > enc;

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
    std :: cerr << "Missing key_file" << std :: endl;
    show_usage();
    return 1;
  }

  keyfile = argv[1];

  if ( std :: string(argv[2]) == "-f")
  {
    if ( argc < 3 )
    {
      std :: cerr << "Missing filename" << std :: endl;
      show_usage();
      return 1;
    }
    else
      filename = argv[3];

    if ( argc >= 5 )
    {
      std :: cerr << "Too much arguments!" << std :: endl;
      show_usage();
      return 1;
    }
  }
  else
  {
    for (int i = 2; i < argc; ++i)
      enc.push_back(std :: stoul(argv[i]));
  }

  // read keyfile
  std :: ifstream key (keyfile);

  if ( !key.is_open() )
  {
    std :: cerr << "Missing keyfile" << std :: endl;
    std :: exit(2);
  }

  key >> n;
  key >> d;

  key.close();

  Decrypter dec(n, d);

  if ( std :: string(argv[2]) == "-f" )
  {
    std :: ifstream is(filename);

    if ( !is.is_open() )
    {
      std :: cerr << "File not found. Given: " << filename << std :: endl;
      std :: exit(1);
    }

    while (is >> c) enc.push_back(c);
    is.close();

    auto decoded = dec.decrypt(enc);

    std :: string outfile = filename.substr(0, filename.find("."));

    std :: ofstream out(outfile + ".dec");
    out << decoded;
    out.close();
  }
  else
  {
    auto decoded = dec.decrypt(enc);
    std :: cout << decoded << std :: endl;
  }

  return 0;
}
