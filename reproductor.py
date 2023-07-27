import pygame
# desbes instalar el modulo pygame
# Inicializar pygame
pygame.init()

# Crear la ventana principal
ventana_principal = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Reproductor de Música")

# Función para reproducir la música
def reproducir_musica():
    pygame.mixer.music.load("cancion.mp3")
    pygame.mixer.music.play()

# Función para detener la música
def detener_musica():
    pygame.mixer.music.stop()

# Bucle principal del programa
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # Dibujar la interfaz del reproductor de música
    ventana_principal.fill((255, 255, 255))
    pygame.draw.rect(ventana_principal, (0, 128, 0), (50, 50, 100, 50))  # Botón de reproducir
    pygame.draw.rect(ventana_principal, (255, 0, 0), (200, 50, 100, 50))  # Botón de detener

    # Detectar clics en los botones
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if 50 <= mouse_pos[0] <= 150 and 50 <= mouse_pos[1] <= 100:
            reproducir_musica()
        elif 200 <= mouse_pos[0] <= 300 and 50 <= mouse_pos[1] <= 100:
            detener_musica()

    pygame.display.update()

# Cerrar pygame
pygame.quit()
