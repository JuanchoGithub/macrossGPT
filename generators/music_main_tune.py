from pydub import AudioSegment
from pydub.generators import Sine

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

# Define the envelope shape for the notes as (attack, decay, sustain, release) tuples
envelope_shape = [
    (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100),
    (10, 20, 0.3, 50), (10, 20, 0.3, 50), (25, 50, 0.6, 100), (10, 20, 0.3, 50),
    (10, 20, 0.3, 50), (25, 50, 0.6, 100), (10, 20, 0.3, 50), (10, 20, 0.3, 50),
    (50, 100, 0.6, 200), (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100),
    (25, 50, 0.6, 100), (25, 50, 0.6, 100), (10, 20, 0.3, 50), (10, 20, 0.3, 50),
    (50, 100, 0.6, 200), (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100),
    (25, 50, 0.6, 100), (25, 50, 0.6, 100), (10, 20, 0.3, 50), (10, 20, 0.3, 50),
    (50, 100, 0.6, 200), (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100),
    (25, 50, 0.6, 100), (25, 50, 0.6, 100), (10, 20, 0.3, 50), (10, 20, 0.3, 50),
    (50, 100, 0.6, 200), (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100),
    (25, 50, 0.6, 100), (25, 50, 0.6, 100), (10, 20, 0.3, 50), (10, 20, 0.3, 50),
    (50, 100, 0.6, 200), (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100),
    (25, 50, 0.6, 100), (25, 50, 0.6, 100), (10, 20, 0.3, 50), (10, 20, 0.3, 50),
    (50, 100, 0.6, 200), (25, 50, 0.6, 100), (25, 50, 0.6, 100), (25, 50, 0.6, 100),
    (25, 50, 0.6, 100), (25, 50, 0.6, 100), (10, 20, 0.3, 50), (10, 20, 0.3, 50),
    (50, 100, 0.6, 200)]

#Define the tempo of the music as the number of beats per minute (BPM)
tempo = 120

#Define the length of each beat as the duration of a quarter note (in milliseconds)
beat_length = 60 / tempo * 1000

#Create an empty audio segment to hold the final music
music = AudioSegment.empty()

#Loop through each note in the melody and create an audio segment for it
for note, envelope in zip(melody_notes, envelope_shape):
# Create a sine wave with the given frequency and duration
    sine_wave = Sine(note[0]).to_audio_segment(duration=note[1])

# Apply an envelope to the sine wave using the attack, decay, sustain, and [release times](poe://www.poe.com/_api/key_phrase?phrase=release%20times&prompt=Tell%20me%20more%20about%20release%20times.)
envelope_shape = [0, envelope[0], envelope[1], envelope[2], envelope[3]]
envelope_segment = AudioSegment.silent(duration=note[1])
for i in range(len(envelope_shape) - 1):
    start = int(envelope_shape[i] * note[1] / 1000)
    end = int(envelope_shape[i+1] * note[1] / 1000)
    envelope_segment = envelope_segment.overlay(sine_wave[start:end].fade_in(envelope[0]).fade_out(envelope[3]), position=start)

# Add the envelope-shaped note to the music
music += envelope_segment
#Export the music as an MP3 file
music.export("robotech_main_theme_generated.wav", format="wav")

