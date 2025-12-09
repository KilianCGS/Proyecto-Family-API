Voy a utilizar este archivo para tomar datos de que he hecho en este proyecto y cuales son sus objetivos

A priori entiendo que el objetivo del proyecto es crear una API REST usando Python y Flask.
La idea es gestionar los mimebros de una familia (Jackson) en memoria (no tengo base de datos real)
Lo que permiten los métodos es

Leer miembros:
GET /members (para ver todos)
GET /member/<id> (para ver 1)
POST /member  (para añadir un miembro)
DELETE /members/<id>  (para eliminar un membro específico)

Al hacerse en memoria si reinicio se pierde todo. Pero al menos practico estructura de datos, endpoints y JSON

En datastructure almacenamos y manipulamos la familia. Tenemos los datos de cada elemento del diccionario y eso es lo que utilizamos
para agregar los miembros

Los ID se generan de forma incremental (+1 cada vez que se añade uno) más interesante que usando el método de "random"

Tengo las funciones add_member (el POST), get_member (GET con el ID), delete_member(DELETE) y get_allmembers (GET en general)

Y por último los endpoints que ejecutan dichas funciones.
La idea es empezar a interiorizar el concepto de CRUD (Create, Read, Update, Delete) y como se separan los archivos

Datastructure.py -> datos y lógica
App.py -> endpoints

Si resumiéramos el proyecto a pseudocódigo básicamente es algo como

¿Que quiero almacenar? miembros de una familia
¿Que operaciones de CRUD hago? Create (los mimebros) read (obtenerlos) y DELETE (eliminarlos)


Pasar los test básicamente era ir rellenando las funciones y endpoints.
