'''
Created on Jan 29, 2017

@author: aromero
@author: cinfante
'''
import datetime

class BilleteraElectronica:
    _identificador = 0
    _nombres = ""
    _apellidos = ""
    _CI = 0
    _PIN = 0
    _balance = 0
    
    def __init__(self, identificador, nombres, apellidos, CI, PIN, balance):
        if PIN < 0 or PIN > 10000:
            raise Exception('El PIN debe ser de 4 numeros')
        if CI <= 0:
            raise Exception("Debe introducir una cédula válida")
        self._identificador = identificador
        self._nombres = nombres
        self._apellidos = apellidos
        self._CI = CI
        self._PIN = PIN
        self._balance = balance
    
    def getPIN(self):
        return self._PIN
    
    def saldo(self):
        return self._balance
    
    def recargar(self, monto, fecha, idEstablecimiento):
        if monto < 0:
            raise Exception('El monto no puede ser negativo')
        self._balance += monto
        return RegistroRecarga(monto, fecha, idEstablecimiento, self)
    

class RegistroRecarga:
    if monto < 0:
        raise Exception('El monto no puede ser negativo')
    _monto = 0
    _fecha = datetime.date.today()
    _idEstablecimiento = 0
    _billetera = BilleteraElectronica()

    def __init__(self, monto, fecha, idEstablecimiento, billetera):
        self._monto = monto
        self._fecha = fecha
        self._idEstablecimiento = idEstablecimiento
        self._billetera = billetera
        
class RegistroConsumo:
    if monto < 0:
        raise Exception('El monto no puede ser negativo')
    _monto = 0
    _fecha = datetime.date.today()
    _idEstablecimiento = 0
    _billetera = BilleteraElectronica()
    
    def __init__(self, monto, fecha, idEstablecimiento, billetera):
        self._monto = monto
        self._fecha = fecha
        self._idEstablecimiento = idEstablecimiento
        self._billetera = billetera


