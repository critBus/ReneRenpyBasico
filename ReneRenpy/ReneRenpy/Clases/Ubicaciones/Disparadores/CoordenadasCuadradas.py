

class CoordenadasCuadradas:  # BitMap
    def __init__(self, X, Y, ancho, alto=None):
        if alto is None:
            alto = ancho
        self.X = X
        self.Y = Y
        self.ancho = ancho
        self.alto = alto
