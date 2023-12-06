# Adivina-el-numero
Es un proyecto desarrollado en python3 que es el juego de adivina el numero, tiene su version en consola y su version con interfaz gráfica
# Version Consola
El archivo llamado proyecto_consola obviamente es la versión del juego en consola, es simple su uso, simplemente tendrás que digitar un numero del 1 al 100 y mientras vayas poniendo numeros se te irán dando ciertas pistas.
En el momento que adivines el numero se te informará de ello y te dirá el numero de intentos que te costó.
El rango del numero a adivinar lo puedes cambiar en la variable numero_aleatorio, en la parte random.randint(1,100) puedes cambiar el rango por ejemplo de 1 al 1000 simplemente cambias los numeros a tu gusto

# Version Gráfica
La versión gráfica tiene la misma logica que la de consola solo que es más intuitivo y tiene ciertas mejoras, por ejemplo puede detectar si digitaste un espacio en blanco o una letra el programa lo detecta y te muestra un error, también como un plus agregué un boton que lo pueden descargar y usarlo en el programa, si lo descargar pueden crear una carpeta llamada boton y ahí poner la imgen del boton para que no tengan que editar el programa, y en el caso que no quieran usar una imagen como boton tienen que editar la siguiente linea:

boton_enviar = Button(root, image=boton , border=0 ,command=verificar_numero).pack()

Ahí solo tendrías que borrar el apartado image y poner un text="" con el texto que quieras y para que el boton se vea un poco más te recomendaria quitar el apartado border=0.

Espero y disfruten ambas versiones
