import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("fundomenu.png")


def get_font(size):
    return pygame.font.Font("8-BIT WONDER.TTF", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Jogo", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(400, 400),
                           text_input="VOLTAR", font=get_font(65), base_color="#368170", hovering_color="White")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(35).render("Ayrton da Silva", True, "#70d885")
        OPTIONS_TEXT2 = get_font(35).render("Julia Gomes", True, "#70d885")
        OPTIONS_TEXT3 = get_font(35).render("Matheus Vicente", True, "#70d885")


        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 216))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_RECT = OPTIONS_TEXT2.get_rect(center=(400, 275))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT)

        OPTIONS_RECT = OPTIONS_TEXT3.get_rect(center=(400, 333))
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT)


        OPTIONS_BACK = Button(image=None, pos=(400, 400),
                              text_input="VOLTAR", font=get_font(65), base_color="#368170", hovering_color="Black")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("MENU PRINCIPAL", True, "#70d885")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 83))

        PLAY_BUTTON = Button(image=pygame.image.load("Fundo Rect.png"), pos=(400, 208),
                             text_input="JOGAR", font=get_font(45), base_color="#c7e4c6", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Fundo Rect.png"), pos=(400, 333),
                                text_input="CREDITOS", font=get_font(45), base_color="#c7e4c6", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Fundo Rect.png"), pos=(400, 458),
                             text_input="FECHAR", font=get_font(45), base_color="#c7e4c6", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()