import numpy as np
import pygame.sndarray

def generate_laser_beep(start_freq=1500, end_freq=300, duration_ms=200, volume=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * duration_ms / 1000)
    t = np.linspace(0, duration_ms / 1000, n_samples, False)

    freqs = np.linspace(start_freq, end_freq, n_samples)
    wave = 32767 * np.sin(2 * np.pi * freqs * t)

    # Convert to stereo
    wave = np.column_stack((wave, wave)).astype(np.int16)

    sound = pygame.sndarray.make_sound(wave)
    sound.set_volume(volume)
    return sound