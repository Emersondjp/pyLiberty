# -*- coding: utf-8 -*-

##
# Support module for the pyliberty package
##


from base import BaseObject
import re

DEBUG = 1

class SimpleAttr_Extract_ERROR(Exception):
    pass

class SimpleAttr( BaseObject ):
    '''
    Class for extract / form simple attributes of liberty.
    '''
    # Attribute Name
    name = ''
    # Attribute Value
    value = ''

    def __init__( self ):
        pass

    def __str__( self ):
        '''
        Get string of simple attribute.
        '''
        return "%s : %s ;" % ( self.name, self.value )

    def extract( self, line ):
        '''
        Extract name and value from string line.
        '''
        pat = re.compile(r'\s*(\S+)\s* : \s*(.+)\s*;')
        m = pat.match( line )
        if m :
            self.name = m.group(1)
            self.value = m.group(2)
        else :
            if DEBUG :
                print( "Error matching simple attribute for string %s" % (line) )
            raise SimpleAttr_Extract_ERROR
    pass
