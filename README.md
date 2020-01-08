# Tienda de Olivanders

Proyecto desarrollado por José María Samos y Sebastià Adrover

## Descripción del proyecto

Es el desarrollo software de una tienda online. Está totalmente basada en la programación orientada a objetos. Este solamente es la capa lógica del proyecto completo.

El programa asigna tres propiedades a cada producto: nombre, tiempo de vida y calidad; y define el comportamiento que debe tener cada propiedad.

El programa tambien genera un html con todos los items disponibles y sus propedades que es usado para desarrollar la aplicación web de la tienda.

## Estructura del proyecto

El proyecto consta de cuatro objetos principales:

1. Item.py: asigna las aspectos básicos de todos los items (name, sell_in, quality).
2. Normal_item.py: asigna el comportamiento genérico de los aspectos de los items.
3. Gilded_rose.py: genera una lista de items con el valor de sus aspectos.
4. Updatable.py: es una interfaz que obliga a todos los items que deben actualizar su quality.

Por otra parte tenemos quatro objetos cuyos comportamientos son distintos a los que asigna el objeto Normal_item:

5. Aged_brie.py: aunque sell_in sea cero, su quality sigue aumentando.
6. Sulfuras.py: no disminuye ni su sell_in, ni su quality.
7. Conjured.py: su quality disminuye el doble de rápido que un Normal_item.
8. Backstage_pass.py: su quality va aumentando exponencialmente a medida que sell_in se acerca a cero.

Luego tenemos dos ficheros que conforman el desarrollo web:

9. logica.py: genera el html y añade los items a la instancia de Gilded_rose.
10. app.py: es la aplicación que ejecuta Flask.

