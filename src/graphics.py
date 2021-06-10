import pygame

import engine

SIZE = 63
BLOCK_SIZE = SIZE * 10 // 9
MID_BLOCK = BLOCK_SIZE // 2


def add_default(n, pos):
    y = pos // 9
    x = pos % 9

    engine.grid[y][x] = n


def print_courser(w, pos):
    y = pos // 9
    x = pos % 9

    X = BLOCK_SIZE * x + MID_BLOCK
    Y = BLOCK_SIZE * y + MID_BLOCK

    pygame.draw.rect(w, (0, 0, 0), [X - 1, Y - 1, 2, 2])


def print_grid(w):
    for x in range(9):
        if x % 3 == 0:
            pygame.draw.line(w, (0, 0, 0), (BLOCK_SIZE * x, 0), (BLOCK_SIZE * x, SIZE * 10), 3)
        else:
            pygame.draw.line(w, (0, 0, 0), (BLOCK_SIZE * x, 0), (BLOCK_SIZE * x, SIZE * 10))
    for y in range(9):
        if y % 3 == 0:
            pygame.draw.line(w, (0, 0, 0), (0, BLOCK_SIZE * y), (SIZE * 10, BLOCK_SIZE * y), 3)
        else:
            pygame.draw.line(w, (0, 0, 0), (0, BLOCK_SIZE * y), (SIZE * 10, BLOCK_SIZE * y))


def print_board(w, grid):
    font = pygame.font.Font('freesansbold.ttf', 32)
    for y in range(9):
        for x in range(9):
            color = (0, 0, 0)
            n = grid[y][x]
            if n == 0:
                n = ""
            if engine.made[y][x]:
                color = (0, 255, 0)
            text = font.render(str(n), True, color, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (BLOCK_SIZE * x + MID_BLOCK, BLOCK_SIZE * y + MID_BLOCK)
            w.blit(text, textRect)


def main():
    pygame.init()
    display_surface = pygame.display.set_mode((SIZE * 10, SIZE * 10))
    solved = False
    place = 0
    while True:
        display_surface.fill((255, 255, 255))
        print_grid(display_surface)
        print_board(display_surface, engine.grid)
        if solved:
            engine.solve(display_surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if place == 81:
                if event.type == pygame.MOUSEBUTTONUP:
                    solved = not solved
            keys = pygame.key.get_pressed()
            if place < 81:
                print_courser(display_surface, place)
                if keys[pygame.K_0]:
                    add_default(0, place)
                    place += 1
                elif keys[pygame.K_1]:
                    add_default(1, place)
                    place += 1
                elif keys[pygame.K_2]:
                    add_default(2, place)
                    place += 1
                elif keys[pygame.K_3]:
                    add_default(3, place)
                    place += 1
                elif keys[pygame.K_4]:
                    add_default(4, place)
                    place += 1
                elif keys[pygame.K_5]:
                    add_default(5, place)
                    place += 1
                elif keys[pygame.K_6]:
                    add_default(6, place)
                    place += 1
                elif keys[pygame.K_7]:
                    add_default(7, place)
                    place += 1
                elif keys[pygame.K_8]:
                    add_default(8, place)
                    place += 1
                elif keys[pygame.K_9]:
                    add_default(9, place)
                    place += 1
                elif keys[pygame.K_BACKSPACE]:
                    place -= 1
                engine.create_made()
            pygame.display.update()


if __name__ == '__main__':
    main()
