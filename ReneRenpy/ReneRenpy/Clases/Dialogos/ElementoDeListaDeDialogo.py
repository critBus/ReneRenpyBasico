from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Dialogos.ElementoDeTransicion import ElementoDeTransicion
from ReneRenpy.Clases.Dialogos.CreadorDeElementoDeListaDeDialogo import CreadorDeElementoDeListaDeDialogo
from ReneRenpy.Clases.Interfaces.TieneAccionAlTerminar import TieneAccionAlTerminar
from ReneRenpy.Clases.Interfaces.TieneCondicionDeVisibilidad import TieneCondicionDeVisibilidad

class ElementoDeListaDeDialogo(ElementoDeTransicion, CreadorDeElementoDeListaDeDialogo, TieneAccionAlTerminar,
                               TieneCondicionDeVisibilidad):
    def __init__(self, texto, contextoDeDialogo):  # siguienteEscenario
        self.texto = texto
        # self.etiquetaDeSalida=etiquetaDeSalida

        self.accionAlTerminar = None
        self.contexto = contextoDeDialogo
        ElementoDeTransicion.__init__(self, contextoDeDialogo)
        TieneCondicionDeVisibilidad.__init__(self, contextoDeDialogo)
        TieneAccionAlTerminar.__init__(self, contextoDeDialogo)

    def getTexto(self):
        return self.texto
