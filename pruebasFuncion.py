# -*- coding: utf-8 -*-
'''
Created on Jan 29, 2017

@author: cinfante 13-10681
@author: aromero 13-11274
'''
import unittest
from funcion import BilleteraElectronica, RegistroRecarga, RegistroConsumo
from datetime import date

class Test(unittest.TestCase):
    BilleteraElectronica = None

    def setUp(self):
        BilleteraElectronica(1, "Oscar", "Masuno", 3540645, 5) 

    def tearDown(self):
        BilleteraElectronica = None
    
    # Prueba Malicia
    def testExcepcionCINegativo(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", -45, 5) 
        self.assertTrue("Debe introducir una cedula valida" in str(context.exception))
        
    # Prueba Malicia
    def testExcepcionPINegativo(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 3540645, -5) 
        self.assertTrue("El PIN no puede ser un numero negativo" in str(context.exception))
 
     # Prueba Borde
    def testRecargarBorde(self):
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        a.recargar(1, date(2017, 1, 28), 50)
        self.assertEqual(a.saldo(), 1, "Fallo en recarga borde")
        
    # Prueba Esquina
    def testRecargarMontoNegativo(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
            a.recargar(-1, date(2017, 1, 28), 50)
        self.assertTrue("El monto no puede ser negativo" in str(context.exception)) 
   
    # Prueba Borde
    def testConsumirBorde(self):
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        a.recargar(50, date(2017, 1, 28), 50)
        a.consumir(50, date(2017, 1, 28), 50, 5)
        self.assertEqual(a.saldo(), 0, "Fallo en consumir")
   
    # Prueba Esquina
    def testConsumirMontoNegativo(self):  
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
            a.consumir(-1, date(2017, 1, 28), 50, 5)
        self.assertTrue("El monto no puede ser negativo" in str(context.exception)) 
  
    # Prueba borde
    def testConsumirBorde(self):
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        a.recargar(50, date(2017, 1, 28), 50)
        a.consumir(50, date(2017, 1, 28), 50, 5)
        self.assertEqual(a.saldo(), 0, "Fallo en consumir")
    
    # Prueba Esquina
    def testConsumirMontoEsquina(self):  
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
            a.recargar(50, date(2017, 1, 28), 50)
            a.consumir(51, date(2017, 1, 28), 50, 5)
        self.assertTrue("No cuenta con el balance suficiente para cubrir el costo" in str(context.exception)) 
        
      # Prueba Esquina
    def testConsumirMontoEsquinaPIN(self):  
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 9999999)
            a.recargar(50, date(2017, 1, 28), 50)
            a.consumir(40, date(2017, 1, 28), 50, 9999998)
        self.assertTrue("El PIN introducido es distinto al del usuario" in str(context.exception)) 
    
    
    # Prueba Malicia
    def testConsumirMontoNegativoPINMalo(self):  
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
            a.recargar(50, date(2017, 1, 28), 50)
            a.consumir(-1, date(2017, 1, 28), 50, 45)
        self.assertTrue("El monto no puede ser negativo" in str(context.exception))
        
    # Prueba Malicia
    def testConsumirFaltaBalancePINMalo(self):  
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
            a.recargar(50, date(2017, 1, 28), 50)
            a.consumir(51, date(2017, 1, 28), 50, 45)
        self.assertTrue("No cuenta con el balance suficiente para cubrir el costo" in str(context.exception))
    
    
    # Prueba Malicia     
    def testUnicode(self):
        a = BilleteraElectronica(2, "Ñun", "Mión", 12309, 10)
 
     # Prueba Malicia            
    def testRecargaMontoCero(self):
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        a.recargar(0, date(2017, 1, 28), 50)
        self.assertEqual(a.saldo(), 0, "Fallo en recarga")

    # Prueba Malicia     
    def testConsumirMontoCero(self):  
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        a.consumir(0, date(2017, 1, 28), 50, 5)
        self.assertEqual(a.saldo(), 0, "Fallo en recarga")
        
    # Prueba Malicia     
    def testConsumirPINCero(self):  
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 0)
        a.consumir(0, date(2017, 1, 28), 50, 0)
        self.assertEqual(a.saldo(), 0, "Fallo en recarga")
        
    # Prueba Malicia     
    def testRecargarCeroConsumirCero(self):  
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 0)
        a.recargar(0, date(2017, 1, 28), 50)
        a.consumir(0, date(2017, 1, 28), 50, 0)
        self.assertEqual(a.saldo(), 0, "Fallo en recarga")

    # Prueba Interior
    def testSaldo(self):
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        self.assertEqual(a.saldo(), 0, "Fallo en saldo")
  
    # Prueba interior  
    def testRecargaIncrementa(self):
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        a.recargar(50, date(2017, 1, 28), 50)
        self.assertEqual(a.saldo(), 50, "Fallo en recarga")

    # Prueba Malicia     
    def testConsumirInsuficiente(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
            a.consumir(10, date(2017, 1, 28), 50, 5)
        self.assertTrue("No cuenta con el balance suficiente para cubrir el costo" in str(context.exception))
     
    # Prueba Malicia
    def testConsumirPINEquivocado(self):
        with self.assertRaises(Exception) as context:
            a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
            a.consumir(0, date(2017, 1, 28), 50, 40)
        self.assertTrue("El PIN introducido es distinto al del usuario" in str(context.exception))
    
    # Prueba Interior
    def testConsumirDecrementa(self):
        a = BilleteraElectronica(1, "Oscar", "Masuno", 45, 5)
        a.recargar(50, date(2017, 1, 28), 50)
        a.consumir(10, date(2017, 1, 28), 50, 5)
        self.assertEqual(a.saldo(), 50-10, "Fallo en consumir")
  
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()