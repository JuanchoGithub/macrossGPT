import pygame

# Initialize Pygame
pygame.init()

# Load the MIDI file
pygame.mixer.music.load("./mus/main_theme.mid")

# Set the volume for the MIDI file
volume = 0.5 # half volume
pygame.mixer.music.set_volume(volume)

# Play the MIDI file
pygame.mixer.music.play()

# Wait for the MIDI file to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)

# Clean up Pygame
pygame.quit()