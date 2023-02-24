from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Visual.Escenario import Escenario
from ReneRenpy.Clases.Ubicaciones.Disparadores.CoordenadasCuadradas import CoordenadasCuadradas
from ReneRenpy.Clases.Ubicaciones.Disparadores.DisparadorBotonImagen import DisparadorBotonImagen
from ReneRenpy.Clases.Ubicaciones.Disparadores.DisparadorBitMap import DisparadorBitMap
from ReneRenpy.Clases.Dialogos.Dialogo import Dialogo
from ReneRenpy.Clases.Progresos.Etapa import Etapa
class UbicacionTemporal(Escenario):
    def __init__(self, ctx, ubicacion):
        Escenario.__init__(self, ctx)
        self.listaDeDisparadores = []
        self.ubicacion = ubicacion

    def addBotonImagen(self, *args):
        boton = None
        leng = len(args)
        if leng == 7 and isinstance(args[0], Escenario) and esString(args[1]) \
                and esString(args[2]) and esIntAll(args, 3):#isinstance(args[1], str)
            boton = DisparadorBotonImagen(escenario=args[0]
                                          , coordenadas=CoordenadasCuadradas(X=args[3]
                                                                             , Y=args[4]
                                                                             , ancho=args[5]
                                                                             , alto=args[6])
                                          , ctx=self.contexto).setFondo(args[1], args[2])
        elif leng == 6 and esString(args[0]) \
                and esString(args[1]) and esIntAll(args, 2):
            boton = DisparadorBotonImagen(escenario=self.ubicacion
                                          , coordenadas=CoordenadasCuadradas(X=args[2]
                                                                             , Y=args[3]
                                                                             , ancho=args[4]
                                                                             , alto=args[5])
                                          , ctx=self.contexto).setFondo(args[0], args[1])
        if boton is None:
            raise Exception("el image boton no se incializo")
        self.listaDeDisparadores.append(boton)
        return boton

    def addMap(self, *args):
        disparador = None
        leng = len(args)
        if leng == 2:
            if isinstance(args[0], Dialogo) and isinstance(args[1], CoordenadasCuadradas):  # BitMap
                disparador = DisparadorBitMap(args[0], [args[1]], self.contexto)
                self.listaDeDisparadores.append(disparador)
        elif leng > 2:
            # if isinstance(args[0],Dialogo):
            if isinstance(args[0], Escenario) and isinstance(args[1], CoordenadasCuadradas):  # BitMap
                disparador = DisparadorBitMap(args[0], [args[1]], self.contexto)
                if esFuncion(args[2]):
                    disparador.setCondicionDeVisbilidad(args[2])
                elif Etapa.esEtapaAll(args, 2):
                    disparador._if(*args[2:])



            elif esIntAll(args, 1):
                coordenadas = None
                if leng == 4:
                    coordenadas = CoordenadasCuadradas(X=args[1], Y=args[2], ancho=args[3])  # BitMap
                elif leng == 5:
                    coordenadas = CoordenadasCuadradas(X=args[1], Y=args[2], ancho=args[3], alto=args[4])  # BitMap
                disparador = DisparadorBitMap(args[0], [coordenadas], self.contexto)
            self.listaDeDisparadores.append(disparador)
        return disparador

