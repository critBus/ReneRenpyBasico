from ReneRenpy.UtilesInit import *


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