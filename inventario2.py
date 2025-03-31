import pygame

class Inventario2:
    def __init__(self):
        pygame.init()

        self.GREEN = (0, 100, 0)
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 60)

        self.inventory_open = False
        self.inventory_rect = pygame.Rect(600, 100, 400, 500)
        self.items = []  # Começa vazio

    def draw_inventory(self, screen):
        pygame.draw.rect(screen, self.GREEN, self.inventory_rect, border_radius=15)
        for i, item in enumerate(self.items):
            x, y = self.inventory_rect.left + 40, self.inventory_rect.top + 40 + i * 80
            text = self.font.render(item, True, self.WHITE)
            screen.blit(text, (x, y))

    def get_item_at(self, pos):
        for i, item in enumerate(self.items):
            x, y = self.inventory_rect.left + 40, self.inventory_rect.top + 40 + i * 80
            if pygame.Rect(x, y, 300, 80).collidepoint(pos):
                return item
        return None
