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
    
    # Malicia    
    def testUnicode(self):
        a = BilleteraElectronica(2, "Ñun", "Mión", 12309, 10)
        
    def testRecargaMontoNegativo(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
            a.recargar(-1, date(2017, 1, 28), 50)
        self.assertTrue("El monto no puede ser negativo" in str(context.exception))
    
    def testConsumirMontoNegativo(self):  
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
            a.consumir(-1, date(2017, 1, 28), 50, 5)
        self.assertTrue("El monto no puede ser negativo" in str(context.exception))
    
    def testSaldo(self):
        a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
        self.assertEqual(a.saldo(), 0, "Fallo en saldo")
    
    def testRecargaIncrementa(self):
        a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
        a.recargar(50, date(2017, 1, 28), 50)
        self.assertEqual(a.saldo(), 50, "Fallo en recarga")
        
    def testConsumirInsuficiente(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
            a.consumir(10, date(2017, 1, 28), 50, 5)
        self.assertTrue("No cuenta con el balance suficiente para cubrir el costo" in str(context.exception))
        
    def testConsumirPINEquivocado(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
            a.consumir(0, date(2017, 1, 28), 50, 4)
        self.assertTrue("El PIN introducido es distinto al del usuario" in str(context.exception))
        
    def testConsumirDecrementa(self):
        a = BilleteraElectronica(1, "Oscaruja", "Mezortega", 45, 5)
        a.recargar(50, date(2017, 1, 28), 50)
        a.consumir(10, date(2017, 1, 28), 50, 5)
        self.assertEqual(a.saldo(), 50-10, "Fallo en consumir")
  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()