import fluidsynth
from pydub import AudioSegment

# Initialize FluidSynth
fs = fluidsynth.Synth()
fs.start(driver="alsa")

# Load the soundfont
#sfid = fs.sfload("/path/to/soundfont.sf2")

# Load the MIDI file
midi_data = open("./mus/theme.mid", 'rb').read()

# Parse the MIDI data
fsmidi = fluidsynth.MidiFile()
fsmidi.read(midi_data)

# Convert the MIDI to audio
audio_data = fs.render(fsmidi)

# Convert the audio data to WAV format
wav_data = AudioSegment(
    audio_data, 
    sample_width=2, 
    frame_rate=44100, 
    channels=2
).export("./mus/theme.wav", format="wav")

# Clean up FluidSynth
fs.delete()