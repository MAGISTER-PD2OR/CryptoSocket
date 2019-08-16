#!/usr/bin/env python
# -*- coding: utf-8 -*-

__package__ = 'version'
__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

from CryptoSocket.build import read_version

VERSION = read_version('./CMakeLists.txt')

__version__ = '.'.join(map(str, VERSION))
