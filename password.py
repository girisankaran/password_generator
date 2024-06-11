import pygame
import random
import string

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 32)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def draw_text(surface, text, position, font, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def main():
    running = True
    input_active = True
    input_text = ''
    password_length = 8

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        password_length = int(input_text)
                        password = generate_password(password_length)
                        print("Your generated password is:", password)
                        running = False
                elif input_active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.unicode.isdigit():
                        input_text += event.unicode
        
        screen.fill(WHITE)
        draw_text(screen, "Enter password length and press Enter", (20, 20), font, BLACK)
        draw_text(screen, input_text, (20, 60), font, BLACK)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
