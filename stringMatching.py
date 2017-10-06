#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StringMatching(object):
    """Superclase que funciona como interfaz de todos los algoritmos de
    Exact Matching a implementar."""
    def __init__(self):
        self.pattern = ""
        self.text = ""

    def set_pattern(self, P):
        """Actualiza el patrón por uno nuevo recibido.
            @param P {string}: Pattern.
            @return {void}
        """
        self.pattern = P

    def set_text(self, T):
        """Actualiza el texto por uno nuevo recibido
            @param T {string}: Text.
            @return {void}
        """
        self.text = T
