from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Partida.Personaje import Personaje

class ContextoDePartida:
    def __init__(self, arbolDeProgresos=None, calendario=None, personajePrincipal=None, personajeNarrador=None):
        self.inicializar(arbolDeProgresos, calendario, personajePrincipal, personajeNarrador)

    def inicializar(self, arbolDeProgresos, calendario, personajePrincipal, personajeNarrador):
        self.arbolDeProgresos = arbolDeProgresos
        self.storage = {}
        if (personajePrincipal is not None) and not isinstance(personajePrincipal, Personaje):
            personajePrincipal = Personaje(personajePrincipal)
        if (personajeNarrador is not None) and not isinstance(personajeNarrador, Personaje):
            personajeNarrador = Personaje(personajeNarrador)
        self.personajePrincipal = personajePrincipal
        self.personajeNarrador = personajeNarrador
        self.calendario = calendario
