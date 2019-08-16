| **Authors**  | **Project** | **Build Status**              | **Latest Version** | **License** |
|:------------:|:-----------:|:-----------------------------:|:------------------:|:-----------:|
| [**N. Curti**](https://github.com/Nico-Curti)  <br/> [**A. Fabbri**](https://github.com/allefabbri)  |  **CryptoSocket**   | **Linux/MacOS** : [![Travis](https://travis-ci.com/Nico-Curti/CryptoSocket.svg?branch=master)](https://travis-ci.com/Nico-Curti/CryptoSocket) <br/> **Windows** : [![appveyor](https://ci.appveyor.com/api/projects/status/3vu62g6xvbgmwl13?svg=true)](https://ci.appveyor.com/project/Nico-Curti/cryptosocket)  | ![version](https://img.shields.io/badge/PyPI-v1.0.0-orange.svg?style=plastic) | [![license](https://img.shields.io/badge/license-GPL-blue.svg?style=plastic)](https://github.com/Nico-Curti/CryptoSocket/blob/master/LICENSE)

[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Nico-Curti/CryptoSocket.svg?style=plastic)](https://github.com/Nico-Curti/CryptoSocket/pulls)
[![GitHub issues](https://img.shields.io/github/issues/Nico-Curti/CryptoSocket.svg?style=plastic)](https://github.com/Nico-Curti/CryptoSocket/issues)

[![GitHub stars](https://img.shields.io/github/stars/Nico-Curti/CryptoSocket.svg?label=Stars&style=social)](https://github.com/Nico-Curti/CryptoSocket/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/Nico-Curti/CryptoSocket.svg?label=Watch&style=social)](https://github.com/Nico-Curti/CryptoSocket/watchers)

<a href="https://github.com/UniboDIFABiophysics">
<div class="image">
<img src="https://cdn.rawgit.com/physycom/templates/697b327d/logo_unibo.png" width="90" height="90">
</div>
</a>

# CryptoSocket
## TCP/IP Client Server with RSA cryptography

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribution](#contribution)
5. [Authors](#authors)
6. [Citation](#citation)

## Prerequisites

**CryptoSocket** supports a pure Python implementation with some C++ features. To install the two components see the section below.

The **Python version** depends only by Numpy library and the Socket package.

The **C++ version** supports c++ standard 11 and it does not need extra dependencies.

## Installation

First of all clone the project:

```bash
git clone https://github.com/Nico-Curti/CryptoSocket
cd CryptoSocket
```

For the **Python installation** just type:

```bash
python setup.py install
```

or

```bash
python setup.py develop --user
```

for an installation in development mode.

For the **C++ installation** use the `build.sh` script if you are in Unix OS or the `build.ps1` for the Windows users.

For any troubles with the dependencies installation we recommend the use of [**ShUt**](https://github.com/Nico-Curti/shut) which includes a complete set of *no root*-user installation scripts.


## Usage

In the [example folder](https://github.com/Nico-Curti/CryptoSocket/tree/master/CryptoSocket/examples) you can find a pair of client-server scripts to test the connection. First of all open two local shell. Pay attention to start the server before the client!
In the first one run the command

```bash
python server.py -l localhost -r localhost -a 8080 -t 8087
```

You can see that this shell starts to wait messages from a putative client. Thus, in the second one we will send something using the client script with the command

```bash
python client.py -l localhost -r localhost -a 8087 -t 8080
```

You will see that the server shell has received the message send by the client and print the same message on its shell. You should see something like

```bash
starting up on localhost port 8080
waiting for a connection...
receiving...
Object ObjectToTransfer:
    Number of members: 3
    arr: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    msg: This is the message.
    num: 3.14

waiting for a connection...
```

Different kind of data are send by the client at the same time. You can manage the client script to your needs and try to send also more complex python object. Each message will be serialized using `pickle` so any Python class is allowed.

You can perform more sophisticated messages using the RSA cryptography inside the [Crypto](https://github.com/Nico-Curti/CryptoSocket/tree/master/CryptoSocket/Crypto) submodule just passing the keyfile in the previous command line. In this case the message will be encrypted by the client and decrypted by the server.

First of generate the couples of key-file needed by the RSA algorithm. The [generate_key.py](https://github.com/Nico-Curti/CryptoSocket/blob/master/CryptoSocket/examples/generate_key.py) file allows you to create a public and private key (in plain text) with the two keys.
The you can use the [encrypt.py](https://github.com/Nico-Curti/CryptoSocket/blob/master/CryptoSocket/examples/encrypt.py) script to encrypt a plain text as

```bash
python encrypt.py -k ./my_secret_private_key_filename.dat -f "this repo is amazing"
>>> [139, 345, 150, 312, 296, 361, 745, 701, 342, 296, 150, 312, 296, 487, 406, 487, 243, 150, 616, 372]
```

The with the [decrypt.py]() script we re-convert the encoded text to plain with the public key
```bash
python decrypt.py -k ./my_public_key_filename.dat -c 139 345 150 312 296 361 745 701 342 296 150 312 296 487 406 487 243 150 616 372
>>> this repo is amazing
```

The same script are callable also with the pure-C++ implementation of the RSA algorithm in the second [example](https://github.com/Nico-Curti/CryptoSocket/tree/master/cpp/example) directory.

## Contribution

Any contribution is more than welcome :heart:. Just fill an issue or a pull request and I will check ASAP!

## Authors

* **Nico Curti** [git](https://github.com/Nico-Curti), [unibo](https://www.unibo.it/sitoweb/nico.curti2)

* **Alessandro Fabbri** [git](https://github.com/allefabbri), [unibo](https://www.unibo.it/sitoweb/alessandro.fabbri27)

See also the list of [contributors](https://github.com/Nico-Curti/CryptoSocket/contributors) who participated in this project.


### Citation

If you have found `CryptoSocket` helpful in your research, please consider citing the

```tex
@misc{CryptoSocket,
  author = {Nico Curti, Alessandro Fabbri},
  title = {CryptoSocket - TCP/IP Client Server with RSA cryptography},
  year = {2019},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/Nico-Curti/CryptoSocket}},
}
```
