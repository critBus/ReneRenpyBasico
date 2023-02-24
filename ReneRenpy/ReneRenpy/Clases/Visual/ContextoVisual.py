from ReneRenpy.Clases.Visual.Fondos.FondoVideo import FondoVideo
class ContextoVisual:
    def __init__(self):
        self.fondoAnterior = None
        self.elAnteriorFueUnVideo=False

    def hayQuePonerNuevoFondo(self, escenario):
        fondoNuevo = escenario.getFondo()
        #print("fondoNuevo=",fondoNuevo)
        #print("fondoNuevo == self.fondoAnterior ",(fondoNuevo == self.fondoAnterior))
        if (fondoNuevo is not None) and not fondoNuevo == self.fondoAnterior:
            self.elAnteriorFueUnVideo =isinstance(self.fondoAnterior,FondoVideo)


            self.fondoAnterior = fondoNuevo
            return True

        return self.fondoAnterior is not None