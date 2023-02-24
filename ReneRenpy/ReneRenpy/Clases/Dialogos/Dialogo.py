from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Dialogos.ElementoDeDialogo import ElementoDeDialogo
from ReneRenpy.Clases.Dialogos.ListaDeDialogo import ListaDeDialogo
from ReneRenpy.Clases.Dialogos.SecuenciaDeDialogo import SecuenciaDeDialogo
from ReneRenpy.Clases.Dialogos.ElementoDeListaDeDialogo import ElementoDeListaDeDialogo
from ReneRenpy.Clases.Dialogos.CreadorDeElementoDeDialogo import CreadorDeElementoDeDialogo
from ReneRenpy.Clases.Dialogos.CreadorDeElementoDeListaDeDialogo import CreadorDeElementoDeListaDeDialogo
from ReneRenpy.Clases.Dialogos.ContextoDeDialogo import ContextoDeDialogo
from ReneRenpy.Clases.Partida.Personaje import Personaje

from ReneRenpy.Clases.Visual.Escenario import Escenario
class Dialogo(Escenario):
    def __init__(self, contextoDePartida):
        self.contexto = ContextoDeDialogo(contextoDePartida)
        self.__metodoGetElementeInicial = None
        Escenario.__init__(self, self.contexto)

    def setMetodoGetElementoInicial(self, metodo):
        self.__metodoGetElementeInicial = metodo
        return self

    def getElementoInicial(self):
        return self.__metodoGetElementeInicial(self.contexto)

    def eld(self, texto, siguienteEscenario=None):
        elm = ElementoDeListaDeDialogo(texto=texto,
                                       contextoDeDialogo=self.contexto)  # ,etiquetaDeSalida=etiquetaDeSalida
        if siguienteEscenario is not None:
            elm.setSiguienteEscenario(siguienteEscenario)
        return elm

    def ed(self, *a):
        texto = None
        personaje = None
        siguienteEscenario = None
        leng = len(a)
        if leng == 1:
            if esString(a[0]):# isinstance(a[1], str):
                texto = a[0]
        elif leng == 2:
            if isinstance(a[0], Personaje) and esString(a[1]):#isinstance(a[1], str):
                personaje = a[0]
                texto = a[1]
            elif esString(a[0])  and isinstance(a[1], Escenario):#isinstance(a[0], str)
                texto = a[0]
                siguienteEscenario = a[1]

        elif leng == 3:
            if isinstance(a[0], Personaje) and esString(a[1]) and isinstance(a[2], Escenario):#isinstance(a[1], str)
                personaje = a[0]
                texto = a[1]
                siguienteEscenario = a[2]

        if isNoneAll(texto, personaje, siguienteEscenario):
            raise Exception("error de incializacion")

        if personaje is None:
            personaje = self.contexto.contextoDePartida.personajeNarrador
        elm = ElementoDeDialogo(personaje=personaje, texto=texto, contextoDeDialogo=self.contexto)
        elm.setSiguienteEscenario(siguienteEscenario)
        # a=elm.getTexto()
        return elm

    def set(self, *a):  # ListaInicial
        leng = len(a)
        a=list(a)
        for i,e in enumerate(a):
            if isinstance(e, SecuenciaDeDialogo):
                a[i]=e.build()




        if leng > 0 and isinstance(a[0],CreadorDeElementoDeListaDeDialogo):
            listaDeElementosDeDialogo = a
            listaDeElementos = []
            for celd in listaDeElementosDeDialogo:
                if isinstance(celd, CreadorDeElementoDeListaDeDialogo):
                    celd = celd.crearElementoDeListaDeDialogo()
                listaDeElementos.append(celd)
            lista = ListaDeDialogo(listaDeElementosDeDialogo=listaDeElementos, contextoDeDialogo=self.contexto)
            self.__metodoGetElementeInicial = lambda ctx: lista
            return lista
        # elif leng == 1 and isinstance(a[0], SecuenciaDeDialogo):
        #     elm = a[0].crearElementoDeDialogo()
        #     self.__metodoGetElementeInicial = lambda ctx: elm
        #     return elm


        return None

    def sc_ed(self, *args):
        return SecuenciaDeDialogo(self).ed(*args)

    def sc_eld(self, *args):
        return SecuenciaDeDialogo(self).eld(*args)

    def setFondo(self, textoNombreImagen):
        self.getElementoInicial().setFondo(textoNombreImagen)
        return self

    def getFondo(self):
        return self.getElementoInicial().getFondo()

    def setFondoMultiple(self, *args):
        return self.getElementoInicial().setFondoMultiple(*args)

    def setVideo(self, *args):
        return self.getElementoInicial().setVideo(*args)
