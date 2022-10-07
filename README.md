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

# ¿Para quién es este lab?

Para personas nivel basico/medio  

# Tabla de contenido:

Parte 1: Conocer el algoritmo 
Parte 2: Conocer [encode/decode de valor entero](https://github.com/libialany/b_encoder/blob/main/int_encode_decode_.py)

Parte 3: Conocer [encode/decode de valor texto](https://github.com/libialany/b_encoder/blob/main/str_encode_decode.py)

Parte 4: Conocer [encode/decode de una estructura lista](https://github.com/libialany/b_encoder/blob/main/ls_encode_decode.py)


## Run

- python3  int_encode_decode_.py -v

- python3  str_encode_decode.py -v

- python3  ls_encode_decode.py -v 

Una implementacion completa se puede encontrar en [utdemir](https://github.com/utdemir/bencoder).

![image](https://user-images.githubusercontent.com/82403984/194634259-ea2e1f2b-26c1-4c13-a184-347d9bd6c8f0.png)



# Mas material
 🤷‍♂️ 
