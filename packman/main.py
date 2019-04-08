import pygame

from ghosts.blinky import Blinky_directions
from ghosts.clyde import Clyde_directions
from ghosts.ghost import Ghost
from ghosts.inky import Inky_directions
from ghosts.pinky import Pinky_directions
from src import consts
from src.block import Block
from src.player import Pacman
from src.room import setupRoom
from src.wall import Wall


def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(282, 242, 42, 2, consts.white))
    all_sprites_list.add(gate)
    return gate


def startGame():
    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoom(all_sprites_list)

    gate = setupGate(all_sprites_list)

    p_turn = p_steps = 0
    b_turn = b_steps = 0
    i_turn = i_steps = 0
    c_turn = c_steps = 0

    pacman = Pacman(consts.width, consts.packman_height, "images/pacman.png")
    all_sprites_list.add(pacman)
    pacman_collide.add(pacman)

    Blinky = Ghost(consts.width, consts.binky_height, "images/Blinky.png")
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)

    Pinky = Ghost(consts.width, consts.monster_height, "images/Pinky.png")
    monsta_list.add(Pinky)
    all_sprites_list.add(Pinky)

    Inky = Ghost(consts.inky_width, consts.monster_height, "images/Inky.png")
    monsta_list.add(Inky)
    all_sprites_list.add(Inky)

    Clyde = Ghost(consts.clyde_width, consts.monster_height, "images/Clyde.png")
    monsta_list.add(Clyde)
    all_sprites_list.add(Clyde)

    # Draw the grid
    for row in range(19):
        for column in range(19):
            if (row in [7, 8]) and (column in [8, 9, 10]):
                continue
            else:
                block = Block(consts.yellow, 4, 4)

                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    block_list.add(block)
                    all_sprites_list.add(block)

    bll = len(block_list)

    score = 0

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.update_image("images/pacman_left.png")
                    pacman.change_speed(-30, 0)
                if event.key == pygame.K_RIGHT:
                    pacman.update_image("images/pacman_right.png")
                    pacman.change_speed(30, 0)
                if event.key == pygame.K_UP:
                    pacman.update_image("images/pacman_top.png")
                    pacman.change_speed(0, -30)
                if event.key == pygame.K_DOWN:
                    pacman.update_image("images/pacman_bottom.png")
                    pacman.change_speed(0, 30)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pacman.change_speed(30, 0)
                if event.key == pygame.K_RIGHT:
                    pacman.change_speed(-30, 0)
                if event.key == pygame.K_UP:
                    pacman.change_speed(0, 30)
                if event.key == pygame.K_DOWN:
                    pacman.change_speed(0, -30)

        pacman.update(wall_list, gate)

        p_turn, p_steps = Pinky.change_speed(Pinky_directions, False, p_turn, p_steps, pinky_length)
        Pinky.change_speed(Pinky_directions, False, p_turn, p_steps, pinky_length)
        Pinky.update(wall_list, False)

        b_turn, b_steps = Blinky.change_speed(Blinky_directions, False, b_turn, b_steps, blinky_length)
        Blinky.change_speed(Blinky_directions, False, b_turn, b_steps, blinky_length)
        Blinky.update(wall_list, False)

        i_turn, i_steps = Inky.change_speed(Inky_directions, False, i_turn, i_steps, inky_length)
        Inky.change_speed(Inky_directions, False, i_turn, i_steps, inky_length)
        Inky.update(wall_list, False)

        c_turn, c_steps = Clyde.change_speed(Clyde_directions, "clyde", c_turn, c_steps, clyde_length)
        Clyde.change_speed(Clyde_directions, "clyde", c_turn, c_steps, clyde_length)
        Clyde.update(wall_list, False)

        blocks_hit_list = pygame.sprite.spritecollide(pacman, block_list, True)

        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)

        screen.fill(consts.black)

        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        text = font.render("Score: " + str(score) + "/" + str(bll), True, consts.red)
        screen.blit(text, [10, 10])

        if score == bll:
            doNext("Congratulations, you won!", 145, all_sprites_list, block_list, monsta_list, pacman_collide,
                   wall_list, gate)

        monsta_hit_list = pygame.sprite.spritecollide(pacman, monsta_list, False)

        if monsta_hit_list:
            doNext("Game Over", 235, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate)

        pygame.display.flip()

        clock.tick(10)


def doNext(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    startGame()

        # Grey background
        w = pygame.Surface((400, 200))  # the size of your rect
        w.set_alpha(10)  # alpha level
        w.fill((128, 128, 128))  # this fills the entire surface
        screen.blit(w, (100, 200))  # (0,0) are the top-left coordinates

        # Won or lost
        text1 = font.render(message, True, consts.white)
        screen.blit(text1, [left, 233])

        text2 = font.render("To play again, press ENTER.", True, consts.white)
        screen.blit(text2, [135, 303])
        text3 = font.render("To quit, press ESCAPE.", True, consts.white)
        screen.blit(text3, [165, 333])

        pygame.display.flip()

        clock.tick(10)


if __name__ == "__main__":
    pacico = pygame.image.load('images/pacman.png')
    pygame.display.set_icon(pacico)

    pygame.mixer.init()
    pygame.mixer.music.load('sound/pacman.mp3')
    pygame.mixer.music.play(-1, 0.0)

    pinky_length = len(Pinky_directions)
    blinky_length = len(Blinky_directions)
    inky_length = len(Inky_directions)
    clyde_length = len(Clyde_directions)

    pygame.init()
    screen = pygame.display.set_mode([606, 606])
    pygame.display.set_caption('Pacman')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(consts.black)

    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.Font("font/freesansbold.ttf", 24)

    startGame()

    pygame.quit()
