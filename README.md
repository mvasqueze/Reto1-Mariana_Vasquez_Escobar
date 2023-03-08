

<h3 align="center">Reto 1 de Programación</h3>

<div align="center">

Mariana Vásquez Escobar - Tópicos especiales en Telemática

</div>

---

## 📝 Table of Contents

- [Descripción del proyecto](#about)
- [Alcance del proyecto](#getting_started)
- [Estructura del proyecto](#deployment)
- [Arquitectura de la solución planteada](#usage)
- [Resultados logrados](#built_using)
- [Descripción técnica de la solución implementada](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Guía de uso](#authors)
- [Acknowledgments](#acknowledgement)

## Descripción del proyecto <a name = "about"></a>

El presente proyecyo busca afianzar y demostrar las habilidades adquiridas a través del laboratorio 1 en la implementación de la arquitectura de microservicios a través de gRPC.

## Alcance del proyecto <a name = "getting_started"></a>

El objetivo del proyecto es implementar una arquitectura de tres microservicios usando dos lenguajes programación diferentes, así como un cliente, estando los cuatro servidores desplegados en máquinas de AWS.

Se busca retratar el funcionamiento de una tienda online, implementando servicios de inventario (inventory), carrito de compras (shoppingCart) y envíos (shipment).


## Estructura del proyecto <a name = "tests"></a>

El repositorio se encuentra inicialmente dividido en la carpeta servers (que guarda los microservicios), el código de javascript del cliente (client.js) y el presente README.md; En la carpeta servers se encuentran a su vez tres carpetas, cada una correspondiente a un microservicio y conservando la misma estructura. Se dará el ejemplo con la carpeta inventory:

Inventory>
    - Archivos generados para el uso de grpc (inventory_pb2_grpc.py,inventory_pb2.py, inventory_pb2.pyi).
    - Código de python correspondiente al microservicio (inventory.py).
    - Código .proto para enlazar con grpc (inventory.proto).
    - Un archivo que funciona como persistencia de datos (inventory.proto).



## Arquitectura de la solución planteada <a name="usage"></a>

Se logró implementar una arquitectura orientada a microservicios, usando Postman para simular el cliente.

## Resultados logrados <a name = "deployment"></a>

Se lograron implementar tres microservicios en python, los cuales es posible conectar por gRPC y a los cuales es posible hacer peticiones por medio de postman.

El código client.js fue planteado, sin embargo no fue probado.

  ### Problemas encontrados y objetivos no logrados
      - Por limitaciones externas (las máquinas de AWS empleadas no guardaban el código) y limitaciones de tiempo, se decidió limitar el proyecto con el uso de postman como canal de comunicación.
      - Se pedían dos lenguajes de programación en los microservicios, solo se desarollaron con uno.
      - El cliente, si bien fue creado, por limitaciones logísticas, de tiempo y de conocimiento, no fue debidamente ejecutado y probado.
      - La lógica de cada microservicio tiene oportunidades de mejora.


## Descripción técnica de la solución implementada <a name = "built_using"></a>

Para el desarrollo del presente proyecto fueron ejecutados los siguientes comandos:

pip install grpcio-tools grpcio googleapis-common-protos

Para la generación de archivos service_pb2_grpc.py,service_pb2.py, service_pb2.pyi se ejecutó el siguiente comando dentro de cada carpeta:

python -m grpc_tools.protoc -I..\carpeta\ --python_out=. --grpc_python_out=. --mypy_grpc_out=. .\service.proto

Los archivos que genera ya están en el presente repositorio, por lo que no es necesario que sea ejecutado en la consola.

  ### Extensiones de VS utilizadas para el presente proyecto
  - vscode-proto3
  - Readme Pattern

Cabe anotar que para ejecutar este proyecto es necesario tener Postman y Python instalado.

## Guía de uso <a name = "authors"></a>

1. Clone el repositorio.
2. Ubíquese en cada una de las carpetas de la carpeta servers y ejecute el comando:

    python service.py

Reemplazando "Service" por el respectivo servicio (inventory, shoppingCart, shipment)

3. Siga el siguiente tutorial para probar con Postman:

https://youtu.be/hrp727UVhbw

## Bibliografía <a name = "acknowledgement"></a>
- https://daily.dev/blog/build-a-grpc-service-in-nodejs
- https://www.youtube.com/watch?v=2oY9PbaE71A&t=1244s

Si bien no es una referencia directa, es importante aclarar que este pryecto no hubiera sido posible sin haber recibido comentarios y recomendaciones de mis compañeros de clase.
