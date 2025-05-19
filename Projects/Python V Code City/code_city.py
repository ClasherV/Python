import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (0, 255, 100)
FONT_NAME = 'freesansbold.ttf'

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python V: Code City")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(FONT_NAME, 36)
small_font = pygame.font.Font(FONT_NAME, 24)

# Characters
characters = [
    {"name": "Neo the Debugger", "color": (255, 100, 100)},
    {"name": "Byte Buster", "color": (100, 255, 100)},
    {"name": "Captain Syntax", "color": (100, 100, 255)}
]

# Missions
missions = {
    "Neo the Debugger": ["Loop Labyrinth", "Syntax Swamp"],
    "Byte Buster": ["Memory Maze", "Variable Vault"],
    "Captain Syntax": ["Error Express", "String Stronghold"]
}

# Typing challenges for each mission
challenges = {
    "Loop Labyrinth": ["for i in range(5):", "while True:"],
    "Syntax Swamp": ["if x == 10:", "def my_function():", "elif y > 3:"],
    "Memory Maze": ["list = [1, 2, 3]", "list.append(4)", "del list[0]"],
    "Variable Vault": ["x = 5", "name = 'Python'", "flag = True"],
    "Error Express": ["try:", "except Exception as e:", "raise ValueError"],
    "String Stronghold": ["s = 'hello'", "print(s.upper())", "s.find('e')"]
}

# Helper to draw centered text
def draw_text(text, size, y, font_obj, color=TEXT_COLOR):
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(text_surface, text_rect)

# Start screen
def start_screen():
    screen.fill(BG_COLOR)
    draw_text("PYTHON V: CODE CITY", 64, 150, font)
    draw_text("Press ENTER to start", 36, 300, small_font)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

# Character selection
def character_selection():
    selected = 0
    selecting = True

    while selecting:
        screen.fill(BG_COLOR)
        draw_text("Select Your Hacker", 48, 100, font)
        for i, char in enumerate(characters):
            color = HIGHLIGHT_COLOR if i == selected else TEXT_COLOR
            draw_text(char['name'], 32, 200 + i * 60, small_font, color)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(characters)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(characters)
                elif event.key == pygame.K_RETURN:
                    return characters[selected]['name']

# Mission screen
def mission_screen(character):
    available_missions = missions[character]
    selected = 0
    choosing = True

    while choosing:
        screen.fill(BG_COLOR)
        draw_text(f"{character} - Choose a Mission", 36, 100, font)
        for i, mission in enumerate(available_missions):
            color = HIGHLIGHT_COLOR if i == selected else TEXT_COLOR
            draw_text(mission, 32, 200 + i * 60, small_font, color)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(available_missions)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(available_missions)
                elif event.key == pygame.K_RETURN:
                    return available_missions[selected]

# Typing challenge
def typing_challenge(character, mission_name):
    phrases = challenges[mission_name]
    input_text = ''
    target_text = random.choice(phrases)
    active = True

    while active:
        screen.fill(BG_COLOR)
        draw_text(f"{character} in {mission_name}", 28, 50, small_font)
        draw_text("Type the code:", 28, 120, small_font)
        draw_text(target_text, 32, 180, font, HIGHLIGHT_COLOR)
        draw_text(input_text, 32, 240, font, TEXT_COLOR)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text.strip() == target_text:
                        active = False
                else:
                    input_text += event.unicode

# Main game loop
def main():
    current_character = None
    running = True

    while running:
        start_screen()
        current_character = character_selection()
        mission_name = mission_screen(current_character)
        typing_challenge(current_character, mission_name)

        # Final message
        screen.fill(BG_COLOR)
        draw_text("Mission Completed!", 40, 150, font, HIGHLIGHT_COLOR)
        draw_text("Press ENTER to play again or ESC to quit.", 36, 220, small_font)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        waiting = False

    pygame.quit()
    sys.exit()

# Run game
if __name__ == "__main__":
    main()
