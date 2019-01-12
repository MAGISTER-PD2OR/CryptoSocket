| **Authors**  | **Project** | **Build Status**              | **Latest Version** | **License** |
|:------------:|:-----------:|:-----------------------------:|:------------------:|:-----------:|
|   N. Curti  <br/> A. Fabbri  |   CryptoSocket   | **Linux/MacOS** : [![Travis](https://travis-ci.com/Nico-Curti/CryptoSocket.svg?branch=master)](https://travis-ci.com/Nico-Curti/CryptoSocket) <br/> **Windows** : [![appveyor](https://ci.appveyor.com/api/projects/status/3vu62g6xvbgmwl13?svg=true)](https://ci.appveyor.com/project/Nico-Curti/cryptosocket)  | ![version](https://img.shields.io/badge/PyPI-v1.0.0-orange.svg?style=plastic) | [![license](https://img.shields.io/badge/license-GPL-blue.svg?style=plastic)](https://github.com/Nico-Curti/CryptoSocket/blob/master/LICENSE)

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

## Prerequisites

**CryptoSocket** supports a pure Python implementation with some C++ features. To install the two components see the section below.

The **Python version** depends only by Numpy library and the Socket package.

The **C++ version** supports c++ standard 11 and it does not need extra dependecies.

## Installation

First of all clone the project:

```
git clone https://github.com/Nico-Curti/CryptoSocket
cd CryptoSocket
```

For the **Python installation** just type:

```
python setup.py install
```

or

```
python setup.py develop --user
```

for the installation in development mode.

For the **C++ installation** use the `build.sh` script if you are in Unix OS or the `build.ps1` for the Windows OS.

For any troubles with the dependencies installation we recomend the use of [**ShUt**](https://github.com/Nico-Curti/shut) which includes a complete set of *no root* users installation scripts.


## Usage



## Contribution

Any contribution is more than welcome :heart:. Just fill an issue or a pull request and I will check ASAP!

## Authors

* **Nico Curti** [git](https://github.com/Nico-Curti), [unibo](https://www.unibo.it/sitoweb/nico.curti2)

* **Alessandro Fabbri** [git](https://github.com/allefabbri), [unibo](https://www.unibo.it/sitoweb/alessandro.fabbri27)

See also the list of [contributors](https://github.com/Nico-Curti/CryptoSocket/contributors) who partecipated in this project.
