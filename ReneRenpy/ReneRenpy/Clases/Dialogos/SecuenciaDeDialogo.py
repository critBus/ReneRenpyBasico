from ReneRenpy.Utiles.Utiles import *

from ReneRenpy.Clases.Dialogos.CreadorDeElementoDeDialogo import CreadorDeElementoDeDialogo
from ReneRenpy.Clases.Dialogos.CreadorDeElementoDeListaDeDialogo import CreadorDeElementoDeListaDeDialogo

from ReneRenpy.Clases.Visual.Escenario import Escenario
from ReneRenpy.Clases.Visual.CreadorDeEscenario import CreadorDeEscenario


class SecuenciaDeDialogo(CreadorDeEscenario, CreadorDeElementoDeDialogo, CreadorDeElementoDeListaDeDialogo):
    def __init__(self, dialogo):
        self.ubicacionFinal = None
        self.dialogo = dialogo
        self.listaDeCreadores = []  # Escenario -> ElementoDeDlg
        self.creadorElementoDeListaDeDialogo = None  # Escenario -> ElementoDeListaDeDialogo

    def ed(self, *args):
        leng = len(args)
        if leng > 1 and isinstance(args[-1], Escenario):
            self.ubicacionFinal = args[-1]

        def crearElemento(escenarioSiguiente):
            elm = self.dialogo.ed(*args)

            self.__ponerTrasicion(elm, escenarioSiguiente)
            # a = elm.getTexto()
            return elm

        self.listaDeCreadores.append(crearElemento)
        return self

    def eld(self, texto):  # *args
        def crearElemento(escenarioSiguiente):
            elm = self.dialogo.eld(texto)
            self.__ponerTrasicion(elm, escenarioSiguiente)
            return elm

        self.creadorElementoDeListaDeDialogo = crearElemento
        return self

    def __ponerTrasicion(self, elm, siguiente):
        if siguiente is not None:
            elm.setSiguienteEscenario(siguiente)

    def end(self, *args):
        leng = len(self.listaDeCreadores)
        if (self.creadorElementoDeListaDeDialogo is not None) and leng == 0:
            anterior = self.creadorElementoDeListaDeDialogo
            self.creadorElementoDeListaDeDialogo = lambda es: anterior(es).end(*args)
        else:
            anterior = self.listaDeCreadores[-1]

            def nuevo(es):
                elm = anterior(es)
                elm.end(*args)
                return elm

            self.listaDeCreadores[-1] = nuevo
            # self.listaDeCreadores[-1] = lambda es: anterior(es).end(*args)

        return self

    def __setNewMetodo(self, metodoNuevo):  # ob,args->None, *args
        def getMetodoAPoner(anterior):
            return lambda es: metodoNuevo(anterior(es))#, args

        leng = len(self.listaDeCreadores)
        if (self.creadorElementoDeListaDeDialogo is not None) and leng == 0:
            anterior = self.creadorElementoDeListaDeDialogo
            # self.creadorElementoDeListaDeDialogo = lambda es: anterior(es)._if(*args)
            self.creadorElementoDeListaDeDialogo = getMetodoAPoner(anterior)
        else:
            anterior = self.listaDeCreadores[-1]
            # self.listaDeCreadores[-1] = lambda es: anterior(es)._if(*args)
            self.listaDeCreadores[-1] = getMetodoAPoner(anterior)

        return self

    def _if(self, *args):
        # leng = len(self.listaDeCreadores)
        # if (self.creadorElementoDeListaDeDialogo is not None) and leng == 0:
        #     anterior = self.creadorElementoDeListaDeDialogo
        #     self.creadorElementoDeListaDeDialogo = lambda es: anterior(es)._if(*args)
        # else:
        #     anterior = self.listaDeCreadores[-1]
        #     self.listaDeCreadores[-1] = lambda es: anterior(es)._if(*args)
        self.__setNewMetodo(lambda ob: ob._if(*args))#, *args , argumentos
        return self

    def _ifnot(self, *args):
        # leng = len(self.listaDeCreadores)
        # if (self.creadorElementoDeListaDeDialogo is not None) and leng == 0:
        #     anterior = self.creadorElementoDeListaDeDialogo
        #     self.creadorElementoDeListaDeDialogo = lambda es: anterior(es)._ifnot(*args)
        # else:
        #     anterior = self.listaDeCreadores[-1]
        #     self.listaDeCreadores[-1] = lambda es: anterior(es)._ifnot(*args)
        self.__setNewMetodo(lambda ob: ob._ifnot(*args)) #, *args , argumentos
        return self

    # avan
    def avan(self, *args):
        # leng = len(self.listaDeCreadores)
        # if (self.creadorElementoDeListaDeDialogo is not None) and leng == 0:
        #     anterior = self.creadorElementoDeListaDeDialogo
        #     self.creadorElementoDeListaDeDialogo = lambda es: anterior(es).avan(*args)
        # else:
        #     anterior = self.listaDeCreadores[-1]
        #     self.listaDeCreadores[-1] = lambda es: anterior(es).avan(*args)
        self.__setNewMetodo(lambda ob: ob.avan(*args)) #, *args , argumentos
        return self

    def accion(self, *args):
        # leng = len(self.listaDeCreadores)
        # if (self.creadorElementoDeListaDeDialogo is not None) and leng == 0:
        #     anterior = self.creadorElementoDeListaDeDialogo
        #     self.creadorElementoDeListaDeDialogo = lambda es: anterior(es).accion(*args)
        # else:
        #     anterior = self.listaDeCreadores[-1]
        #     self.listaDeCreadores[-1] = lambda es: anterior(es).accion(*args)
        self.__setNewMetodo(lambda ob: ob.accion(*args))#, *args , argumentos
        return self

    def setFondo(self, *args):
        self.__setNewMetodo(lambda ob: ob.setFondo(*args))#, *args , argumentos
        return self

    def setVideo(self, *args):
        def metodoSetVideo(ob):#,*argumentos
            # print("paso por set viedo secuencia")
            # print("ob=",ob)
            # print("tipo=",type(ob))
            # for i,a in enumerate(args):
            #     print("i=",i," ",a)

            ob.setVideo(*args)
            return ob
        #self.__setNewMetodo(lambda ob, argumentos: ob.setVideo(*args), *args)
        self.__setNewMetodo(metodoSetVideo)#, *args
        return self
    def setFondoMultiple(self, *args):
        self.__setNewMetodo(lambda ob: ob.setFondoMultiple(*args))#, argumentos , *args
        return self
    def esElementoDeListaDeDialogo(self):
        return self.creadorElementoDeListaDeDialogo is not None
    def build(self):
        if self.esElementoDeListaDeDialogo():
            return self.crearElementoDeListaDeDialogo()
        return self.crearElementoDeDialogo()
    def crearEscenario(self):
        return self.crearElementoDeDialogo()

    def crearElementoDeListaDeDialogo(self):
        return self.creadorElementoDeListaDeDialogo(self.crearElementoDeDialogo())

    def crearElementoDeDialogo(self):
        # le = []
        anterior = self.ubicacionFinal
        if anterior is None:
            raise Exception("Hay una secuencia de dialogo sin ubicacion final")
        for cr in reversed(self.listaDeCreadores):
            actual = cr(anterior)
            # if isinstance(actual, TieneAccionAlTerminar):
            #     texto = actual.getTexto()
            #     print(texto)

            # le.append(actual)
            anterior = actual
        # self.__ponerTrasicion(anterior, self.ubicacionFinal)
        return anterior

