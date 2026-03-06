import numpy as np
import soundfile as sf

def snr(clean, denoised):
    noise = clean - denoised
    return 10 * np.log10(np.sum(clean**2) / np.sum(noise**2))

clean, _ = sf.read("Normalized_Mighty_Sparrow_Jean_Dinah.wav", dtype='float64')
denoised, _ = sf.read("Denoised_Sparrow10dB_nmf_semi_supervised.wav")
clean = clean.mean(axis=1) if clean.ndim == 2 else clean
denoised = denoised.mean(axis=1) if denoised.ndim == 2 else denoised

min_len = min(len(clean), len(denoised))
clean = clean[:min_len]
denoised = denoised[:min_len]

value = snr(clean, denoised)
print("SNR:", value)
#SNR_improvement = SNR(denoised) – SNR(noisy)
#C:\Users\Aliya\OneDrive\Documents\Audacity\