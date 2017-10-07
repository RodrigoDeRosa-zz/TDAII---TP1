#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stringMatching import StringMatching
import pyhash

class RabinKarp(StringMatching):
    """Implementación del algoritmo de Rabin y Karp de exact matching."""
    def __init__(self):
        #Constructor de superclase
        super(StringMatching, self).__init__()

    def setHasher(self, hasher):
        self.hasher = hasher

    def __str__(self):
        return "Rabin-Karp Algorithm"

    #Override
    def find_match(self):
        """Encuentra todos los matchs de P en T.
            @return {List}: contiene las posiciones de inicio de todos
                            los matchs de P en T."""
        #definicion de variables para no usar 'self.' todo el tiempo
        P = self.pattern
        T = self.text
        H = self.hasher
        #largo de los strings
        t_len = len(T)
        p_len = len(P)
        #lista de matchs
        matchs = []

        #Valor de hash del patron
        hPatternValue = H(P)

        # ciclo principal del algoritmo
        for j in xrange(t_len):

            #se chequean los valores de hash del patron contra el
            #valor de hash de la palabra actual
            #solo si hay un match se verifica letra por letra
            hStringValue = H(T[j:p_len + j])

            #si hay match
            if (hPatternValue == hStringValue):

                #se verifica letra por letra
                for i in xrange(p_len):
                    # Si se va de rango, cortamos.
                    if (j + i == t_len): break
                    # Si son diferentes, avanzamos en T
                    if (P[i] != T[j + i]): break
                    # Si i llego a valer el largo de P, entonces hay un match en j
                    if (i == p_len - 1): matchs.append(j)

        #Devolvemos la lista
        return matchs
