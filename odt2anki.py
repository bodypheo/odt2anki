#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from lpod.document import odf_get_document
from lpod.table import *
import re

#Cadena de archivos para crear la lista de ficheros
filenames = 'Vocabulario Adjetivos lugares Verbos'.split()
separator = "\t"
for filename in filenames:
    #Create instance
    doc = odf_get_document(filename+'.odt') 
    #Get body structure
    body = doc.get_body() 
    #get number of tables
    tablas = body.get_tables()

    file = open(filename+'.txt', 'w+') #w+ truncate file if exists
    for t in tablas:
        size =  t.get_size() #Returns (columns, rows)
        filas = re.search ('.*?,\s+(\d+)\)', str(size)) # To extract the rows
        print filas.group(1)
        nombre_tabla = t.get_name()
        for r in range(2, int(filas.group(1))+1):
            kanji = t.get_cell( 'A' + str(r)).get_value()
            kana = t.get_cell( 'B' + str(r)).get_value()
            significado = t.get_cell( 'C' + str(r)).get_value()
            cadena = ('%s<br>(%s) %s  %s %s %s') % (kana, kanji, separator,
                                                     significado, separator,
                                                nombre_tabla) + "\n"
            file.write(cadena.encode("UTF-8"))
    file.close
