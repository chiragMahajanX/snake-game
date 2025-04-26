import pygame as py
import random

py.init()
font = py.font.SysFont(None, 48)
c1 = (0, 0, 0)
c2 = (0, 255, 0)
c3 = (255, 0, 0)
clock = py.time.Clock()
sc = py.display.set_mode((800, 600))
text5 = font.render("Enter speed (1-9)", True, (255, 255, 255))

def get_speed():
    speed = 0
    selecting = True
    while selecting:
        sc.fill(c1)
        sc.blit(text5, (250, 220))
        py.display.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                return None
            if event.type == py.KEYDOWN:
                if py.K_0 <= event.key <= py.K_9:
                    speed = event.key - py.K_0
                    if speed > 0:
                        selecting = False
                        break
    return speed

def game():
    speed = get_speed()
    if speed is None:
        return False  # Exit if user closed during speed input

    x, y = 100, 100
    dx, dy = 0, 0
    start = False
    snake = [[100, 100]]
    hi = True
    run = True

    while run:
        sc.fill(c1)
        for event in py.event.get():
            if event.type == py.QUIT:
                return False
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT and dx == 0:
                    dx, dy = -20, 0
                    start = True
                elif event.key == py.K_RIGHT and dx == 0:
                    dx, dy = 20, 0
                    start = True
                elif event.key == py.K_UP and dy == 0:
                    dx, dy = 0, -20
                    start = True
                elif event.key == py.K_DOWN and dy == 0:
                    dx, dy = 0, 20
                    start = True
                elif event.key == py.K_SPACE:
                    start = False

        if hi:
            z1 = (random.randint(0, 39)) * 20
            z2 = (random.randint(0, 29)) * 20
            hi = False
        if start:
            x += dx
            y += dy

            if x >= 800 or x < 0 or y >= 600 or y < 0:
                return game_over()

            head = [x, y]
            snake.append(head)

            if head in snake[:-1]:
                return game_over()

            if abs(x - z1) < 20 and abs(y - z2) < 20:
                hi = True
            else:
                snake.pop(0)

        for i, j in enumerate(snake):
            if i == len(snake) - 1 :

                color = (0, 0, 255) 
                if dx==-20 and dy==0:
                    py.draw.circle(sc, color, [j[0]+20, j[1]-dx/2], 10)
                elif dx==20 and dy==0:
                    py.draw.circle(sc, color, [j[0], j[1]+dx/2], 10)
                elif dx==0 and dy==-20:
                    py.draw.circle(sc, color, [j[0]-dy/2, j[1]+20], 10)
                elif dx==0 and dy==20:
                    py.draw.circle(sc, color, [j[0]+dy/2, j[1]], 10)
                
                

            else:
                color=(0, 0, 255) 
                py.draw.rect(sc, color, (j[0], j[1], 20, 20))

        py.draw.rect(sc, c3, (z1, z2, 20, 20))

        score_text = font.render("Score: " + str(len(snake) - 1), True, (255, 255, 255))
        sc.blit(score_text, (10, 10))

        clock.tick(speed * 2 + 5)  # Dynamic speed
        py.display.update()

def game_over():
    sc.fill((0, 0, 0))
    text1 = font.render("Game Over!", True, (255, 255, 255))
    text2 = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    sc.blit(text1, (250, 220))
    sc.blit(text2, (100, 280))
    py.display.update()

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                return False
            if event.type == py.KEYDOWN:
                if event.key == py.K_r:
                    return True
                elif event.key == py.K_q:
                    return False

while True:
    if not game():
        break

py.quit()
