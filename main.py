import subprocess
import pygame

def start_game():
    subprocess.Popen(["python", "macross .py"])
    os._exit(0)

# Initialize Pygame
pygame.init()

# Set up the window and caption
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('My Game')

# Load the background images
bg1 = pygame.image.load('./img/background1.png').convert()
bg2 = pygame.image.load('./img/background2.png').convert()

# Load the logo image
logo_load = pygame.image.load('./img/logo.png').convert_alpha()
logo_size = (int(window.get_width() * 2/3), int(window.get_height() * 2/3))
logo = pygame.transform.scale(logo_load, logo_size)
logo_rect = logo.get_rect()
logo_rect.center = (window_size[0] // 2, window_size[1] // 2 - 100)

# Load the font for the menu options and copyright text
font = pygame.font.Font(None, 48)

# Create the menu options
new_game_text = font.render('NEW GAME', True, (255, 255, 255))
new_game_rect = new_game_text.get_rect()
new_game_rect.center = (window_size[0] // 2, window_size[1] // 2 + 120)

quit_game_text = font.render('QUIT GAME', True, (255, 255, 255))
quit_game_rect = quit_game_text.get_rect()
quit_game_rect.center = (window_size[0] // 2, window_size[1] // 2 + 170)

# Create the copyright text
copyright_text = font.render('copyright Truchisoft LLC - made with AI',
                              True, (255, 255, 255))
copyright_rect = copyright_text.get_rect()
copyright_rect.bottomright = (window_size[0] - 10, window_size[1] - 10)

# Load the music and play it
# Load the MIDI file
pygame.mixer.music.load("./mus/theme.wav")
# Play the MIDI file
pygame.mixer.music.play()

# Set up the clock for the game loop
clock = pygame.time.Clock()

bg1_x = 0
bg2_x = 0
# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the menu options
            if new_game_rect.collidepoint(event.pos):
                print('Starting new game')
                start_game()
            elif quit_game_rect.collidepoint(event.pos):
                pygame.quit()
                quit()

    # Scroll the background images
    bg1_x = (bg1_x - 1) % bg1.get_width()
    bg2_x = (bg2_x - 2) % bg2.get_width()
    window.blit(bg1, (bg1_x, 0))
    window.blit(bg1, (bg1_x - bg1.get_width(), 0))
    window.blit(bg2, (bg2_x, 0))
    window.blit(bg2, (bg2_x - bg2.get_width(), 0))

    # Draw the logo and menu options
    window.blit(logo, logo_rect)
    window.blit(new_game_text, new_game_rect)
    window.blit(quit_game_text, quit_game_rect)

    # Draw the copyright text
    window.blit(copyright_text, copyright_rect)

    # Update the display and limit the frame rate
    pygame.display.flip()
    clock.tick(60)