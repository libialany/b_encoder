# b_encoder
📢 Pyladies El ALto Lab
![image](https://media.giphy.com/media/S9i8jJxTvAKVHVMvvW/giphy.gif)

En esta temporada, estamos creando un encode/decode bittorrent file.


# Introduccion



__usos del protocolo__

Como ya sabrá como usuario de Linux, muchos desarrolladores de distribuciones de Linux eligen compartir su sistema operativo en forma de descarga de torrent. [mas referencias](https://linuxconfig.org/how-to-create-and-share-torrent-on-linux)

__client torrent__

Un client torrent necesita muchas funcionalidades ,por ejemplo:
- Leer un archivo torrent
- Scrapear udp o http
- Conectar con compañeros(Peers).
- Peticiones de bloques de informacion(archivos).
- Guarde un bloque en la RAM, y cuando una pieza esté completa y verificada, escriba los datos en su disco duro
- Trate con los torrentes de un archivo o de varios archivos
- Seed entre peerings.

__b encode__

Bencode (pronunciado como Bee-encode ) es la codificación utilizada por el sistema de intercambio de archivos entre pares BitTorrent para almacenar y transmitir datos poco estructurados. [mas referncia](https://en.wikipedia.org/wiki/Bencode)

## solo realizamos una funcionalidad de lo que seria un client torrent

¿Para quién es este lab?

Para personas nivel basico/medio  

# Tabla de contenido:

Parte 1: Conocer el algoritmo 
Parte 2: Conocer [encode/decode de valor entero](https://github.com/libialany/b_encoder/blob/main/int_encode_decode_.py)

Parte 3: Conocer [encode/decode de valor texto](https://github.com/libialany/b_encoder/blob/main/str_encode_decode.py)

Parte 4: Conocer [encode/decode de una estructura lista](https://github.com/libialany/b_encoder/blob/main/ls_encode_decode.py)

Addional: Regex scripting para linux[updating script](https://gist.github.com/yumminhuang/8b1502a49d8b20a6ae70)

# Mas material
 🤷‍♂️ 
