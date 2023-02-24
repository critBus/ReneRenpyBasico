from ReneRenpy.Utiles.Utiles import *

from ReneRenpy.Clases.Interfaces.TieneContexto import TieneContexto
from ReneRenpy.Clases.Visual.Fondos.FondoVideo import FondoVideo
from ReneRenpy.Clases.Visual.Fondos.FondoVisual import FondoVisual
from ReneRenpy.Clases.Visual.Fondos.FondoMultiple import FondoMultiple
class TieneFondo(TieneContexto):
    def __init__(self, ctx):
        self.__getFondo = None
        TieneContexto.__init__(self, ctx)

    def setFondo(self, *imagenes):
        # if self.__getFondo is not None:
        #     fondo=self.__getFondo(self.contexto)
        #     m="Trato de volver a poner el fondo a "+str(self)+"\ntipo"+str(type(self))
        #     raise Exception(m)
        if len(imagenes) > 1:
            self.__getFondo = lambda ctx: FondoVisual(*imagenes)
        else:
            if esString(imagenes[0]):#isinstance(imagenes[0], str)
                self.__getFondo = lambda ctx: imagenes[0]
        return self

    def getFondo(self):
        if self.__getFondo is None:
            return None
        return self.__getFondo(self.contexto)

    def setVideo(self, *args):
        #print("seteo")
        direccionDeVideo = args[0]
        ininterrumpido = True
        if len(args) > 1 and isinstance(args[1], bool):
            ininterrumpido = args[1]
        def nuevo(ctx):
            #print("puso el fondo")
            return FondoVideo(direccionDeVideo, ininterrumpido)
        #self.__getFondo = lambda ctx: FondoVideo(direccionDeVideo, ininterrumpido)
        self.__getFondo =nuevo
        # fondoAhora=self.__getFondo(self.contexto)
        # print("fondoAhora=",fondoAhora)
        # print("tipo=",type(fondoAhora))
        return self
    def setFondoMultiple(self,*args):
        if len(args)==1 and isinstance(args[0],FondoMultiple):
            self.__getFondo = lambda ctx: args[0]
        elif len(args)>0:
            self.__getFondo = lambda ctx: FondoMultiple(ctx,*args)

        return self

    def getVideoDeFondo(self):
        if self.__getFondo is None:
            return None
        videoFondo = self.__getFondo(self.contexto)
        return videoFondo
        # if videoFondo is None:
        #     return None
        # return videoFondo.direccionVideo
