from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Interfaces.TieneContexto import TieneContexto
from ReneRenpy.Clases.Visual.Fondos.ImagenDeFondo import ImagenDeFondo
class FondoMultiple(TieneContexto):
    def __init__(self,ctx,*nombreDeImagenes):
        TieneContexto.__init__(self,ctx)
        self.listaDeImagenes=[]
        for img in nombreDeImagenes:
            self.listaDeImagenes.append(ImagenDeFondo(img,ctx))
    def add(self,nombreImagen):
        img=ImagenDeFondo(nombreImagen, self.contexto)
        self.listaDeImagenes.append(img)
        return img




