'''
Created on Jan 29, 2017

@author: aromero
@author: cinfante
'''

class BilleteraElectronica:
    _identificador = 0
    _nombres = ""
    _apellidos = ""
    _CI = 0
    _PIN = 0
    
    def __init__(self, identificador, nombres, apellidos, CI, PIN):
        if PIN < 0 or pin > 10000:
            raise Exception('El PIN debe ser de 4 numeros MMG')
        if CI <= 0:
            raise Exception("Debe introducir una cédula válida")
        self._identificador = identificador
        self._nombres = nombres
        self._apellidos = apellidos
        self._CI = CI
        self._PIN = PIN
    
    def getPIN(self):
        return self._PIN