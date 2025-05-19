import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
WHITE, BLACK, BLUE, GREEN, RED = (255, 255, 255), (0, 0, 0), (100, 149, 237), (0, 200, 0), (200, 0, 0)
FONT = pygame.font.SysFont("Arial", 24)

# Topics & Difficulty Mapping
city_map = {
    "Start Zone": {"type": "info", "text": "Welcome to Python V: Code City!"},
    "Syntax District": {"type": "mcq", "difficulty": "easy", "topic": "syntax"},
    "Variables Plaza": {"type": "puzzle", "difficulty": "easy", "topic": "variables"},
    "Loops Lane": {"type": "mcq", "difficulty": "medium", "topic": "loops"},
    "Functions Avenue": {"type": "puzzle", "difficulty": "medium", "topic": "functions"},
    "OOP Station": {"type": "mcq", "difficulty": "hard", "topic": "oop"},
    "Heist HQ": {"type": "final", "text": "This is the final mission. Good luck!"}
}

city_order = list(city_map.keys())

# Player
player_pos = 0

# MCQ Database
mcqs = {
    "syntax": [
        {
            "q": "Which of these is a valid Python variable name?",
            "options": ["2value", "_value", "value$", "value-name"],
            "answer": "_value"
        }
    ],
    "loops": [
        {
            "q": "What is the output of: for i in range(3): print(i)?",
            "options": ["0 1 2", "1 2 3", "0 1 2 3", "Error"],
            "answer": "0 1 2"
        }
    ],
    "oop": [
        {
            "q": "What does OOP stand for?",
            "options": ["Only One Python", "Object Oriented Programming", "Open Optional Program", "Object On Platform"],
            "answer": "Object Oriented Programming"
        }
    ]
}

# Code Puzzles
puzzles = {
    "variables": {
        "q": "Fix the variable error:\n1x = 5\nprint(1x)",
        "answer": "_x = 5\nprint(_x)"
    },
    "functions": {
        "q": "Complete the function:\ndef greet(name):\n    _____\n\ngreet('Sam')",
        "answer": "print('Hello, ' + name)"
    }
}


def draw_map(win):
    win.fill(WHITE)
    title = FONT.render("Python V: Code City", True, BLACK)
    win.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))

    for i, loc in enumerate(city_order):
        color = GREEN if i == player_pos else BLACK
        pygame.draw.rect(win, color, (80 + i * 120, 100, 100, 100))
        label = FONT.render(loc.split()[0], True, WHITE)
        win.blit(label, (90 + i * 120, 140))
    pygame.display.update()


def ask_mcq(win, topic):
    q_data = random.choice(mcqs[topic])
    question = q_data["q"]
    options = q_data["options"]
    answer = q_data["answer"]

    while True:
        win.fill(WHITE)
        y = 50
        win.blit(FONT.render("MCQ Challenge", True, BLUE), (20, y))
        y += 40
        win.blit(FONT.render(question, True, BLACK), (20, y))
        y += 40

        buttons = []
        for i, opt in enumerate(options):
            rect = pygame.Rect(20, y, 500, 40)
            buttons.append((rect, opt))
            pygame.draw.rect(win, BLUE, rect)
            win.blit(FONT.render(opt, True, WHITE), (30, y + 5))
            y += 50

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, opt in buttons:
                    if rect.collidepoint(event.pos):
                        return opt == answer


def ask_puzzle(win, topic):
    puzzle = puzzles[topic]
    input_text = ''
    active = True

    while True:
        win.fill(WHITE)
        y = 50
        win.blit(FONT.render("Code Puzzle", True, BLUE), (20, y))
        y += 40
        for line in puzzle["q"].split('\n'):
            win.blit(FONT.render(line, True, BLACK), (20, y))
            y += 30

        pygame.draw.rect(win, BLACK, (20, y + 20, 600, 40), 2)
        win.blit(FONT.render(input_text, True, BLACK), (30, y + 25))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text.strip() == puzzle["answer"].strip()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode


def info_screen(win, text):
    while True:
        win.fill(WHITE)
        win.blit(FONT.render(text, True, BLACK), (50, 200))
        win.blit(FONT.render("Press any key to continue...", True, BLUE), (50, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def main():
    global player_pos
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python V: Code City")

    while True:
        draw_map(win)

        loc = city_order[player_pos]
        data = city_map[loc]

        if data["type"] == "info":
            info_screen(win, data["text"])
        elif data["type"] == "mcq":
            correct = ask_mcq(win, data["topic"])
            msg = "Correct! Proceeding..." if correct else "Wrong! Try again later!"
            info_screen(win, msg)
            if not correct:
                continue
        elif data["type"] == "puzzle":
            correct = ask_puzzle(win, data["topic"])
            msg = "Nice Code! Moving on." if correct else "Not quite right. Try again!"
            info_screen(win, msg)
            if not correct:
                continue
        elif data["type"] == "final":
            info_screen(win, data["text"])
            info_screen(win, "Congratulations! You've completed Code City!")
            break

        player_pos += 1
        if player_pos >= len(city_order):
            player_pos = len(city_order) - 1


if __name__ == "__main__":
    main()
