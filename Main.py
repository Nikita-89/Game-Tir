import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Настройки окна

SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("image/тир.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения цели
target_img = pygame.image.load("image/цель.jpg")
target_wide = 80
target_height = 84

# Позиция цели
target_x = random.randint(0, SCREEN_WIDTH - target_wide)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменные для игры
score = 0  # Счетчик попаданий
start_time = time.time()  # Время начала игры
game_duration = 30  # Продолжительность игры в секундах

# Шрифт для отображения текста
font = pygame.font.SysFont(None, 55)

# Функция отображения текста на экране
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Основной игровой цикл
running = True
while running:
    screen.fill(color)

    # Получаем текущее время
    elapsed_time = time.time() - start_time

    # Проверка на завершение времени игры
    if elapsed_time >= game_duration:
        running = False
        continue

    # Отображение таймера и количества попаданий
    remaining_time = game_duration - int(elapsed_time)
    draw_text(f"Время: {remaining_time}", font, (255, 255, 255), 10, 10)
    draw_text(f"Попадания: {score}", font, (255, 255, 255), 10, 60)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_wide and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счетчик попаданий
                target_x = random.randint(0, SCREEN_WIDTH - target_wide)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отображение цели на экране
    screen.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.update()

# Завершение игры: отображение результата
screen.fill((0, 0, 0))  # Черный фон
draw_text(f"Игра окончена!", font, (255, 255, 255), SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3)
draw_text(f"Ваш результат: {score}", font, (255, 255, 255), SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2)
pygame.display.update()

# Держим результат на экране несколько секунд
time.sleep(5)

# Завершение Pygame
pygame.quit()
