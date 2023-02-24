from ReneRenpy.Utiles.Utiles import *

from ReneRenpy.Clases.Visual.Escenario import Escenario
class ListaDeDialogo(Escenario):
    def __init__(self, listaDeElementosDeDialogo, contextoDeDialogo):
        self.listaDeElementosDeDialogo = listaDeElementosDeDialogo
        Escenario.__init__(self, contextoDeDialogo)
