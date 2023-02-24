from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Dialogos.ElementoDeTransicion import ElementoDeTransicion
from ReneRenpy.Clases.Dialogos.CreadorDeElementoDeDialogo import CreadorDeElementoDeDialogo
from ReneRenpy.Clases.Interfaces.TieneAccionAlTerminar import TieneAccionAlTerminar
from ReneRenpy.Clases.Visual.Escenario import Escenario

class ElementoDeDialogo(Escenario, ElementoDeTransicion, CreadorDeElementoDeDialogo, TieneAccionAlTerminar):
    def __init__(self, personaje, texto, contextoDeDialogo):  #
        # self.nombre=nombre
        self.personaje = personaje
        if esString(texto):#isinstance(texto, str):
            anterior = texto
            texto = lambda ctx: anterior
        self.__metodoGetTexto = texto

        self.__contextoDeDialogo = contextoDeDialogo
        Escenario.__init__(self, contextoDeDialogo)
        ElementoDeTransicion.__init__(self, contextoDeDialogo)
        TieneAccionAlTerminar.__init__(self, contextoDeDialogo)
        # a = self.getTexto()
        # print(a)
        # TieneContexto.__init__(self, contextoDeDialogo)

    def getTexto(self):
        m = self.__metodoGetTexto
        b = m(self.__contextoDeDialogo)
        # print(b)
        return b
