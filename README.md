# Reproductor
Este código en Python utiliza el módulo pygame para crear una interfaz simple de reproductor de música que permite reproducir y detener una canción.
Inicializa pygame con pygame.init().

Crea la ventana principal del reproductor de música utilizando pygame.display.set_mode((500, 200)) con una resolución de 500x200 píxeles. También establece el título de la ventana como "Reproductor de Música" usando pygame.display.set_caption().

Define dos funciones: reproducir_musica() y detener_musica(). La función reproducir_musica() carga y reproduce una canción con el nombre "cancion.mp3" (se asume que existe un archivo de música con ese nombre en el directorio del programa). La función detener_musica() detiene la reproducción de la música.

Inicia un bucle principal (while ejecutando:) que se ejecutará hasta que el usuario cierre la ventana. El bucle espera eventos, como clics del mouse.

Dentro del bucle, se dibuja la interfaz del reproductor de música en la ventana principal. Se crean dos botones rectangulares utilizando pygame.draw.rect() para representar los botones de "Reproducir" y "Detener" en coordenadas específicas.

Se detecta si el usuario hace clic en alguno de los botones utilizando pygame.mouse.get_pos() para obtener la posición del mouse y pygame.mouse.get_pressed() para verificar si se ha hecho clic con el botón izquierdo del mouse.

Si el usuario hace clic en el botón de "Reproducir" (dentro de las coordenadas del botón), se llama a la función reproducir_musica(), y si hace clic en el botón de "Detener", se llama a la función detener_musica().

Se actualiza la ventana con pygame.display.update() para reflejar los cambios de dibujo.

Si el usuario cierra la ventana (evento pygame.QUIT), el bucle principal termina y se cierra pygame con pygame.quit().

El código crea una interfaz gráfica muy básica de un reproductor de música con dos botones ("Reproducir" y "Detener") y permite al usuario reproducir y detener una canción. Para que funcione correctamente, es necesario tener una canción llamada "cancion.mp3" en el mismo directorio que el archivo de código.
