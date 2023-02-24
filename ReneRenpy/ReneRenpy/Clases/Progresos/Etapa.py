from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Progresos.Ayuda import Ayuda

class Etapa:
    def __init__(self, nombre, condicionDeInicio=None, ayuda=None):
        self.nombre = nombre
        if condicionDeInicio is None:
            condicionDeInicio = lambda: True
        self.condicionDeInicio = condicionDeInicio
        if ayuda is None:
            ayuda = Ayuda()
        self.ayuda = ayuda
        self.completado = False

    def seCumpleCondicionDeInicio(self):
        return self.condicionDeInicio()
    @staticmethod
    def esEtapaAll(args, indiceInicial=0):
        for i, e in enumerate(args[indiceInicial:]):
            if not isinstance(e, Etapa):
                return False
        return True



