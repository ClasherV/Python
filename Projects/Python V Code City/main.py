import pygame
import sys

pygame.init()

# Screen setup
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python V: Code City")

# Colors
BG_COLOR = (20, 20, 20)
TEXT_COLOR = (240, 240, 240)
HIGHLIGHT_COLOR = (100, 200, 255)
MISSION_COLOR = (200, 50, 50)
MISSION_HOVER_COLOR = (255, 100, 100)

# FPS controller
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.SysFont("Consolas", 48)
small_font = pygame.font.SysFont("Consolas", 28)

# Characters
characters = [
    {"name": "Franklin", "code_name": "AutoByte", "role": "Automation Prodigy"},
    {"name": "Michael", "code_name": "Systemic", "role": "Architect & OOP master"},
    {"name": "Trevor", "code_name": "RageCore", "role": "Raw Power & Chaos"},
]

current_char_index = 0

# Missions - each has a name and position on the map
missions = [
    {"name": "Intro to Automation", "pos": (300, 250)},
    {"name": "OOP Foundations", "pos": (600, 300)},
    {"name": "Chaos Coding", "pos": (400, 450)},
]
side_quests = [
    {"name": "Debugging Drill", "pos": (600, 120)},
    {"name": "Logic Puzzle", "pos": (800, 500)},
]

final_heist = {"name": "Final Heist: Code Breaker", "pos": (WIDTH//2, HEIGHT//2)}


def draw_text(text, x, y, font_obj, color=TEXT_COLOR):
    surface = font_obj.render(text, True, color)
    screen.blit(surface, (x, y))

def main_menu():
    global current_char_index
    running = True

    while running:
        screen.fill(BG_COLOR)

        # Title
        draw_text("Python V: Code City", WIDTH//2 - 200, 100, font, HIGHLIGHT_COLOR)

        # Current Character info
        char = characters[current_char_index]
        draw_text("Current Character:", 100, 250, small_font)
        draw_text(f"{char['name']} ({char['code_name']})", 100, 300, font)
        draw_text(f"Role: {char['role']}", 100, 370, small_font)

        # Instructions
        draw_text("Use LEFT / RIGHT arrows to switch characters", 100, 450, small_font)
        draw_text("Press ENTER to Start Missions", 100, 490, small_font)
        draw_text("Press ESC to Quit", 100, 530, small_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_char_index = (current_char_index + 1) % len(characters)
                elif event.key == pygame.K_LEFT:
                    current_char_index = (current_char_index - 1) % len(characters)
                elif event.key == pygame.K_RETURN:
                    mission_selection_screen(char)
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

def run_side_quest(character, quest_name):
    # Simple multiple choice quiz
    questions = {
        "Debugging Drill": {
            "question": "What keyword fixes bugs in Python?",
            "options": ["debug", "try", "fix", "except"],
            "answer": "try"
        },
        "Logic Puzzle": {
            "question": "Which operator means 'and' in Python?",
            "options": ["&&", "and", "AND", "&"],
            "answer": "and"
        }
    }

    q = questions.get(quest_name)
    if not q:
        # fallback
        simple_mission_screen(character, quest_name)
        return

    selected = 0
    running = True
    while running:
        screen.fill(BG_COLOR)
        draw_text(f"Side Quest: {quest_name}", 40, 50, small_font, HIGHLIGHT_COLOR)
        draw_text(q["question"], 40, 110, font)

        # Draw options
        for i, opt in enumerate(q["options"]):
            color = HIGHLIGHT_COLOR if i == selected else TEXT_COLOR
            draw_text(opt, 60, 180 + i*40, font, color)

        draw_text("Use UP/DOWN to select, ENTER to confirm, BACKSPACE to exit", 40, HEIGHT-60, small_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(q["options"])
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(q["options"])
                elif event.key == pygame.K_RETURN:
                    if q["options"][selected] == q["answer"]:
                        # Success message
                        success_screen(f"Correct! You completed {quest_name}!", character)
                        running = False
                    else:
                        # Fail message (simple)
                        fail_screen(f"Wrong answer. Try again.", character)
                elif event.key == pygame.K_BACKSPACE:
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

def success_screen(message, character):
    # Show message for 2 seconds or until key press
    timer = 120  # 2 seconds at 60 FPS
    while timer > 0:
        screen.fill(BG_COLOR)
        draw_text(message, 50, HEIGHT//2 - 30, font, (50, 200, 50))
        draw_text("Press any key to continue...", 50, HEIGHT//2 + 30, small_font, TEXT_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)
        timer -= 1

def fail_screen(message, character):
    # Show message for 2 seconds
    timer = 120
    while timer > 0:
        screen.fill(BG_COLOR)
        draw_text(message, 50, HEIGHT//2 - 30, font, (200, 50, 50))
        draw_text("Try again!", 50, HEIGHT//2 + 30, small_font, TEXT_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(FPS)
        timer -= 1

def run_final_heist(character):
    # Step 1: Typing challenge (reuse code snippet)
    code_snippet = "def hack_the_mainframe():"
    user_input = ""
    step = 1
    completed_step1 = False
    running = True

    while running:
        screen.fill(BG_COLOR)

        if step == 1:
            draw_text("Final Heist - Step 1: Typing Challenge", 40, 40, small_font, HIGHLIGHT_COLOR)
            draw_text(f"Type: {code_snippet}", 40, 90, font)

            # Draw user input
            correct_text = ""
            incorrect_text = ""
            for i, char in enumerate(user_input):
                if i < len(code_snippet) and char == code_snippet[i]:
                    correct_text += char
                else:
                    incorrect_text += char

            correct_surface = font.render(correct_text, True, (50, 200, 50))
            screen.blit(correct_surface, (40, 130))

            if incorrect_text:
                correct_width = correct_surface.get_width()
                incorrect_surface = font.render(incorrect_text, True, (200, 50, 50))
                screen.blit(incorrect_surface, (40 + correct_width, 130))

            if user_input == code_snippet:
                completed_step1 = True
                draw_text("Step 1 Complete! Press ENTER to continue.", 40, 180, small_font, (200, 255, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and not completed_step1:
                    if event.key == pygame.K_BACKSPACE:
                        if len(user_input) > 0:
                            user_input = user_input[:-1]
                    else:
                        if len(user_input) < len(code_snippet):
                            if event.unicode and event.unicode.isprintable():
                                user_input += event.unicode
                elif event.type == pygame.KEYDOWN and completed_step1:
                    if event.key == pygame.K_RETURN:
                        step = 2

        elif step == 2:
            # Simple quiz for step 2
            question = "What function starts a Python program?"
            options = ["main()", "start()", "init()", "begin()"]
            answer = "main()"
            selected = 0

            quiz_running = True
            while quiz_running:
                screen.fill(BG_COLOR)
                draw_text("Final Heist - Step 2: Quiz", 40, 40, small_font, HIGHLIGHT_COLOR)
                draw_text(question, 40, 90, font)
                for i, opt in enumerate(options):
                    color = HIGHLIGHT_COLOR if i == selected else TEXT_COLOR
                    draw_text(opt, 60, 160 + i*40, font, color)

                draw_text("Use UP/DOWN to select, ENTER to confirm", 40, HEIGHT-80, small_font)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            selected = (selected - 1) % len(options)
                        elif event.key == pygame.K_DOWN:
                            selected = (selected + 1) % len(options)
                        elif event.key == pygame.K_RETURN:
                            if options[selected] == answer:
                                success_screen("You cracked the final code! Mission Success!", character)
                                quiz_running = False
                                running = False
                            else:
                                fail_screen("Wrong answer! Try again.", character)
                        elif event.key == pygame.K_BACKSPACE:
                            quiz_running = False
                            running = False

                pygame.display.flip()
                clock.tick(FPS)
            break

        pygame.display.flip()
        clock.tick(FPS)


def mission_selection_screen(character):
    running = True

    while running:
        screen.fill(BG_COLOR)

        # Title and instructions
        draw_text(f"Select a Mission - {character['name']} ({character['code_name']})", 50, 50, small_font, HIGHLIGHT_COLOR)
        draw_text("Click a mission to start, or press BACKSPACE to return", 50, 90, small_font)

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True

            # Draw side quests on map
    for sq in side_quests:
        x, y = sq["pos"]
        dist = ((mouse_pos[0]-x)**2 + (mouse_pos[1]-y)**2)**0.5
        color = (255, 215, 0) if dist < 25 else (255, 165, 0)  # Gold/orange colors
        pygame.draw.rect(screen, color, (x-20, y-20, 40, 40))  # Side quests as squares
        draw_text(sq["name"], x + 30, y - 10, small_font)

        if dist < 25 and mouse_clicked:
            run_side_quest(character, sq["name"])

    # Draw final heist if all main missions done (for simplicity, always show)
    x, y = final_heist["pos"]
    dist = ((mouse_pos[0]-x)**2 + (mouse_pos[1]-y)**2)**0.5
    color = (150, 0, 150) if dist < 30 else (200, 0, 200)  # Purple hues
    pygame.draw.circle(screen, color, (x, y), 30)
    draw_text(final_heist["name"], x + 35, y - 10, small_font)

    if dist < 30 and mouse_clicked:
        run_final_heist(character)


        # Draw missions as circles
        for m in missions:
            x, y = m["pos"]
            dist = ((mouse_pos[0]-x)**2 + (mouse_pos[1]-y)**2)**0.5

            color = MISSION_HOVER_COLOR if dist < 25 else MISSION_COLOR
            pygame.draw.circle(screen, color, (x, y), 25)
            draw_text(m["name"], x + 40, y - 15, small_font)

            # Click to start mission
            if dist < 25 and mouse_clicked:
                run_mission(character, m["name"])

        pygame.display.flip()
        clock.tick(FPS)

def run_mission(character, mission_name):
    # Only "Intro to Automation" has a mini-game, others show placeholder screen
    if mission_name == "Intro to Automation":
        typing_challenge(character, mission_name)
    else:
        simple_mission_screen(character, mission_name)

def simple_mission_screen(character, mission_name):
    running = True
    while running:
        screen.fill(BG_COLOR)
        draw_text(f"Mission: {mission_name}", 50, 150, font, HIGHLIGHT_COLOR)
        draw_text(f"Playing as: {character['name']} ({character['code_name']})", 50, 220, small_font)
        draw_text("Press BACKSPACE to return to Missions", 50, 280, small_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

def typing_challenge(character, mission_name):
    # Python snippet to type
    code_snippet = "print('Hello, Automation!')"
    user_input = ""
    running = True
    completed = False

    while running:
        screen.fill(BG_COLOR)

        draw_text(f"Mission: {mission_name} - Typing Challenge", 40, 50, small_font, HIGHLIGHT_COLOR)
        draw_text(f"Playing as: {character['name']} ({character['code_name']})", 40, 90, small_font)
        draw_text("Type the following code:", 40, 130, small_font)

        # Show the code snippet
        draw_text(code_snippet, 40, 170, font)

        # Show user input with coloring (green correct chars, red wrong)
        correct_text = ""
        incorrect_text = ""

        for i, char in enumerate(user_input):
            if i < len(code_snippet) and char == code_snippet[i]:
                correct_text += char
            else:
                incorrect_text += char

        # Draw correct part in green
        correct_surface = font.render(correct_text, True, (50, 200, 50))
        screen.blit(correct_surface, (40, 220))

        # Draw incorrect part in red (next to correct part)
        if incorrect_text:
            correct_width = correct_surface.get_width()
            incorrect_surface = font.render(incorrect_text, True, (200, 50, 50))
            screen.blit(incorrect_surface, (40 + correct_width, 220))

        # Check for completion
        if user_input == code_snippet:
            completed = True
            draw_text("Success! Mission Complete! Press BACKSPACE to return.", 40, 300, small_font, (200, 255, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not completed:
                if event.key == pygame.K_BACKSPACE:
                    if len(user_input) > 0:
                        user_input = user_input[:-1]
                else:
                    # Add key pressed if length allows
                    if len(user_input) < len(code_snippet):
                        # Only add printable characters
                        if event.unicode and event.unicode.isprintable():
                            user_input += event.unicode
            elif event.type == pygame.KEYDOWN and completed:
                if event.key == pygame.K_BACKSPACE:
                    running = False

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main_menu()
