import pygame
import sys

#Initializing the pygame
pygame.init()

#Setting up the window dimentions, font size and color.
title_bar = "Spiderman: Code to Home"
WIN_WIDTH = 900
WIN_HEIGHT = 500
very_small_font = pygame.font.SysFont("comicsans", 20)
small_font = pygame.font.SysFont("comicsans", 25)
medium_font = pygame.font.SysFont("comicsans", 30)
medium2_font = pygame.font.SysFont("arial", 27)
large_font = pygame.font.SysFont("comicsans", 40)
very_large_font = pygame.font.SysFont("arial", 50)

fonts_dict = {"v_small": very_small_font,"small":small_font, "medium":medium_font, "medium2":medium2_font ,"large":large_font, "v_large":very_large_font}

#Loading up all the images used
IMAGE_HOME = pygame.image.load('homef.png')
IMAGE_PINK = pygame.image.load('pink.png')
IMAGE_ORANGE = pygame.image.load('orange.png')
IMAGE_YELLOW = pygame.image.load('yellow.png')
IMAGE_DOC = pygame.image.load('DC.png')
IMAGE_SPIDEY = pygame.image.load('MC.png')
MENU_IMG = pygame.image.load('main_menu.png')
END_SCREEN_IMG = pygame.image.load('end_screen.png')

blocks_type_dict = {'pink': IMAGE_PINK, 'orange':IMAGE_ORANGE, 'yellow':IMAGE_YELLOW, 'home':IMAGE_HOME, 'villan':IMAGE_DOC}

#Initialize the screen
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(title_bar)


#Constants
BLOCK_SIZE = 50
FONT_COLOR = (255,255,255)
BG_COLOR = (6, 40, 70)
CHAR_COLOR = (255, 0, 0)
MM_FONT_COLOR = (255,36,36)
DELAY_TIME = 400
done = False
executed = False
first_letter_typed = True
stage_selected = False
keys_pressed = []
lines = []


#Ans Key for each stages
for_lines = ['for steps in range(13):', '\tif block==yellow:', '\t\tforward()', '\telif block==pink:', '\t\tright()', '\telif block==villan:', '\t\tjump()', '\tsteps=steps+1']
for_char_render = ["down", "down", "down", "down", "down", "jump_l", "left","up","up","up","up","up"]

while_lines = ['while steps<8:', '\tif block==yellow:', '\t\tforward()', '\telif block==orange:', '\t\tleft()', '\telif block==pink:', '\t\tright()', '\telif block==villan:', '\t\tjump()', '\tsteps=steps+1']
while_char_render = ["right", "right", "up", "jump_r", "down", "right", "right"]

if_else_lines = ['if block==yellow:', '\tforward()', 'elif block==orange:', '\tleft()', 'elif block==pink:', '\tright()']
if_else_char_render = ["left", "left", "left", "down", "down", "right", "right", "down","down","left","left","left"]


#Seed
#Uncomment the below 2 lines, if stages not rendered at centre
#CODE_X = 603
#CODE_Y = 61

CODE_X_SPACING = 10
CODE_Y_SPACING = 30
FONT_CORR = 3

score = 0

def blocks_render(block_x, block_y, next_block, block_type):
    """
    Arguments: block_x, block_y - Previous x and y co-ordinates of the block
               next_block - Where the next block should be placed
               block_type - The color of the block
               
    Returns: bloc_x, block_y - Current block co-ordinates
    """
    if block_type in blocks_type_dict:
        block_image = blocks_type_dict[block_type]
    
    else:
        print("Specified Image Not Found***")
        
    if next_block == "up":
        block_y -= BLOCK_SIZE            
        
    elif next_block == "down":
        block_y += BLOCK_SIZE
        
    elif next_block == "right":
        block_x += BLOCK_SIZE
        
    elif next_block == "left":
        block_x -= BLOCK_SIZE
        
    WIN.blit(block_image, (block_x, block_y))
    pygame.display.update()
    
    #print("Blocks x,y co-ordinates: ",block_x, block_y)
    return block_x, block_y

def while_stage_render():
    """
    Renders the while stage
    """
    
    block_x, block_y = blocks_render(BLOCK_X, BLOCK_Y, "right", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "right", "orange")
    block_x, block_y = blocks_render(block_x, block_y, "up", "pink")
    block_x, block_y = blocks_render(block_x, block_y, "right", "villan")
    block_x, block_y = blocks_render(block_x, block_y, "right", "pink")
    block_x, block_y = blocks_render(block_x, block_y, "down", "orange")
    block_x, block_y = blocks_render(block_x, block_y, "right", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "right", "home")


def if_else_stage_render():
    """
    Renders the if else stage
    """
    
    block_x, block_y = blocks_render(BLOCK_X, BLOCK_Y, "left", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "left", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "left", "orange")
    block_x, block_y = blocks_render(block_x, block_y, "down", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "down", "orange")
    block_x, block_y = blocks_render(block_x, block_y, "right", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "right", "pink")
    block_x, block_y = blocks_render(block_x, block_y, "down", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "down", "pink")
    block_x, block_y = blocks_render(block_x, block_y, "left", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "left", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "left", "home")

def for_stage_render():
    """
    Renders For Stage
    """
    
    block_x, block_y = blocks_render(BLOCK_X, BLOCK_Y, "down", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "down", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "down", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "down", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "down", "pink")
    block_x, block_y = blocks_render(block_x, block_y, "left", "villan")
    block_x, block_y = blocks_render(block_x, block_y, "left", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "left", "pink")
    block_x, block_y = blocks_render(block_x, block_y, "up", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "up", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "up", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "up", "yellow")
    block_x, block_y = blocks_render(block_x, block_y, "up", "home")


def while_keypoints(executed, score):
    """
    Renders the To Do list of the given stage, and after 
    execution removes, the stuff done correctly form To Do list
    Arguments: executed - If the user entered code is executed
               score - How many lines matched the ans key
    """
    thickness1 = thickness2 = thickness3 = 1
    if executed:
         if score >= 1:
            thickness1 = 0
        
         if score > 1 and score < 7:
             thickness2 = 0
         
         if score > 7:
             thickness2 = 0
        
    pygame.draw.rect(WIN, FONT_COLOR, (0,0,150,75),1)
    texts("To Do !", 6,40, "large")
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,75,150,75),thickness1)
    texts("While Loop", 10, 125, "small")
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,150,150,75),thickness2)
    texts("if statements", 10, 200, "small")
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,225,150,75),thickness3)
    texts("steps increment", 10, 275, "small")

       
def if_else_keypoints(executed, score):
    """
    Renders the To Do list of the given stage, and after 
    execution removes, the stuff done correctly form To Do list
    Arguments: executed - If the user entered code is executed
               score - How many lines matched the ans key
    """
    thickness1 = thickness2 = thickness3 = 1
    if executed:
         if score >= 1:
            thickness1 = 0
        
         if score > 1 and score < 5:
             thickness2 = 0
         
         if score >= 5:
             thickness2 = 0  
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,0,150,75),1)
    texts("To Do !", 6,40, "large")

    pygame.draw.rect(WIN, FONT_COLOR, (0,75,150,75),thickness1)
    texts("If statement", 10, 125, "small")
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,150,150,75),thickness2)
    texts("elif statements", 10, 200, "small")
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,225,150,75),thickness3)
    texts("steps increment", 10, 275, "small")    
    
def for_keypoints(executed, score):
    """
    Renders the To Do list of the given stage, and after 
    execution removes, the stuff done correctly form To Do list
    Arguments: executed - If the user entered code is executed
               score - How many lines matched the ans key
    """
    thickness1 = thickness2 = thickness3 = 1
    if executed:
         if score >= 1:
            thickness1 = 0
        
         if score > 1 and score < 7:
             thickness2 = 0
         
         if score > 7:
             thickness2 = 0
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,0,150,75),1)
    texts("To Do !", 6,40, "large")

    pygame.draw.rect(WIN, FONT_COLOR, (0,75,150,75),thickness1)
    texts("Range correct", 10, 125, "small")
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,150,150,75),thickness2)
    texts("if/elif statements", 5, 200, "small")
    
    pygame.draw.rect(WIN, FONT_COLOR, (0,225,150,75),thickness3)
    texts("steps increment", 10, 275, "small") 
    


def pre_char_render(ans_char_render):
    """
    Does the calculations, for where the character will move
    Arguments: ans_key_char - Ans key of the given stage
    """
    
    char_x, char_y = CHAR_X, CHAR_Y
    for pt in ans_char_render:
        if pt == 'right':
            char_x += BLOCK_SIZE
            stage_character_render(char_x, char_y, stage)
            pygame.time.delay(DELAY_TIME)
            
        if pt =='left':
            char_x -= BLOCK_SIZE
            stage_character_render(char_x, char_y, stage)
            pygame.time.delay(DELAY_TIME)
            
        if pt == 'up':
            char_y -= BLOCK_SIZE
            stage_character_render(char_x, char_y, stage)
            pygame.time.delay(DELAY_TIME)
        
        if pt == 'down':
            char_y += BLOCK_SIZE
            stage_character_render(char_x, char_y, stage)
            pygame.time.delay(DELAY_TIME)
            
        if pt == 'jump_r':
            char_x += BLOCK_SIZE*2
            stage_character_render(char_x, char_y, stage)
            pygame.time.delay(DELAY_TIME)
            
        if pt == 'jump_l':
            char_x -= BLOCK_SIZE*2
            stage_character_render(char_x, char_y, stage)
            pygame.time.delay(DELAY_TIME)
            

def special_characters():
       """
       Renders the special symbols on screen
       Returns: The rectangle object, which can
                be used to detect the mouse click
       """
        
       colon = pygame.draw.rect(WIN, FONT_COLOR, (600, 440, 100, 30), 1)
       texts(":", 650, 445, "small")
       less_than = pygame.draw.rect(WIN, FONT_COLOR, (700,440,100,30),1)
       texts("<", 750, 445, "small")
       plus = pygame.draw.rect(WIN, FONT_COLOR, (800,440,100,30),1)
       texts("+", 847, 445, "small")
       
       equal_to = pygame.draw.rect(WIN, FONT_COLOR, (600, 470, 100,30), 1)
       texts("=", 650, 475, "small")
       open_paren = pygame.draw.rect(WIN, FONT_COLOR, (700,470,100,30), 1)
       texts("(", 750,475,"small")
       close_paren = pygame.draw.rect(WIN, FONT_COLOR, (800,470,100,30),1)
       texts(")", 850,475,"small")
       return colon, less_than, plus, equal_to, open_paren, close_paren
       
       
def chars_to_line(keys_pressed):
    """
    Used to convert the input characters, into a string
    Arguments: keys_pressed - List of keys pressed
    Returns: line - converted list of character, into a single line
    """
    line = ''
    for key in keys_pressed:
        line += key

    return line


def texts(text, x,y, font_size):
    """
    Used to display the font anywhere on the screen
    Arguments: text - Text to display
               x,y - Co-ordinates of the text
               font_size - size to be used
    """
    
   if font_size in fonts_dict:
       current_font = fonts_dict[font_size]
       text_print = current_font.render(text, True, FONT_COLOR)
       WIN.blit(text_print, [x,y])
       pygame.display.update()
       
   else:
       print("Specified Font Not Found***")
       
       
def main_menu(stage_selected):
    """
    Used to render the main menu
    Arguments: stage_selected - Checks if the stage is already selected
    Returns: stage - string containing the name of the stage
    """
    print("__MAIN MENU__")
    WIN.blit(MENU_IMG, (0,0))
    pygame.display.update()
    for_loop = pygame.draw.rect(WIN, MM_FONT_COLOR, (610,230,250,60), 1)
    if_else = pygame.draw.rect(WIN, MM_FONT_COLOR, (610, 300, 250, 60), 1)
    while_stage = pygame.draw.rect(WIN, MM_FONT_COLOR, (610, 370, 250, 60), 1)
    credit = pygame.draw.rect(WIN, MM_FONT_COLOR, (825, 483, 250, 60), 1)
    
    while not stage_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                stage_selected = True
                print("// TERMINATING THE EXECUTION //")
                pygame.quit()
                sys.exit()
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                x,y = event.pos
                print("Mouse Clicked: ",x,y)
                
                if for_loop.collidepoint(x,y):
                    print("// FOR LOOP STAGE SELECTED //")
                    stage_selected = True
                    return "stage_for"
                
                elif if_else.collidepoint(x,y):
                    print("// IF ELSE STAGE SELECTED //")
                    stage_selected = True
                    return "stage_if_else"
                
                elif while_stage.collidepoint(x,y):
                    print("// WHILE STAGE SELECTED //")
                    stage_selected = True
                    return "stage_while"
                
                elif credit.collidepoint(x,y):
                    print("// CREDITS SELECTED //")
                    #Temporary, add func to display credits in
                    #full screen later
                    return "credits"
 
def stage_character_render(char_x, char_y, stage):
    """
    Used to render the character and the  stage
    Arguments: char_x, char_y - X and Y coordinates of character
    Returns: colon, less_than, plus, equal_to, open_paren, 
             close_paren - Rectangle objects of these symbols 
             to detect if it's clicked by mouse
    """
    
    #Fill the screen 
    WIN.fill(BG_COLOR)
    
    #Render the stage
    if stage == "stage_while":
        while_stage_render()
        
    elif stage == "stage_for":
        for_stage_render()
        
    elif stage == "stage_if_else":
        if_else_stage_render()
        
    else:
        print("__STAGE NOT FOUND__")
        print("__TRYING FORCE QUIT__")
        pygame.time.delay(DELAY_TIME)
        print("// TERMINATING THE EXECUTION //")
        pygame.quit()
        sys.exit()
    
    #Draw the lines
    #Verical Line
    pygame.draw.lines(WIN, FONT_COLOR, False, [(600, 0), (600, 500)], 1)
    
    #Horizontal Line
    pygame.draw.lines(WIN, FONT_COLOR, False, [(600, 60), (900, 60)], 1)
    #texts("Press ENTER before Running", 601, 420, "small")
    
    #Put the font
    texts("Write your program", 605, 25, "medium")
    
    texts("RIGHT SHIFT - To Run", 10, 320, "v_small")
    texts("Functions and Keywords", 10,380,"small")
    texts("right() | left()", 10, 410, "v_small")
    texts("forward() | jump()", 10, 440, "v_small")
    texts("steps | block | yellow | orange | pink | villan", 10, 470, "v_small")
    
    colon, less_than, plus, equal_to, open_paren, close_paren = special_characters()
    
    #Render the keypoints accordingly
    if stage == "stage_while":
        while_keypoints(executed, None)
        
    elif stage == "stage_for":
        for_keypoints(executed, None)
        
    elif stage == "stage_if_else":
        if_else_keypoints(executed, None)
    
    WIN.blit(IMAGE_SPIDEY, (char_x, char_y))
    pygame.display.update()
    
    return colon, less_than, plus, equal_to, open_paren, close_paren
 
        
#Main Execution starts from here
stage = main_menu(stage_selected)

if stage == 'stage_while':
    #Initialize variables for this stage
    pygame.display.set_caption("WHILE STAGE")
    print("__WHILE STAGE__")
    BLOCK_X = 200
    BLOCK_Y = 200
    
    CHAR_X = 200
    CHAR_Y = 200
    
    ans_lines = while_lines
    ans_char_render = while_char_render
    
elif stage == 'stage_for':
    #Initialize variables for this stage
    pygame.display.set_caption("FOR STAGE")
    print("__FOR STAGE__")
    BLOCK_X = 450
    BLOCK_Y = 75
    
    CHAR_X = 450
    CHAR_Y = 75  
    
    ans_lines = for_lines
    ans_char_render = for_char_render
    
elif stage == 'stage_if_else':
    #Initialize variables for this stage
    pygame.display.set_caption("IF ELSE STAGE")
    print("__IF ELSE STAGE__")
    BLOCK_X = 450
    BLOCK_Y = 100
    
    CHAR_X = 450
    CHAR_Y = 100
    
    ans_lines = if_else_lines
    ans_char_render = if_else_char_render
    
elif stage == 'credits':
    #Display the credits
    pygame.display.set_caption("CREDITS")
    WIN.blit(END_SCREEN_IMG, (0,0))
    texts("Made with love by:", 430, 125, "v_large")
    texts("Shubham Mukherjee", 430, 250, "medium2")
    texts("Purvesh Bane", 430, 300, "medium2")
    texts("Harsh Chandorkar", 430, 350, "medium2")
    texts("Darshan Dodia", 430, 400, "medium2")
    texts("Stay Hungy, Stay Foolish !", 730, 475, "v_small")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("// TERMINATING THE EXECUTION //")
                pygame.quit()
                sys.exit()

colon, less_than, plus, equal_to, open_paren, close_paren = stage_character_render(CHAR_X, CHAR_Y, stage)
# =============================================================================
# For Testing Purposes
# ans_lines =['a','b','c']
# print("\nAns to this stage: ",ans_lines)
# =============================================================================


#Main Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        #Check where mouse is clicked and act accordingly
        if event.type == pygame.MOUSEBUTTONDOWN :
            x,y = event.pos
            print("Mouse Clicked: ",x,y)
            if first_letter_typed:
                code_x, code_y = CODE_X, CODE_Y
                first_letter_typed = False
            
            if colon.collidepoint(x,y):
                print('Console ip: colon')
                keys_pressed.append(':')
                texts(':', code_x, code_y, "small")
                code_x += CODE_X_SPACING
                
            if less_than.collidepoint(x,y):
                print('Console ip: less than')
                keys_pressed.append('<')
                texts('<', code_x, code_y, "small")
                code_x += CODE_X_SPACING
                
            if plus.collidepoint(x,y):
                print('Console ip: plus')
                keys_pressed.append('+')
                texts('+', code_x, code_y, "small")
                code_x += CODE_X_SPACING  
                
            if equal_to.collidepoint(x,y):
                print('Console ip: equal')
                keys_pressed.append('=')
                texts('=', code_x, code_y, "small")
                code_x += CODE_X_SPACING

            if open_paren.collidepoint(x,y):
                print('Console ip: open paren')
                keys_pressed.append('(')
                texts('(', code_x, code_y, "small")
                code_x += CODE_X_SPACING

            if close_paren.collidepoint(x,y):
                print('Console ip: close paren')
                keys_pressed.append(')')
                texts(')', code_x, code_y, "small")
                code_x += CODE_X_SPACING
                
            else:
                pass
          
        #Check which keys are pressed
        if event.type == pygame.KEYDOWN:
            
            #Check if it is the first letter that is typed
            if first_letter_typed:
                
                code_x = CODE_X
                code_y = CODE_Y
                first_letter_typed =  False
            
            if not executed:
                            
                if event.key == pygame.K_a:
                     print("Console ip: A")
                     keys_pressed.append('a')
                     texts('a', code_x, code_y, "small")
                     code_x += CODE_X_SPACING
                     
                     
                elif event.key == pygame.K_b:
                     print("Console ip: B")
                     keys_pressed.append('b')
                     texts('b', code_x, code_y, "small")
                     code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_c:
                     print("Console ip: C")
                     keys_pressed.append('c')
                     texts('c', code_x, code_y, "small")
                     code_x += CODE_X_SPACING
                
                elif event.key == pygame.K_d:
                     print("Console ip: D")
                     keys_pressed.append('d')
                     texts('d', code_x, code_y, "small")
                     code_x += CODE_X_SPACING

                elif event.key == pygame.K_e:
                     print("Console ip: E")
                     keys_pressed.append('e')
                     texts('e', code_x, code_y, "small")
                     code_x += CODE_X_SPACING

                elif event.key == pygame.K_f:
                     print("Console ip: F")
                     keys_pressed.append('f')
                     texts('f', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING - FONT_CORR)
 

                elif event.key == pygame.K_g:
                     print("Console ip: G")
                     keys_pressed.append('g')
                     texts('g', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_h:
                     print("Console ip: H")
                     keys_pressed.append('h')
                     texts('h', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_i:
                     print("Console ip: I")
                     keys_pressed.append('i')
                     texts('i', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING - FONT_CORR)


                elif event.key == pygame.K_j:
                     print("Console ip: J")
                     keys_pressed.append('j')
                     texts('j', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING - FONT_CORR)


                elif event.key == pygame.K_k:
                     print("Console ip: K")
                     keys_pressed.append('k')
                     texts('k', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_l:
                     print("Console ip: L")
                     keys_pressed.append('l')
                     texts('l', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING - FONT_CORR)

                elif event.key == pygame.K_m:
                     print("Console ip: M")
                     keys_pressed.append('m')
                     texts('m', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING + FONT_CORR)


                elif event.key == pygame.K_n:
                     print("Console ip: N")
                     keys_pressed.append('n')
                     texts('n', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_o:
                     print("Console ip: O")
                     keys_pressed.append('o')
                     texts('o', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_p:
                     print("Console ip: P")
                     keys_pressed.append('p')
                     texts('p', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_q:
                     print("Console ip: Q")
                     keys_pressed.append('q')
                     texts('q', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_r:
                     print("Console ip: R")
                     keys_pressed.append('r')
                     texts('r', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING - FONT_CORR)


                elif event.key == pygame.K_s:
                     print("Console ip: S")
                     keys_pressed.append('s')
                     texts('s', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_t:
                     print("Console ip: T")
                     keys_pressed.append('t')
                     texts('t', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING - FONT_CORR)


                elif event.key == pygame.K_u:
                     print("Console ip: U")
                     keys_pressed.append('u')
                     texts('u', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_v:
                     print("Console ip: V")
                     keys_pressed.append('v')
                     texts('v', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_w:
                     print("Console ip: W")
                     keys_pressed.append('w')
                     texts('w', code_x, code_y, "small")
                     code_x += (CODE_X_SPACING + FONT_CORR)


                elif event.key == pygame.K_x:
                     print("Console ip: X")
                     keys_pressed.append('x')
                     texts('x', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_y:
                     print("Console ip: Y")
                     keys_pressed.append('y')
                     texts('y', code_x, code_y, "small")
                     code_x += CODE_X_SPACING


                elif event.key == pygame.K_z:
                     print("Console ip: z")
                     keys_pressed.append('z')
                     texts('z', code_x, code_y, "small")
                     code_x += CODE_X_SPACING
                
                elif event.key == pygame.K_0:
                    print("Console ip: 0")
                    keys_pressed.append("0")
                    texts('0', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_1:
                    print("Console ip: 1")
                    keys_pressed.append("1")
                    texts('1', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_2:
                    print("Console ip: 2")
                    keys_pressed.append("2")
                    texts('2', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_3:
                    print("Console ip: 3")
                    keys_pressed.append("3")
                    texts('3', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_4:
                    print("Console ip: 4")
                    keys_pressed.append("4")
                    texts('4', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_5:
                    print("Console ip: 5")
                    keys_pressed.append("5")
                    texts('5', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_6:
                    print("Console ip: 6")
                    keys_pressed.append("6")
                    texts('6', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_7:
                    print("Console ip: 7")
                    keys_pressed.append("7")
                    texts('7', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_8:
                    print("Console ip: 8")
                    keys_pressed.append("8")
                    texts('8', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_9:
                    print("Console ip: 9")
                    keys_pressed.append("9")
                    texts('9', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_PLUS:
                    print("Console ip: +")
                    keys_pressed.append("+")
                    texts('+', code_x, code_y, "small")
                    code_x += CODE_X_SPACING
                    
                elif event.key == pygame.K_TAB:
                     print("Console ip: TAB")
                     keys_pressed.append('\t')
                     texts('    ', code_x, code_y, "small")
                     code_x += CODE_X_SPACING
               
                elif event.key == pygame.K_RETURN:
                     print("Console ip: RETURN")
                     code_y += CODE_Y_SPACING
                     code_x = CODE_X
                     
                     line = chars_to_line(keys_pressed)
                     lines.append(line)
                     keys_pressed = []
                     
                elif event.key == pygame.K_SPACE:
                     print("Console ip: SPACE")
                     keys_pressed.append(" ")
                     texts(' ', code_x, code_y, "small")
                     code_x += CODE_X_SPACING
                     
                     
                elif event.key == pygame.K_BACKSPACE:
                    if code_x > 607:   
                        print("Console ip: backspace")
                        code_x -= CODE_X_SPACING
                        backspace_rect = pygame.draw.rect(WIN, BG_COLOR, (code_x, code_y, 25, 25), 0)
                        pygame.display.update(backspace_rect)
                        keys_pressed.pop(-1)
                        
                
                elif event.key ==  pygame.K_RSHIFT:
                    print("Console ip: R SHIFT")
                    print("__EXECUTING PROGRAM__")
                    
                    #Condition to check if they won
                    if lines == ans_lines:
                        print("...Player Won...")
                        pre_char_render(ans_char_render)
                        WIN.blit(END_SCREEN_IMG, (0,0))
                        texts("YOU WON !", 400, 175, "v_large")
                        texts("Remember, with great power comes great responsibilites !", 320,450, "medium2")
                        
                    else:
                        print("...Player Lost...")
                        texts("YOU LOST", 605, 360, "large")
                        
                        for line, a_line in zip(lines, ans_lines):
                            if line == a_line:
                                score+=1
                                
                        sentence = str(score) + " out of " + str(len(ans_lines)) + " lines were correct"
                        texts(sentence, 606, 400, "small")
                        
                        executed = True
                        if stage == "stage_while":
                            while_keypoints(executed, score)
                            
                        elif stage == "stage_for":
                            for_keypoints(executed, score)
                            
                        elif stage == "stage_if_else":
                            if_else_keypoints(executed, score)
                           
    
pygame.quit() 
