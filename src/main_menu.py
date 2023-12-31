import pygame 
import button
from game_test import Game
import math

class Menu():
    def __init__(self, screen, screen_height, screen_width): #add new variable here
        pygame.display.init()
        screen_height = 1080
        screen_width = 1920
        self.screen = screen
        self.game_paused = False
        self.menu_state = "main_menu"
        self.game_state = "game"
        pygame.font.init() #initialize font module
        self.font = pygame.font.SysFont("arial", 40)
        self.TEXT_COL = (0, 0, 0)
        #Insert Character Variable
        self.character_selection = [
            button.Button(400, 600, pygame.image.load('src/img/Bird_1.png').convert_alpha(), 1, selected_frame_index=0),
            button.Button(400, 800, pygame.image.load('src/img/Bird_2.png').convert_alpha(), 1),
            button.Button(400, 1000, pygame.image.load('src/img/Bird_3.png').convert_alpha(), 1),
        ]

        #load button images
        start_img = pygame.image.load('src/img/PH_start_button.png').convert_alpha()
        exit_img = pygame.image.load('src/img/PHexit_button.png').convert_alpha()
        selection_img = pygame.image.load('src/img/selection_button.png').convert_alpha()
        video_img = pygame.image.load('src/img/video_ph.png').convert_alpha()
        backmenu_img = pygame.image.load('src/img/back_menu.png').convert_alpha()

        #load bg image
        self.og_bg_img = pygame.image.load("src/img/MenuBackground.png").convert()
        self.bg_width = self.og_bg_img.get_width()
        self.scroll = 0
        self.tiles = math.ceil(screen_width / self.bg_width) + 2

        #Create button instance
        self.start_button = button.Button(860, 370, start_img, 1)
        self.end_button = button.Button(860, 700, exit_img, 1)
        self.selection_button = button.Button(860, 570, selection_img, 1)
        self.backmenu_button = button.Button(304, 680, backmenu_img, 1) 
 
    def draw_text(self, text, x, y):
        img = self.font.render(text, True, self.TEXT_COL)
        self.screen.blit(img, (x, y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_paused = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def run(self):
            #Game loop 
            run = True
            while run:
                #Fill the screen
                self.screen.fill((11,241,255))
                #Draw bg img and change dimension
                for i in range(0, self.tiles):
                    self.screen.blit(self.og_bg_img, (i * self.bg_width + self.scroll, 0))
                #Scroll background
                self.scroll -= 1.5
                #Reset scroll
                if abs(self.scroll) > self.bg_width:
                    self.scroll = 0

        #Check if game is paused
                if self.game_paused:
                    #check menu_state
                    if self.menu_state == "main_menu":
                        #draw pause screen buttons
                        if self.start_button.draw(self.screen):
                            self.game_paused = False
                            game = Game(1920, 1080) #Create a Game instance
                            game.run()
                        if self.selection_button.draw(self.screen):
                            self.menu_state = "selection"
                        if self.end_button.draw(self.screen):
                            run = False
                #check if the selection menu is open
                if self.menu_state == "selection":
                #draw different option buttons in the screen
                    for char_button in self.character_selection:
                        if char_button.draw(self.screen):

                            self.selected_character = char_button
                            print(f"selected character: {self.selected_character}")

                    if self.backmenu_button.draw(self.screen):
                        self.menu_state = "main_menu"  
                #check if the selection screen is open
                if self.menu_state == "selection":
                    #draw other buttons for selection screen
                    if self.backmenu_button.draw(self.screen):
                        self.menu_state = "main_menu"
                else: 
                    self.draw_text("Press Space to Play", 800, 540) #Welcome Text Dimension

                self.handle_events()
                pygame.display.update()

if __name__== "__main__":
    #Create a display window
    pygame.init()
    screen_height = 1920
    screen_width = 1080

    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption("Main Menu")

    character_selection_buttons = [
            button.Button(400, 600, pygame.image.load('src/img/Bird_1.png').convert_alpha(), 1),
            button.Button(400, 800, pygame.image.load('src/img/Bird_2.png').convert_alpha(), 1),
            button.Button(400, 1000, pygame.image.load('src/img/Bird_3.png').convert_alpha(), 1),
        ]

    menu = Menu(screen, screen_height, screen_height)
    menu.character_selection = character_selection_buttons
    menu.run()

    pygame.quit()