#!/usr/bin/env python

import pickle # serialization of python object

class ObjectToTransfer():

  def __init__(self):
    pass

  def __init__(self, msg, number, array):
    self.msg = msg
    self.num = number
    self.arr = array

  def serialize(self):
    return pickle.dumps(self)

  def __len__(self):
    return len([attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")])

  def __repr__(self):
    fmt_str = 'Object ' + self.__class__.__name__ + ':\n'
    fmt_str += '    Number of members: {}\n'.format(self.__len__())
    members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
    for m in members:
      fmt_str += '    %s: %s\n'%(m, eval('self.%s'%m))
    return fmt_str
