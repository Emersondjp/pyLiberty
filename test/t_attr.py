#!/usr/bin/env python3

from AttributeClass import SimpleAttr
from AttributeClass import ComplexAttr

s = '  delay_model : lookup_table ; '
cs = ' line(1, 2, 3, 4); '

sa = SimpleAttr()
ca = ComplexAttr()

sa.extract( s )
print(sa)

ca.extract( cs )
print(ca)

sa.extract( ' time_unit : "1ns" ; ' )
print(sa)

