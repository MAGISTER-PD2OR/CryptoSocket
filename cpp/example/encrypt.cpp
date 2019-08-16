#include <Encrypter.h>
#include <iostream>
#include <fstream>

static void show_usage ()
{
  std :: cerr << "Usage: RSA encrypter <option(s)>"         << std :: endl
              << "Option:"                                  << std :: endl
              << "   -h,--help      Show this help message" << std :: endl
              << "   encrypter public_keyfilename -f file"  << std :: endl
              << "                 OR"                      << std :: endl
              << "   encrypter public_keyfilename text"     << std :: endl
              << std :: endl;
}

int main (int argc, char ** argv)
{
  long unsigned int n;
  long unsigned int e;

  std :: string text;
  std :: string filename;
  std :: string keyfile;
  std :: string row;

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

  if( argc < 2 )
  {
    std :: cerr << "Missing key_file" << std :: endl;
    show_usage();
    return 1;
  }

  keyfile = argv[1];

  if ( std :: string(argv[2]) == "-f" )
  {
    if( argc < 3 )
    {
      std :: cerr << "Missing filename" << std :: endl;
      show_usage();
      return 1;
    }
    else
      filename = argv[3];

    if( argc >= 5 )
    {
      std :: cerr << "Too much arguments!" << std :: endl;
      show_usage();
      return 1;
    }
  }
  else
  {
    text = argv[2];
    if ( argc >= 4 )
    {
      std :: cerr << "Too much arguments!" << std :: endl;
      show_usage();
      return 1;
    }
  }

  // read keyfile
  std :: ifstream key(keyfile);

  if ( !key.is_open() )
  {
    std :: cerr << "Missing keyfile" << std :: endl;
    std :: exit(2);
  }

  key >> n;
  key >> e;

  key.close();

  Encrypter enc(n, e);

  if ( std :: string(argv[2]) == "-f" )
  {
    std :: ifstream is(filename);

    if ( !is.is_open() )
    {
      std :: cerr << "File not found. Given: " << filename << std :: endl;
      std :: exit(1);
    }

    std :: string outfile = filename.substr(0, filename.find("."));

    std :: ofstream out(outfile + ".rsa");

    while ( std :: getline(is, text) )
    {
      auto encoded = enc.encrypt(text + "\n");
      for (const auto & e : encoded)
        out << e << " ";
    }
    is.close();
    out.close();
  }
  else
  {
    auto encoded = enc.encrypt(text);
    for (const auto & l : encoded)
      std :: cout << l << " ";
    std :: cout << std :: endl;
  }

  return 0;
}
