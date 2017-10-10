#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from stringMatching import StringMatching

class Colussi(StringMatching):
    """Implementación del algoritmo de Ukkonen [linear-time suffix tree]."""
    def __init__(self):
        super(StringMatching, self).__init__()

    def __str__(self):
        return "Ukkonen"

    def find_match(self):
        """Encuentra todos los matchs de P en T.
            @return {List}: contiene las posiciones de inicio de todos
                            los matchs de P en T.
        """
        #Definicion de variables para hacer mas corta la llamada
        P = self.pattern
        T = self.text
