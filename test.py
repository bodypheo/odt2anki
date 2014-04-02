#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from lpod.document import odf_get_document
from lpod.table import *
import re

#Se podría acceder al documento en red con urlopen("url_address")
filename = "Vocabulario.odt"
separator = "\t"

doc = odf_get_document(filename) #Create instance
body = doc.get_body() #Get body structure
tabla = body.get_table()
size =  tabla.get_size() #Returns (columns, rows)
filas = re.search ('.*?,\s+(\d+)\)', str(size)) # To extract the rows

file = open('vocabulario.txt', 'w+')
for r in range(2, int(filas.group(1))+1):
    kanji = tabla.get_cell( 'A' + str(r)).get_value()
    kana = tabla.get_cell( 'B' + str(r)).get_value()
    significado = tabla.get_cell( 'C' + str(r)).get_value()
    cadena = ('%s<br>(%s) %s  %s %s vocabulario') % (kana, kanji, separator,
                                                 significado, separator) + "\n"
    file.write(cadena.encode("UTF-8"))
file.close
