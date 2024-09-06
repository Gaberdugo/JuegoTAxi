import pygame, random, sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva a los taxi")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 143, 57)
GRIS = (138, 149, 151)

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Fuente para el texto
fuente = pygame.font.SysFont('Arial', 55)

# Jugador
tamano_jugador = 50
color_jugador = (0, 128, 255)
pos_jugador = [ tamano_jugador, ALTO // 2]
puntos = 0

# Objetos que caen
tamano_objeto = 50
color_objeto = AMARILLO
pos_objeto = pos_objeto = [ANCHO - tamano_objeto, random.randint(2 * tamano_jugador, ALTO - 2 * tamano_jugador - tamano_objeto)]
velocidad_objeto = 10

# Función para dibujar el menú principal
def dibujar_menu():
    pantalla.fill(NEGRO)
    texto_titulo = fuente.render('Esquiva a los taxi', True, BLANCO)
    texto_inicio = fuente.render('Presiona Enter para Iniciar', True, BLANCO)
    texto_salir = fuente.render('Presiona S para Salir', True, BLANCO)
    
    pantalla.blit(texto_titulo, (ANCHO // 5.5, ALTO // 4))
    pantalla.blit(texto_inicio, (ANCHO // 5.5, ALTO // 2))
    pantalla.blit(texto_salir, (ANCHO // 5.5, ALTO // 1.5))

# Función para dibujar la pantalla de Game Over
def dibujar_game_over():
    global pos_jugador, pos_objeto, velocidad_objeto, tamano_jugador, puntos
    pantalla.fill(NEGRO)
    texto_game_over = fuente.render(f'¡Juego Terminado! Sacaste {puntos}', True, BLANCO)
    texto_reiniciar = fuente.render('Presiona Enter para Reiniciar', True, BLANCO)
    texto_salir = fuente.render('Presiona S para Salir', True, BLANCO)
    
    pantalla.blit(texto_game_over, (ANCHO // 6, ALTO // 4))
    pantalla.blit(texto_reiniciar, (ANCHO // 6, ALTO // 2))
    pantalla.blit(texto_salir, (ANCHO // 6, ALTO // 1.5))

    pos_jugador = [ tamano_jugador, ALTO // 2]
    pos_objeto = pos_objeto = [ANCHO - tamano_objeto, random.randint(2 * tamano_jugador, ALTO - 2 * tamano_jugador - tamano_objeto)]
    velocidad_objeto = 10
    puntos = 0

# Función principal del juego
def bucle_juego():
    global pos_jugador, pos_objeto, velocidad_objeto, puntos

    iterador = 1

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and pos_jugador[1] > 2 * tamano_jugador:
            pos_jugador[1] -= 10
        if teclas[pygame.K_DOWN] and pos_jugador[1] < ALTO - 3 * tamano_jugador:
            pos_jugador[1] += 10
        
        # Actualización de la posición del objeto
        pos_objeto[0] -= velocidad_objeto

        if iterador % 200 == 0:
            velocidad_objeto += 10

        if pos_objeto[0] < 0:
            puntos += 1
            pos_objeto = [ANCHO - tamano_objeto, random.randint(2 * tamano_jugador, ALTO - 2 * tamano_jugador - tamano_objeto)]

        # Detección de colisión
        if (pos_jugador[0] < pos_objeto[0] < pos_jugador[0] + tamano_jugador or
            pos_jugador[0] < pos_objeto[0] + tamano_objeto < pos_jugador[0] + tamano_jugador) and \
           (pos_jugador[1] < pos_objeto[1] < pos_jugador[1] + tamano_jugador or
            pos_jugador[1] < pos_objeto[1] + tamano_objeto < pos_jugador[1] + tamano_jugador):
            return
        
        # Dibujar todo
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, color_jugador, (pos_jugador[0], pos_jugador[1], tamano_jugador, tamano_jugador))
        pygame.draw.rect(pantalla, color_objeto, (pos_objeto[0], pos_objeto[1], tamano_objeto, tamano_objeto))
        pygame.draw.rect(pantalla, VERDE, (0, 0, ANCHO, 1.75 * tamano_jugador))
        pygame.draw.rect(pantalla, VERDE, (0, ALTO - 1.75 * tamano_jugador, ANCHO, 1.75 * tamano_jugador))
        pygame.draw.rect(pantalla, GRIS, (0, 1.75 * tamano_jugador, ANCHO, 0.25 * tamano_jugador))
        pygame.draw.rect(pantalla, GRIS, (0, ALTO - 2 * tamano_jugador, ANCHO, 0.25 * tamano_jugador))
        texto_puntos = fuente.render(str(puntos), True, BLANCO)
        pantalla.blit(texto_puntos, (ANCHO - 2 * tamano_jugador, tamano_jugador//2))
        pygame.display.flip()

        iterador += 1
        # Controlar la velocidad de fotogramas
        reloj.tick(30)

# Bucle principal del programa
def principal():
    while True:
        dibujar_menu()
        pygame.display.flip()
        
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        pygame.quit()
                        sys.exit()
                    elif evento.key == pygame.K_RETURN:
                        bucle_juego()
                        dibujar_game_over()
                        pygame.display.flip()
                        
                        while True:
                            for evento in pygame.event.get():
                                if evento.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif evento.type == pygame.KEYDOWN:
                                    if evento.key == pygame.K_s:
                                        pygame.quit()
                                        sys.exit()
                                    elif evento.key == pygame.K_RETURN:
                                        principal()

if __name__ == "__main__":
    principal()