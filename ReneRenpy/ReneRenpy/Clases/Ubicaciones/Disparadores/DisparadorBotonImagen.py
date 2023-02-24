from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Ubicaciones.Disparadores.DisparadorDeEscenario import DisparadorDeEscenario
from ReneRenpy.Clases.Visual.Fondos.TieneFondo import TieneFondo
class DisparadorBotonImagen(DisparadorDeEscenario, TieneFondo):
    def __init__(self, escenario, coordenadas, ctx):
        TieneFondo.__init__(self,ctx)
        DisparadorDeEscenario.__init__(self, escenario, ctx)
        self.coordenadas = coordenadas
