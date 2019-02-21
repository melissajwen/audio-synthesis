from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# Globals
PIANO_WAV = "scale.wav"
SIN_WAV = "sin_scale.wav"
SAMPLE_FREQ = 44100

# Values obtained from analysis of pitch tracking with Sonic Visualizer and pYIN plugin
TIME = [0, 0.319274376, 0.940408163, 1.515102041, 2.060770975, 2.618049887, 3.204353741, 3.744217687, 4.307301587,
        4.876190476]
FREQ = [0, 261, 290, 330, 350, 390, 440, 495, 524]


# Part I
def pitch_tracking():
    # Declare data to hold generated sine waves
    data = []

    # Loop over time and frequency arrays
    for i in range(9):
        # Obtain the frequency and time duration
        freq = FREQ[i]
        time = TIME[i + 1] - TIME[i]

        # Produce a sine wave signal
        samples = np.arange(time * SAMPLE_FREQ) / SAMPLE_FREQ
        signal = np.sin(2 * np.pi * freq * samples)
        signal *= 32767
        signal = np.int16(signal)

        # Append the generated signal to data array
        data.append(signal)

    # Concatenate all generated tones into a single signal
    scale = np.concatenate(data)

    # Output the data to a .wav file
    wavfile.write(SIN_WAV, SAMPLE_FREQ, scale)


# Part II
def note_length_modification():
    # Read in data from .wav file
    fs, data = wavfile.read(PIANO_WAV, 'r')

    # Plot the data
    plt.title('File Data from ' + PIANO_WAV)
    plt.plot(data)
    plt.savefig("plot.png")

    # Calculate a single period of the note and find frequency
    single_period = TIME[len(TIME) - 1] - TIME[len(TIME) - 2]
    freq = FREQ[len(FREQ) - 1]

    # Produce a sine wave signal to be appended at the end
    samples = np.arange(single_period * SAMPLE_FREQ) / SAMPLE_FREQ
    signal = np.sin(2 * np.pi * freq * samples)
    signal *= 32767
    signal = np.int16(signal)

    # Retrieve data from original scale
    fs, data = wavfile.read(SIN_WAV)

    # Concatenate the two signals
    long_signal = np.concatenate((data, signal))

    # Write data to output .wav file
    wavfile.write('long_scale.wav', SAMPLE_FREQ, long_signal)


def main():
    pitch_tracking()
    note_length_modification()


main()
