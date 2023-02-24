

class FondoVisual:  # (TieneContexto)
    def __init__(self, *imagenesDeEstado):
        # TieneContexto.__init__(self, ctx)
        self.normal = imagenesDeEstado[0]
        self.hover = None
        if len(imagenesDeEstado) > 1:
            self.hover = imagenesDeEstado[1]
