import subprocess
import pygame
import os

def start_game():
    subprocess.Popen(["python", "macross.py"])
    os._exit(0)

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Set up the Pygame window and clock
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Set the character images and dimensions
character_images = [
    pygame.image.load("./img/character1.png"),
    pygame.image.load("./img/character2.png"),
    pygame.image.load("./img/character3.png"),
    pygame.image.load("./img/character4.png"),
    pygame.image.load("./img/character5.png"),
    pygame.image.load("./img/character6.png")
]
character_width = 100
character_height = 150
character_spacing = 50

# Load the background images
bg1 = pygame.image.load('./img/background1.png').convert()
bg2 = pygame.image.load('./img/background2.png').convert()



# Load the logo image
logo_image = pygame.image.load("./img/logo.png")
logo_image = pygame.transform.scale(logo_image, (int(screen_width * 0.2), int(screen_height * 0.2)))

# Load the music file and play it
pygame.mixer.music.load("./mus/theme.wav")
pygame.mixer.music.play(-1)


# Set up the font for the character names
font = pygame.font.Font(None, 30)

# Define a function to draw the character selection screen
def draw_screen(selected_character):
    
    # Draw the logo image at the top of the screen
    logo_x = (screen_width - logo_image.get_width()) / 2
    logo_y = 50
    
    screen.blit(logo_image, (logo_x, logo_y))
    # Draw the character images and names
    # Define the character names
    character_names = [
       "Lisa",
        "Miriya",
        "Robotech",
        "Max",
        "Lynn",
        "Dana"
    ]

    character_descriptions = [
"A high-ranking officer in the RDF,\n \
Lisa is intelligent and capable, but\n \
often clashes with Rick due to their\n \
different personalities and backgrounds.\n \
She is a skilled tactician and diplomat.",
"A Zentraedi warrior who defects to the RDF,\n \
Miriya is a fierce and skilled fighter who\n \
becomes romantically involved with Max.\n \
She struggles to reconcile her loyalty to\n \
her people with her growing love for Max\n \
and her newfound respect for human culture.",
"A powerful robot created by the alien\n \
Robotech Masters, this entity seeks to gain\n \
control of the Protoculture Matrix, a\n \
source of immense power. It possesses\n \
advanced technology and formidable\n \
combat abilities.",
"A talented and ambitious pilot, Max is\n \
initially a rival to Rick but later becomes\n \
a close friend and ally. He is cool-headed\n \
and analytical, but also has a romantic side.",
"A pop singer and actress who becomes a\n \
symbol of hope and inspiration for the\n \
people of Earth, Lynn is a kind and empathetic\n \
person who uses her music to bring people\n \
together. She also becomes romantically\n \
involved with Rick, creating a love triangle\n \
with Lisa.",
"A half-human, half-Zentraedi hybrid and\n \
the daughter of Max and Miriya, Dana is\n \
a skilled fighter and leader of the 15th\n \
Squadron. She struggles to find her place\n \
in the world and reconcile her two conflicting\n \
identities."
    ]
    sc = 0
    for i, image in enumerate(character_images):
        x = (i // 2) * (character_width + character_spacing) + 50
        y = (i % 2) * (character_height + character_spacing) + 200
        # Scale the image if it is selected
        if i == selected_character:
            sc=i
            image = pygame.transform.scale(image, (100, 160))
        else:
            image = pygame.transform.scale(image, (90, 150))

        screen.blit(image, (x, y))

        # Draw the character descriptions
        desc_font = pygame.font.Font(None, 24)

        #desc_name = desc_font.render(description, True, (255, 255, 255))
        #desc_rect = desc_name.get_rect(center=(400, 330))
        #screen.blit(desc_name, desc_rect)


        # Draw the character name
        name = character_names[i]
        text_name = font.render(name, True, (255, 255, 255))
        text_rect = text_name.get_rect(center=(x+50, y+130))
        screen.blit(text_name, text_rect)

    # Update the display
    #Render each line of the text
    description = character_descriptions[sc]
    dx = 450
    dy = 300
    for line in description.splitlines():
        text = desc_font.render(line, True, (255, 255, 255))
        screen.blit(text, (dx, dy))
        dy += font.get_height()
    pygame.display.flip()

# Start with the first character selected
selected_character = 0

# Draw the initial character selection screen
draw_screen(selected_character)

bg1_x = 0
bg2_x = 0
# Main game loop
while True:
    # Scroll the background images
    bg1_x = (bg1_x - 1) % bg1.get_width()
    bg2_x = (bg2_x - 2) % bg2.get_width()
    screen.blit(bg1, (bg1_x, 0))
    screen.blit(bg1, (bg1_x - bg1.get_width(), 0))
    screen.blit(bg2, (bg2_x, 0))
    screen.blit(bg2, (bg2_x - bg2.get_width(), 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION:
            # Check if the mouse is hovering over a character
            mouse_pos = event.pos
            for i, image in enumerate(character_images):
                x = (i // 2) * (character_width + character_spacing) + 50
                y = (i % 2) * (character_height + character_spacing) + 200
                if x < mouse_pos[0] < x + character_width and y < mouse_pos[1] < y + character_height:
                    selected_character = i
                    break
            else:
                selected_character = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse was clicked on a character
            if selected_character >= 0:
                # Start the game with the selected character
                print("Starting game with character " + str(selected_character+1))
                start_game()
                pygame.quit()
                quit()

    # Draw the updated character selection screen
    draw_screen(selected_character)

    # Limit the frame rate
    clock.tick(60)