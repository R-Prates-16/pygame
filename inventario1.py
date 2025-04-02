import pygame

class Inventario1:
    def __init__(self):
        pygame.init()
        
        self.DARK_GRAY = (50, 50, 50)
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 40)
        
        self.inventory_open = False
        self.inventory_rect = pygame.Rect(100, 100, 400, 500)
        
        # Carregar imagens
        self.bg_image = pygame.image.load("fundo.jpeg")
        self.bg_image = pygame.transform.scale(self.bg_image, (400, 500))

        self.character_image = pygame.image.load("personagem.png")
        self.character_image = pygame.transform.scale(self.character_image, (80, 80))

        self.items = [
            ("Espada", pygame.image.load("espada.png")),
            ("Escudo", pygame.image.load("escudo.png")),
            ("Armadura", pygame.image.load("armadura.png")),
            ("Poção", pygame.image.load("pocao.png")),
            ("Velocidade", pygame.image.load("velocidade.png"))
        ]
        
        # Ajustar tamanhos e deslocamento
        for i in range(len(self.items)):
            if self.items[i][0] == "Poção":
                new_size = (43, 43)  # Aumentado em +3px
            elif self.items[i][0] == "Armadura":
                new_size = (48, 48)  # Aumentado em +3px
            else:
                new_size = (30, 30)  # Mantém padrão para os outros
            
            self.items[i] = (self.items[i][0], pygame.transform.scale(self.items[i][1], new_size))

    def draw_inventory(self, screen):
        pygame.draw.rect(screen, self.DARK_GRAY, self.inventory_rect, border_radius=20)
        screen.blit(self.bg_image, (self.inventory_rect.x, self.inventory_rect.y))

        # Desenhar círculo do personagem
        circle_x = self.inventory_rect.x + 100
        circle_y = self.inventory_rect.y + 80
        pygame.draw.circle(screen, self.WHITE, (circle_x, circle_y), 50)

        # Posicionar personagem dentro do círculo
        char_x = circle_x - self.character_image.get_width() // 2
        char_y = circle_y - self.character_image.get_height() // 2
        screen.blit(self.character_image, (char_x, char_y))

        # Nome do personagem
        text = self.font.render("Guerreiro", True, self.WHITE)
        screen.blit(text, (self.inventory_rect.x + 180, self.inventory_rect.y + 60))

        # Desenhar os itens do inventário
        for i, (item_name, item_image) in enumerate(self.items):
            x_offset = -8 if item_name in ["Poção", "Armadura"] else 0  # Deslocamento ajustado para a esquerda
            x = self.inventory_rect.left + 40 + x_offset
            y = self.inventory_rect.top + 160 + i * 50
            screen.blit(item_image, (x, y))

            text = self.font.render(item_name, True, self.WHITE)
            screen.blit(text, (self.inventory_rect.left + 90, y + 5))  # Mantém a posição do texto

    def get_item_at(self, pos):
        for i, (item_name, item_image) in enumerate(self.items):
            x_offset = -8 if item_name in ["Poção", "Armadura"] else 0
            x = self.inventory_rect.left + 40 + x_offset
            y = self.inventory_rect.top + 160 + i * 50
            if pygame.Rect(x, y, 200, 40).collidepoint(pos):
                return (item_name, item_image)
        return None
