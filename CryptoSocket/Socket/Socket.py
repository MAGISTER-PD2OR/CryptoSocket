#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys    # stderr
import pickle # serialization of python object
import socket # socket object

__package__ = 'Socket wrap'
__author__  = ['Nico Curti',
               'Alessandro Fabbri'
               ]

__email__ = ['nico.curit2@unibo.it',
             'alessandro.fabbri27@unibo.it'
             ]

class Socket (object):

  def __init__ (self,
                Address_local, Port_local,
                Address_remote, Port_remote
               ):
    self.local  = (Address_local, Port_local)
    self.remote = (Address_remote, Port_remote)

    self.s_in  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def __enter__ (self):

    print('starting up on {} port {}'.format(*self.local), file=sys.stderr)

    self.s_in.bind(self.local)
    self.s_in.listen(1) # max number of connection

    return self

  def __exit__ (self, exc_type, exc_val, exc_tb):

    print('closing sockets', file=sys.stderr)

    self.s_in.close()
    self.s_out.close()

  def connect (self):

    print('connecting to {} port {}'.format(*self.remote), file=sys.stderr)

    try:
      self.s_out.connect(self.remote) # client

    except Exception as e:
      print("Unexpected error: {}".format(str(e)))
      exit(1)


  def accept (self):

    try:
      print('waiting for a connection...', file=sys.stderr)
      self.connection, _ = self.s_in.accept()

    except Exception as e:
      print("Unexpected error: {}".format(str(e)))
      exit(1)

  def send (self, Obj, enc=None):

    self.connect()

    print('sending...', file=sys.stderr)

    if enc is not None:
      self.s_out.send(pickle.dumps(list(enc.encrypt(pickle.dumps(Obj)))))

    else:
      self.s_out.send(pickle.dumps(Obj))

  def recv (self, dec=None):

    self.accept()

    buff = b''
    try:
      # Receive the data in small chunks and retransmit it
      print('receiving...', file=sys.stderr)

      while True:
        tmp = self.connection.recv(1024)

        if not tmp:
          break

        buff += tmp

    finally:
      # Clean up the connection
      self.connection.close()

    decoded = buff

    if dec is not None:
      decoded = dec.decrypt(pickle.loads(buff)).encode('latin-1')

    return pickle.loads(decoded)

