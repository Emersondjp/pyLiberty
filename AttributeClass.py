# -*- coding: utf-8 -*-

##
# Attribute statements extracting support for the pyliberty package
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

    def indent_print( self, indent=0 ):
        '''
        Print attribute with indent.
        '''
        statement = "%s%s" % ( ' '*indent, str(self) )
        print( statement )

    def extract( self, line ):
        '''
        Extract name and value from string line.
        '''
        pat = re.compile(r'\s*(\S+)\s* : \s*(\S+)\s*;')
        m = pat.match( line )
        if m :
            self.name = m.group(1)
            v = m.group(2)
            if v[0] == v[-1] == '"' :
                v = v[1:-1]
            self.value = v
        else :
            if DEBUG :
                print( "Error matching simple attribute for string %s" % (line) )
            raise SimpleAttr_Extract_ERROR

    def build( self, n, v ):
        '''
        Build simple attribute from name / value.
        '''
        self.name = n
        self.vaule = v
        return 

    pass

class ComplexAttr( SimpleAttr ):
    '''
    Class for extract / form complex attributes of liberty.
    '''
    def __str__( self ):
        '''
        Get string of complex attribute.
        '''
        return "%s ( %s ) ;" % ( self.name, ', '.join(self.value) )

    #def indent_print( self, indent=0 ):
    #    '''
    #    Print complex attribute with indent.
    #    '''
    #    statement = "%s%s" % ( ' '*indent, str(self) )
    #    print( statement )

    def extract( self, line ):
        '''
        Extract name and value from string line for complex attributes.
        '''
        pat = re.compile(r'\s*(\S+)\s*\((.+)\)\s*;')
        m = pat.match( line )
        s = None
        if m :
            self.name = m.group(1)
            s = m.group(2)
            self.value = [ x.strip() for x in s.split( ',' ) ]
        else :
            if DEBUG :
                print( "Error matching complex attribute for string %s" % (line) )
            raise ComplexAttr_Extract_ERROR

    def build( self, n, *args ):
        '''
        Build complex attribute from name / value.
        '''
        self.name = n
        self.vaule = list(args)
        if len( args ) == 0 and DEBUG :
            print( "Warning: Complex Attribute build with no value." )
        return 

