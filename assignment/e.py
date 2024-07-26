import numpy as np
import matplotlib.pyplot as plt


def analyze_signal_fft():
    # Parameters
    f1, f2 = 50, 120  # Hz
    fs = 1000  # Sampling frequency (1 kHz)
    t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration

    # Generate the signal
    signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    # Compute FFT
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(t), 1 / fs)

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(freqs[: fs // 2], np.abs(fft_result)[: fs // 2])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("FFT of the Signal")
    plt.xlim(0, 150)
    plt.grid(True)
    plt.savefig("./assets/e-signal_fft.png")


# Run the analysis
analyze_signal_fft()
