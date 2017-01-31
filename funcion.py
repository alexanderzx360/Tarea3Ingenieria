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
    
    def __init__(self, identificador=0, nombres="", apellidos="", CI=0, PIN=0, balance=0):
        if PIN < 0:
            raise Exception("El PIN no puede ser un numero negativo")
        if CI < 0:
            raise Exception("Debe introducir una cedula valida")
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
    
    def consumir(self, monto, fecha, idEstablecimiento):
        if monto < 0:
            raise Exception('El monto no puede ser negativo')
        self._balance -= monto
        return RegistroConsumo(monto, fecha, idEstablecimiento, self)
    

class RegistroRecarga:
    
    _monto = 0
    _fecha = datetime.date.today()
    _idEstablecimiento = 0
    _billetera = BilleteraElectronica()

    def __init__(self, monto, fecha, idEstablecimiento, billetera):
        if monto < 0:
            raise Exception('El monto no puede ser negativo')
        self._monto = monto
        self._fecha = fecha
        self._idEstablecimiento = idEstablecimiento
        self._billetera = billetera
        
class RegistroConsumo:
    _monto = 0
    _fecha = datetime.date.today()
    _idEstablecimiento = 0
    _billetera = BilleteraElectronica()
    
    def __init__(self, monto, fecha, idEstablecimiento, billetera):
        if monto < 0:
            raise Exception('El monto no puede ser negativo')
        self._monto = monto
        self._fecha = fecha
        self._idEstablecimiento = idEstablecimiento
        self._billetera = billetera


