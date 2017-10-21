#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:

    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplica(self):
        return self.valor1 * self.valor2

    def divide(self):
        try:
            return self.valor1 / self.valor2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
