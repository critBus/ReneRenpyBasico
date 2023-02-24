from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Interfaces.TieneCondicionDeVisibilidad import TieneCondicionDeVisibilidad
class ImagenDeFondo(TieneCondicionDeVisibilidad):
    def __init__(self,nombreImagen,ctx):
        TieneCondicionDeVisibilidad.__init__(self,ctx)
        self.nombreImagen=nombreImagen