# -*- coding: utf-8 -*-
'''
Created on Jan 29, 2017

@author: cinfante
@author: aromero
'''
import unittest
from funcion import BilleteraElectronica, RegistroRecarga, RegistroConsumo
from datetime import date

class Test(unittest.TestCase):
    BilleteraElectronica = None

    def setUp(self):
        BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5) 

    def tearDown(self):
        BilleteraElectronica = None
        
    def testExcepcionCINegativo(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscaruja", "Mezortega", -45, 5) 
        self.assertTrue("Debe introducir una cedula valida" in str(context.exception))

    def testExcepcionPINegativo(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, -5) 
        self.assertTrue("El PIN no puede ser un numero negativo" in str(context.exception))
        
    def testRecargaMontoNegativo(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
            a.recargar(-1, date(2017, 1, 28), 50)
        self.assertTrue("El monto no puede ser negativo" in str(context.exception))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()