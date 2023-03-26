import pyaudio
import pychord
import time
import numpy as np

# Define the chords and their durations in milliseconds
chords = [
    ("G", 500),
    ("D", 500),
    ("Em", 500),
    ("C", 500),
    ("G", 500),
    ("D", 500),
    ("Em", 500),
    ("C", 500),
    ("Am", 500),
    ("D", 500),
    ("G", 500),
    ("Am", 500),
    ("D", 500),
    ("G", 500),
    ("C", 500),
    ("D", 500),
    ("G", 500),
    ("C", 500),
    ("D", 500),
    ("G", 500),
    ("C", 500),
    ("D", 500),
    ("G", 500)
]

# Define the mapping of note names to frequencies
note_freqs = {
    "C": 261.63,
    "C#": 277.18,
    "D": 293.66,
    "D#": 311.13,
    "E": 329.63,
    "F": 349.23,
    "F#": 369.99,
    "G": 392.00,
    "G#": 415.30,
    "A": 440.00,
    "A#": 466.16,
    "B": 493.88
}

# Generate the audio signals for each chord
chord_sounds = []
for chord, duration in chords:
    chord_notes = pychord.Chord(chord).components()
    chord_signal = np.zeros(int(duration * 44100 / 1000), dtype=np.float32)
    for note in chord_notes:
        note_signal = np.sin(2 * np.pi * note_freqs[note] * np.arange(len(chord_signal)) / 44100)
        chord_signal += note_signal
    chord_signal /= np.max(np.abs(chord_signal)) # Normalize the signal
    chord_sounds.append(chord_signal)

# Calculate the time between each beat in seconds
beat_time = 60.0 / 180.0

# Initialize the audio player
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

# Play the chords in sequence
for chord_sound, (_, duration) in zip(chord_sounds, chords):
    stream.write(chord_sound.tobytes())
    time.sleep(beat_time * duration / 1000.0)

# Clean up the audio player
stream.stop_stream()
stream.close()
p.terminate()