import pygame
from inventario1 import Inventario1

# Inicialização do Pygame
pygame.init()

# Definir as dimensões da tela e criar a janela em tela cheia
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Cores
BLACK = (0, 0, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Botão para abrir o inventário 2
button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 100, 140, 60)

# Variáveis de controle de arrastar itens
dragging_item = None
dragging_from = None

# Criar as instâncias dos inventários
inventario1 = Inventario1((50, 50, 50), 100, ["Espada", "Poção", "Escudo"])
inventario2 = Inventario1((0, 100, 0), 600)

# Variável de controle do loop
running = True

# Função principal para o loop do jogo
def main():
    global running, dragging_item, dragging_from
    
    while running:

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LALT, pygame.K_RALT):
                    inventario1.inventory_open = not inventario1.inventory_open
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    inventario2.inventory_open = not inventario2.inventory_open

                if inventario1.inventory_open:
                    item = inventario1.get_item_at(event.pos)
                    if item:
                        dragging_item = item
                        dragging_from = "inventory1"

                if inventario2.inventory_open:
                    item = inventario2.get_item_at(event.pos)
                    if item:
                        dragging_item = item
                        dragging_from = "inventory2"

            if event.type == pygame.MOUSEBUTTONUP:
                # Handle mouse button release
                if dragging_item:
                    if inventario2.inventory_open and inventario2.inventory_rect.collidepoint(event.pos) and dragging_from == "inventory1":
                        inventario1.items.remove(dragging_item)
                        inventario2.items.append(dragging_item)
                    elif inventario1.inventory_open and inventario1.inventory_rect.collidepoint(event.pos) and dragging_from == "inventory2":
                        inventario2.items.remove(dragging_item)
                        inventario1.items.append(dragging_item)
                    dragging_item = None
                    dragging_from = None

        # Desenhar os inventários e o botão
        if inventario1.inventory_open:
            inventario1.draw_inventory(screen)
        if inventario2.inventory_open:
            inventario2.draw_inventory(screen)

        inventario1.draw_button(screen)  # Agora o método `draw_button` é da classe Inventario1

        if dragging_item:
            inventario1.draw_dragging_item(screen, dragging_item)  # Agora o método `draw_dragging_item` é da classe Inventario1

        pygame.display.flip()
        clock.tick(30)

# Chamar a função principal para rodar o jogo
if __name__ == "__main__":
    main()

# Finalizar o Pygame
pygame.quit()
