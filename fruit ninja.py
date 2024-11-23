import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Ninja")

# Загрузка изображений фруктов
apple_img = pygame.image.load('apple.png')
banana_img = pygame.image.load('banana.png')
orange_img = pygame.image.load('orange.png')


# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Класс для фруктов
class Fruit(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.speed = random.randint(4, 8)

    def update(self):
        # Перемещение фрукта вниз
        self.rect.y += self.speed

        # Удаление фрукта, когда он выходит за пределы экрана
        if self.rect.top > screen.get_height():
            self.kill()


# Основная функция игры
def main():
    clock = pygame.time.Clock()
    running = True
    score = 0
    fruits = pygame.sprite.Group()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Проверка столкновения мыши с фруктами
                mouse_pos = pygame.mouse.get_pos()
                clicked_fruits = [fruit for fruit in fruits.sprites() if fruit.rect.collidepoint(mouse_pos)]

                for fruit in clicked_fruits:
                    fruit.kill()
                    score += 100

        # Обновление группы фруктов
        fruits.update()

        # Отображение фона
        screen.fill((255, 255, 255))  # Белый фон

        # Добавление новых фруктов каждые 500 миллисекунд
        if not pygame.time.get_ticks() % 500:
            new_fruit = random.choice([Apple(screen), Banana(screen), Orange(screen)])
            fruits.add(new_fruit)

        # Отображение группы фруктов
        fruits.draw(screen)

        # Отображение счета
        draw_text(f'Score: {score}', pygame.font.SysFont(None, 32), (0, 0, 0), screen, 20, 20)

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS до 60 кадров в секунду
        clock.tick(60)

    pygame.quit()


# Подклассы для разных видов фруктов
class Apple(Fruit):
    def __init__(self, screen):
        super().__init__(apple_img, random.randint(50, screen.get_width() - 50), -100)


class Banana(Fruit):
    def __init__(self, screen):
        super().__init__(banana_img, random.randint(50, screen.get_width() - 50), -100)


class Orange(Fruit):
    def __init__(self, screen):
        super().__init__(orange_img, random.randint(50, screen.get_width() - 50), -100)


if __name__ == "__main__":
    main()