import pygame
import numpy as np

# Define the notes of the melody as (frequency, duration) pairs
melody_notes = [
    (440, 500), (587.33, 500), (698.46, 500), (783.99, 500),
    (698.46, 250), (783.99, 250), (880, 500), (783.99, 250),
    (880, 250), (987.77, 500), (880, 250), (987.77, 250),
    (1046.5, 1000), (783.99, 500), (880, 500), (783.99, 500),
    (880, 500), (987.77, 500), (880, 250), (987.77, 250),
    (1046.5, 1000), (783.99, 500), (880, 500), (783.99, 500),
    (880, 500), (987.77, 500), (880, 250), (987.77, 250),
    (1046.5, 1000), (783.99, 500), (880, 500), (783.99, 500),
    (880, 500), (987.77, 500), (880, 250), (987.77, 250),
    (1046.5, 1000), (783.99, 500), (880, 500), (783.99, 500),
    (880, 500), (987.77, 500), (880, 250), (987.77, 250),
    (1046.5, 1000), (783.99, 500), (880, 500), (783.99, 500),
    (880, 500), (987.77, 500), (880, 250), (987.77, 250),
    (1046.5, 1000)
]

# Define the tempo of the music as the number of beats per minute (BPM)
tempo = 120

# Define the length of each beat as the duration of a quarter note (in milliseconds)
beat_length = 60 / tempo * 1000

# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# Loop through each note in the melody and generate a sound for it
for note in melody_notes:
    # Calculate the length of the note in milliseconds based on the tempo
    note_length = note[1] / beat_length
    
    # Generate a sine wave with the given frequency and duration
    num_samples = int(44100 * note_length)
    sine_wave = np.sin(2 * np.pi * note[0] * np.arange(num_samples) / 44100).astype(np.float32)

    # Scale the amplitude of the waveform to lower the volume
    sine_wave *= 0.1

    # Reshape the waveform into a 2-dimensional array
    sine_wave = np.reshape(sine_wave, (num_samples, 1))

    # Make a sound from the sine wave and play it
    pygame.mixer.Sound(sine_wave).play()
    pygame.time.wait(int(beat_length * 0.9))

# Quit pygame and the mixer
pygame.mixer.quit()
pygame.quit()