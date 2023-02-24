from ReneRenpy.UtilesInit import *

elementoActual=None
def accionAlApretarUnaOpcionEnElementoDeDialogo(elementoOpcion):
    global elementoActual
    elementoOpcion.realizarAccionAlterminar()
    elementoActual = elementoOpcion.getSiguienteEscenario()


def accionAlApretarEnBitMap(disparador):
    global elementoActual
    disparador.realizarAccionAlterminar()
    elementoActual = disparador.getEscenario()


av = ArbolDeProgresos()
ctxv = ContextoVisual()
ctx = ContextoDePartida()
d = "asd"
_ubicacionAnterior = None


def ub():
    global _ubicacionAnterior
    _ubicacionAnterior = Ubicacion(ctx)
    return _ubicacionAnterior


def ut():
    global _ubicacionAnterior
    return UbicacionTemporal(ctx, _ubicacionAnterior)


def dlg():
    global d
    d = Dialogo(ctx)
    return d

#from ReneRenpy.InitDefault import *
class Character:
    def __init__(self,nombre):
        self.name=nombre

p_p = Personaje(Character("Principal"))
p_n = Personaje(Character("Narrador"))
p_m = Personaje(Character("Mo"))


def getElementoInicial():
    global av, ctxv, ctx, d

    class Juego:
        def __init__(self):
            self.comproItemUno = False

    jg = Juego()

    mo = av.newProgreso("mo")
    et_mo_0_1 = mo.addEtapa("primera vista")
    et_mo_0_2 = mo.addEtapa("muestra interes 1")
    et_mo_0_3 = mo.addEtapa("muestra interes 2")
    et_mo_1 = mo.addEtapa("se aprovechan posibilidades 1")
    mo.addEtapa("muestra interes 3")
    mo.addEtapa("se aprovechan posibilidades 2")

    calendario = CalendarioLineal()
    ctx.inicializar(av, calendario, p_p, p_n)

    # variables

    def comproAUno(ctx):
        return jg.comproItemUno

    def comprarAUno(ctx):
        jg.comproItemUno = True

    # -------

    # u_casa = ub()
    #
    # dlg_casa_manana_con_mo = dlg()
    # dlg_casa_manana_con_mo.set(
    #     d.sc_eld("Saludar").ed(p_p, "Como estas").ed(p_m, "bien", u_casa).end(et_mo_0_1).avan(1)
    #     , d.eld("Ignorar", u_casa)
    #     ,
    #     d.sc_eld("prio pe")._if(et_mo_0_2).ed(p_p, "te ves bien").ed(p_m, "gracias jeje", u_casa).end(et_mo_0_2).avan(1)
    #     )
    # dlg_casa_manana_con_mo.setFondo("bg club")
    #
    # dlg_casa_manana_con_si=dlg()
    # dlg_casa_manana_con_si.set(
    #     d.sc_eld("hablarle")
    #         .ed(p_p,"Hola").setVideo("video_web.webm")
    #         .ed(p_p,"wao",u_casa)
    # )
    # dlg_casa_manana_con_si.setFondo("bg lecturehall")
    # #dlg_casa_manana_con_si = dlg()
    # #parte_dlg_1=dlg_casa_manana_con_si.ed("Hola", u_casa).setVideo("video_web.webm")
    #
    # # dlg_casa_manana_con_si.set(
    # #     dlg_casa_manana_con_si.eld("hablar", parte_dlg_1))
    #
    # ut_casa_manana = ut().setFondo("imagemap b", "imagemap b hover")
    # ut_casa_manana.addMap(dlg_casa_manana_con_mo, 88, 102, 170, 170)
    # ut_casa_manana.addMap(dlg_casa_manana_con_si, 455, 289, 170, 170)
    # ut_casa_manana.addBotonImagen("item uno", "item uno hover", 600, 100, 100, 100)._ifnot(comproAUno).accion(
    #     comprarAUno)
    #
    # u_casa.add(ut_casa_manana)
    # #print("fondo actual=", parte_dlg_1.getFondo().direccionVideo)
    # ut_mapa_dia = ut().setFondo("imagemap a", "imagemap a hover")
    # ut_mapa_dia.addMap(u_casa, 88, 102, 170, 170)
    # u_mapa = ub().add(ut_mapa_dia)

    u_casa = ub()

    dlg_casa_manana_con_mo = dlg()
    dlg_casa_manana_con_mo.set(d.sc_eld("Saludar").ed(p_p, "Como estas").ed(p_m, "bien", u_casa).end(et_mo_0_1).avan(1)
                               , d.eld("Ignorar", u_casa)
                               , d.sc_eld("prio pe")._if(et_mo_0_2).ed(p_p, "te ves bien").ed(p_m, "gracias jeje",
                                                                                              u_casa).end(
            et_mo_0_2).avan(1)
                               )
    dlg_casa_manana_con_mo.setFondo("bg club")

    dlg_casa_manana_con_si = dlg()
    dlg_casa_manana_con_si.set(
        d.sc_eld("hablarle").ed(p_p, "Hola").setVideo("video1").ed(p_p, "wao", u_casa).setFondo("bg lecturehall")
        , d.sc_eld("otro").ed(p_p, "Hola").setFondoMultiple("bg club", "sylvie blue giggle")
    )
    dlg_casa_manana_con_si.setFondo("bg lecturehall")
    # dlg_casa_manana_con_si=dlg()
    # dlg_casa_manana_con_si.set(dlg_casa_manana_con_si.eld("hablar",dlg_casa_manana_con_si.ed("Hola",u_casa).setVideo("video1"))).setFondo("bg lecturehall")#vid['videouno']

    ut_casa_manana = ut().setFondo("imagemap b", "imagemap b hover")
    ut_casa_manana.addMap(dlg_casa_manana_con_mo, 88, 102, 170, 170)
    ut_casa_manana.addMap(dlg_casa_manana_con_si, 455, 289, 170, 170)
    ut_casa_manana.addBotonImagen("item uno", "item uno hover", 600, 100, 100, 100)._ifnot(comproAUno).accion(
        comprarAUno)

    u_casa.add(ut_casa_manana)

    ut_mapa_dia = ut().setFondo("imagemap a", "imagemap a hover")
    ut_mapa_dia.addMap(u_casa, 88, 102, 170, 170)
    u_mapa = ub().add(ut_mapa_dia)


    return u_mapa
elementoActual=getElementoInicial()

def apretoMapa(indice=0):
    global ubicacionActual
    ubicacionActual=elementoActual.getUbicacionActual()

    dis=ubicacionActual.listaDeDisparadores[indice]

    accionAlApretarEnBitMap(dis)
apretoMapa()
apretoMapa(1)
elementoActual=elementoActual.getElementoInicial()
def apretoListaDialogo1(listaDeDialogo):
    lista = listaDeDialogo.listaDeElementosDeDialogo
    accionAlApretarUnaOpcionEnElementoDeDialogo(lista[0])
apretoListaDialogo1(elementoActual)

if isinstance(elementoActual,ElementoDeDialogo):
    texto=elementoActual.getTexto()
    print("texto=",texto)
    hayQueCambiarElFondo=ctxv.hayQuePonerNuevoFondo(elementoActual)
    print("hay que cambiar el fondo=",hayQueCambiarElFondo)
    if hayQueCambiarElFondo:
        fondo = ctxv.fondoAnterior
        esVideo=isinstance(fondo,FondoVideo)
        print("esVideo=",esVideo)

# def calcularDescuento(cantidadOriginal):
#     if cantidadOriginal>=500:
#         cantidadDescuento=cantidadOriginal-(cantidadOriginal*0.3)
#         return cantidadDescuento
#     elif cantidadOriginal<500 and cantidadOriginal>=200:
#         cantidadDescuento=cantidadOriginal-(cantidadOriginal*0.2)
#         return cantidadDescuento
#     elif cantidadOriginal<200 and cantidadOriginal>=100:
#         cantidadDescuento=cantidadOriginal-(cantidadOriginal*0.1)
#         return cantidadDescuento
#     return cantidadOriginal
#
#
# respuesta=calcularDescuento(float(input("escriba la cantidad original\n")))
# print(respuesta)