import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Python V: Code City")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (30, 30, 30)
BLUE = (50, 150, 255)
GREEN = (50, 255, 100)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Fonts
FONT = pygame.font.SysFont("consolas", 24)
BIG_FONT = pygame.font.SysFont("consolas", 36, bold=True)

# Player data
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_speed = 5
player_size = 40

# Characters & roles
characters = [
    {"name": "Michael", "role": "Systemic", "color": (0, 180, 255)},
    {"name": "Franklin", "role": "AutoByte", "color": (0, 255, 100)},
    {"name": "Trevor", "role": "RageCore", "color": (255, 80, 30)},
]
current_character = 0

# Map zones (just rectangles for now)
zones = {
    "Intro Town": pygame.Rect(50, 50, 300, 200),
    "Script Side": pygame.Rect(400, 100, 350, 250),
    "Logic Loop Lane": pygame.Rect(800, 50, 350, 200),
    "OOP Hills": pygame.Rect(50, 400, 300, 250),
    "Hack Street": pygame.Rect(400, 400, 350, 250),
    "Async Alley": pygame.Rect(800, 400, 350, 250),
}

def draw_map():
    # Background
    screen.fill(DARK_GREY)
    
    # Draw zones
    for name, rect in zones.items():
        pygame.draw.rect(screen, BLUE, rect, 3)
        text_surf = FONT.render(name, True, WHITE)
        screen.blit(text_surf, (rect.x + 10, rect.y + 10))

def draw_player():
    color = characters[current_character]["color"]
    pygame.draw.rect(screen, color, (*player_pos, player_size, player_size))
    # Player label
    name = characters[current_character]["name"]
    label = FONT.render(f"Player: {name}", True, WHITE)
    screen.blit(label, (10, SCREEN_HEIGHT - 30))

def draw_hud():
    # Current character role
    role = characters[current_character]["role"]
    role_text = FONT.render(f"Role: {role}", True, WHITE)
    screen.blit(role_text, (10, SCREEN_HEIGHT - 60))
    
    # Controls info
    controls = "Move: Arrow Keys or WASD | Switch Char: TAB"
    ctrl_text = FONT.render(controls, True, WHITE)
    screen.blit(ctrl_text, (SCREEN_WIDTH//2 - ctrl_text.get_width()//2, SCREEN_HEIGHT - 30))

def handle_movement(keys):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos[1] += player_speed
    
    # Keep player in screen bounds
    player_pos[0] = max(0, min(SCREEN_WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(SCREEN_HEIGHT - player_size, player_pos[1]))

def switch_character():
    global current_character
    current_character = (current_character + 1) % len(characters)

def main():
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    switch_character()
        
        keys = pygame.key.get_pressed()
        handle_movement(keys)
        
        # Draw everything
        draw_map()
        draw_player()
        draw_hud()
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
