#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import csv
from decimal import *
import math


class Calcdb:
    
    def __init__(self, valor):
        self.valor = valor

    def a_lineal(self):
        
        getcontext().prec = 10
        self.valor = float(Decimal(10)**Decimal(self.valor/10))
        return(self.valor)
        
    def a_db(self):
        self.valor = math.log10(self.valor)
        return 10*(self.valor)
        
if __name__ == "__main__":
    getcontext().prec = 10
    if len(sys.argv) != 2:
        sys.exit("Input: python3 calcplus.py fichero")

    with open(sys.argv[1], newline='') as f:
        Fich = csv.reader(f)
        for Linea in Fich:
            Total = 0
            print(len(Linea))
            for Operando in Linea:
                Operar = Calcdb(float(Operando))
                Valor = Operar.a_lineal()

                Total= Total + Valor
            Operar = calcoo.Calculadora(float(Total),float(len(Linea)))

            Total = Operar.divide()
            Operar = Calcdb(float(Total))
            print(Operar.a_db())
