from midiutil import MIDIFile
from music21 import *
import pychord
import numpy as np

def noteToMidi(note):
    pitch_obj = pitch.Pitch(note)
    return pitch_obj.midi

# Define the tempo and time signature
tempo = 600 #120
time_signature = (4, 4)

# Define the melody notes and durations
melody_notes = [
    ("B4", 1), ("A4", 0.5), ("G#4", 0.5), ("A4", 1), ("B4", 1), ("D5", 1),
    ("B4", 1), ("A4", 0.5), ("G#4", 0.5), ("A4", 1), ("B4", 1), ("D5", 1),
    ("B4", 1), ("A4", 0.5), ("G#4", 0.5), ("A4", 1), ("B4", 1), ("D5", 1),
    ("B4", 1), ("A4", 0.5), ("G#4", 0.5), ("A4", 1), ("B4", 1), ("D5", 1),
    ("B4", 1), ("A4", 0.5), ("G#4", 0.5), ("A4", 1), ("B4", 1), ("D5", 1),
    ("B4", 1), ("D5", 1), ("E5", 1), ("F#5", 1), ("E5", 1), ("D5", 1),
    ("B4", 1), ("D5", 1), ("E5", 1), ("F#5", 1), ("E5", 1), ("D5", 1),
    ("B4", 1), ("D5", 1), ("E5", 1), ("F#5", 1), ("E5", 1), ("D5", 1),
    ("B4", 1), ("D5", 1), ("E5", 1), ("F#5", 1), ("E5", 1), ("D5", 1),
    ("B4", 1), ("D5", 1), ("E5", 1), ("F#5", 1), ("E5", 1), ("D5", 1),
    ("C#5", 1), ("B4", 1), ("A4", 1), ("B4", 1), ("C#5", 1), ("D5", 1),
    ("E5", 1), ("D5", 1), ("C#5", 1), ("B4", 1), ("A4", 1), ("B4", 1),
    ("G#4", 2), ("A4", 2), ("B4", 2), ("C#5", 2), ("D5", 2), ("E5", 2),
    ("D5", 2), ("C#5", 2), ("B4", 2), ("A4", 2), ("B4", 2), ("G#4", 2)
]

# Define the melody instrument
melody_program = 25 # Slap Bass 2

# Define the chord progression and durations
chord_progression = [
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2),
    ("G#m7", 2), ("C#7", 2), ("F#maj7", 2), ("Bmaj7", 2)
    ]

#Define the chord instrument
chord_program = 5 # Electric Piano 1

#Create a MIDI file with one track
midi_file = MIDIFile(numTracks=1)
midi_file.addTempo(track=0, time=0, tempo=tempo)
midi_file.addTimeSignature(track=0, time=0, numerator=time_signature[0], denominator=time_signature[1], clocks_per_tick=24)

#Add the melody notes to the MIDI file
melody_track = 0
channel = 0
volume = 100
time = 0
for note, duration in melody_notes:
    midi_note = noteToMidi(note)
    midi_file.addNote(melody_track, channel, midi_note, time, duration, volume, melody_program)
    time += duration

#Add the chord notes to the MIDI file
chord_track = 0
channel = 1
volume = 80
time = 0

for chord, duration in chord_progression:
    chord_notes = pychord.Chord(chord).components()
    for note in chord_notes:
        midi_note = noteToMidi(note)
        midi_file.addNote(chord_track, channel, midi_note, time, duration, volume, chord_program)
        time += duration

#Write the MIDI file to disk
with open("./mus/main_theme.mid", "wb") as output_file:
    midi_file.writeFile(output_file)