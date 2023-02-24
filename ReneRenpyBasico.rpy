init python:
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


screen menuDialogo(listaDeDialogo):#listaDeParesOpcionDialogo
    modal True
    vbox:
        xalign 0.5 ypos 100
        $lista=listaDeDialogo.listaDeElementosDeDialogo
        
        for el in lista:
            $esVisible=el.esVisible()
            if esVisible:
                textbutton el.texto:
                    background "#440000d9"
                    text_color "#c04040"
                    text_hover_color "#ff0000"
                    action [Function(accionAlApretarUnaOpcionEnElementoDeDialogo,el) ,Jump("labelRedireccion") ]#el.etiquetaDeSalida


screen imagemap_ubicacion(ubicacion):


    imagemap:
        idle "[fondo_normal]"
        hover "[fondo_hover]"

        #$ubicacionActual=ubicacion.getUbicacionActual()
        for dis in ubicacionActual.listaDeDisparadores:
            $esVisible=dis.esVisible()
            if esVisible:
                $esBotonImagen=isinstance(dis,DisparadorBotonImagen)
                if esBotonImagen:
                    $cor=dis.coordenadas
                    $coordenadaX=cor.X
                    $coordenadaY=cor.Y
                    $ancho=cor.ancho
                    $alto=cor.alto
                    $fondo_boton=dis.getFondo()
                    $fondo_boton_normal=fondo_boton.normal
                    $fondo_boton_hover=fondo_boton.hover
                    imagebutton:
                        xpos coordenadaX ypos coordenadaY
                        idle fondo_boton_normal#"[fondo_boton_normal]"#Frame(fondo_boton_normal,(ancho,alto))#
                        hover fondo_boton_hover #"[fondo_boton_hover]"#Frame(fondo_boton_hover,(ancho,alto))#
                        xsize ancho
                        ysize alto
                        action  [Function(accionAlApretarEnBitMap,dis) ,Jump("labelRedireccion") ]
                else:
                    $esDisparadorBitMap=isinstance(dis,DisparadorBitMap)
                    if esDisparadorBitMap:
                        for cor in dis.listaDeCoordenadas:
                            $coordenadaX=cor.X
                            $coordenadaY=cor.Y
                            $ancho=cor.ancho
                            $alto=cor.alto
                            hotspot (coordenadaX, coordenadaY, ancho, alto) action  [Function(accionAlApretarEnBitMap,dis) ,Jump("labelRedireccion") ]





label label_fin:
    return

label labelRedireccion:
    
    $esUbicacion=isinstance(elementoActual,Ubicacion)
    if not esUbicacion:
        # python:
        #     if isinstance(elementoActual,ElementoDeDialogo):
        #         texto=elementoActual.getTexto()
        #         print("texto=",texto)
        #         hayQueCambiarElFondo=ctxv.hayQuePonerNuevoFondo(elementoActual)
        #         print("hay que cambiar el fondo=",hayQueCambiarElFondo)
        #         if hayQueCambiarElFondo:
        #             fondo=ctxv.fondoAnterior
        #             esVideo=isinstance(fondo,FondoVideo)
        #             print("esVideo=",esVideo)
                
                
                
                
        $hayQueCambiarElFondo=ctxv.hayQuePonerNuevoFondo(elementoActual)
        if hayQueCambiarElFondo:
            $fondo=ctxv.fondoAnterior
            $esVideo=isinstance(fondo,FondoVideo)
            if esVideo:
                python:
                    print("fue video")
                    loop=0
                    if fondo.ininterrumpido:
                        loop=-1
                        #print("loop=",loop)
                    direccion_video=fondo.direccionVideo
                    elAnteriorFueUnVideo=ctxv.elAnteriorFueUnVideo
                #image video1=Movie(play=direccion_video)
                #show video1
                #$renpy.movie_cutscene(direccion_video,loop)
                if elAnteriorFueUnVideo:
                    $ renpy.scene()
                $ renpy.show(direccion_video)
             
            else:
                $esFondoMultiple=isinstance(fondo,FondoMultiple)
                if esFondoMultiple:
                    $renpy.scene()
                    $lista=fondo.listaDeImagenes
                    $i=0
                    $leng=len(lista)
                    while i<leng:
                        $imagenEnLista=lista[i]
                        $esVisible=imagenEnLista.esVisible()
                        if esVisible:
                            $ imagenActual=imagenEnLista.nombreImagen
                            $ renpy.show(imagenActual)
                        $i=i+1
                        #block of code to run
                    # for imagenEnLista in lista:
                    #     $esVisible=imagenEnLista.esVisible()
                    #     if esVisible:
                    #         $ imagenActual=imagenEnLista.nombreImagen
                    #         $ renpy.show(imagenActual)
                else:
                    $ renpy.scene()
                    $ renpy.show(fondo)

    $esUnaListaDeDalogo=isinstance(elementoActual,ListaDeDialogo)
    if esUnaListaDeDalogo:
        jump labelListaDeDalogo
    $esUnElementoDeDialogo=isinstance(elementoActual,ElementoDeDialogo)
    if esUnElementoDeDialogo:
        jump labelElementoDeDialogo
    $esUnDialogo=isinstance(elementoActual,Dialogo)
    if esUnDialogo:
        jump labelDialogo
    if esUbicacion:
        jump labelUbicacion


    jump ubicacion_casa

label labelListaDeDalogo:
    call screen menuDialogo(elementoActual)
label labelDialogo:
    $elementoActual=elementoActual.getElementoInicial()
    jump labelRedireccion
label labelElementoDeDialogo:
    $texto=elementoActual.getTexto()
    if texto is not None:
        $c=elementoActual.personaje.character#elementoDeDialogo
        c"[texto]"
    python:
        if isinstance(elementoActual,TieneAccionAlTerminar):
            elementoActual.realizarAccionAlterminar()
    $elementoActual=elementoActual.getSiguienteEscenario()
    jump labelRedireccion

label labelUbicacion:
    $ubicacionActual=elementoActual.getUbicacionActual()
    $fondo=ubicacionActual.getFondo()
    $fondo_normal=fondo.normal
    $fondo_hover=fondo.hover
    call screen imagemap_ubicacion(elementoActual)

#init python:
    

