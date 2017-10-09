PSIZE = 4200 #Maximo tamanioo del patron
ASIZE = 256 #Tamanio del alfabeto

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from stringMatching import StringMatching

class ZT(StringMatching):
    def __init__(self):
        #Constructor de superclase
        super(StringMatching, self).__init__()

    def __str__(self):
        return "Zhu-Takaoka"

    def suffixes( self, lenP ):

        patron = self.pattern

        #Inicializacion del vector a devolver.
        suf = [0 for x in xrange(0,PSIZE)]

        suf[lenP - 1] = lenP
        g = lenP - 1

        for x in xrange(0, lenP-1):#queremos que vaya hasta lenP-2
            #En realidad queremos hacer el for al revez entonces:
            i = lenP - 2 - x
            if( (i > g) and (suf[i + lenP - 1 -f] < i - g) ):
                suf[i] = suf[i + lenP - 1 - f]
            else:
                if(i < g):
                    g = i
                f = i
                while(g >=0 and patron[g] == patron[g+lenP-1-f]):
                    g-=1
                    suf[i] = f-g
        return suf

    def preBmGs( self, lenP ):
        patron = self.pattern
        #Inicializacion del vector
        bmgs = [0 for x in xrange(0,PSIZE)]
        suf = self.suffixes(lenP)

        for i in xrange(0, lenP):
            bmgs[i] = lenP
        for i in xrange(0,lenP):
            #Este for en realidad va al revez
            x = lenP - 1 - x
            if(suf[x] == x+1):
                for y in xrange(1,lenP - 1 - x):
                    if(bmgs[y] == lenP):
                        bmgs[y] = m-1-x
        for x in xrange(0,lenP-1):
            bmgs[lenP - 1 - suf[x]] = lenP - 1 - x
        return bmgs


    def preZtBc(self, lenP ):
        patron = self.pattern
        ztbc = [0] * ASIZE
        for i in xrange(ASIZE):
            ztbc[i] = [0] * ASIZE
        for x in xrange(0, ASIZE):
            for y in xrange(0, ASIZE):
                ztbc[x][y] = lenP
        for x in xrange(0,ASIZE):
            ztbc[x][ord(patron[0])] = lenP -1
        for x in xrange(1, lenP - 1):
            ztbc[ord(patron[x-1])][ord(patron[x])] = lenP - 1 - x
        return ztbc

    def find_match( self ):
        patron = self.pattern
        texto = self.text
        lenP = len(patron)
        lenT = len(texto)

        if(lenP <= 0 or lenT<= 0):
            return []
        BMGS = self.preBmGs( lenP)
        ZTBC = self.preZtBc( lenP)
        #Concatenamos el patron 2 veces al final del texto
        texto += patron
        texto += patron
        matches = []
        #Pasamos a buscar el patron en el texto
        contador = 0
        j = 0
        while(j <= lenT - lenP):
            i = lenP - 1
            while( i >= 0 and patron[i] == texto[i+j]):
                i-=1
            if(i<0):
                contador+=1
                matches.append(j)
                j += BMGS[0]
            else:
                j += max(BMGS[i], ZTBC[ord(texto[j+lenP - 2])][ord(texto[j+lenP-1])] )
        return matches
