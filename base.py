# -*- coding: utf-8 -*-

##
# Support module for the pyliberty package
##

# 2018-03-08 Add BaseObject.

from __future__ import print_function

DEBUG = 0

import sys

class BaseObject(object):
    '''
    Parent of almost all other classes in the package. Defines a common "dump" method
    for debugging.
    '''

    _repr_these = []

    def dump(self, f=None, header=None, footer=None, indent=0):
        '''
        @param f open file object, to which the dump is written
        @param header text to write before the dump
        @param footer text to write after the dump
        @param indent number of leading spaces (for recursive calls)
        '''
        if f is None:
            f = sys.stderr
        if hasattr(self, "__slots__"):
            alist = []
            for attr in self.__slots__:
                alist.append((attr, getattr(self, attr)))
        else:
            alist = self.__dict__.items()
        alist = sorted(alist)
        pad = " " * indent
        if header is not None: print(header, file=f)
        list_type = type([])
        dict_type = type({})
        for attr, value in alist:
            if getattr(value, 'dump', None) :
                value.dump(f,
                    header="%s%s (%s object):" % (pad, attr, value.__class__.__name__),
                    indent=indent+4)
            elif attr not in self._repr_these and (
                isinstance(value, list_type) or isinstance(value, dict_type)
                ):
                print("%s%s: %s, len = %d" % (pad, attr, type(value), len(value)), file=f)
            else:
                fprintf(f, "%s%s: %r\n", pad, attr, value)
        if footer is not None: print(footer, file=f)

