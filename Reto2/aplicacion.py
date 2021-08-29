import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams.update({'font.size': 18})
plt.style.use('seaborn')

dt = 0.001
t = np.arange(0, 1, dt)
signal = np.sin(2*np.pi*40*t) + np.sin(2*np.pi*20*t)
signal_clean = signal
signal = signal + 2.5 * np.random.randn(len(t))
minsignal, maxsignal = signal.min(), signal.max()

n = len(t)
fhat = np.fft.fft(signal, n)
psd = fhat * np.conj(fhat)/n
freq = (1/(dt*n)) * np.arange(n)
idxs_half = np.arange(1, np.floor(n/2), dtype=np.int32)

threshold = 100
psd_idxs = psd > threshold
psd_clean = psd * psd_idxs
fhat_clean = psd_idxs * fhat

signal_filtered = np.fft.ifft(fhat_clean)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
ax1.plot(t, signal, color='b', lw=0.5, label='Noisy Signal')
ax1.plot(t, signal_clean, color='r', lw=1, label='Clean Signal')
ax1.set_ylim([minsignal, maxsignal])
ax1.set_xlabel('t axis')
ax1.set_ylabel('Vals')
ax1.legend()

ax2.plot(freq[idxs_half], np.abs(psd[idxs_half]), color='b', lw=0.5, label='PSD noisy')
ax2.set_xlabel('Frequencies in Hz')
ax2.set_ylabel('Amplitude')
ax2.legend()

ax3.plot(freq[idxs_half], np.abs(psd_clean[idxs_half]), color='r', lw=1, label='PSD clean')
ax3.set_xlabel('Frequencies in Hz')
ax3.set_ylabel('Amplitude')
ax3.legend()

ax4.plot(t, signal_filtered, color='r', lw=1, label='Clean Signal Retrieved')
ax4.set_ylim([minsignal, maxsignal])
ax4.set_xlabel('t axis')
ax4.set_ylabel('Vals')
ax4.legend()

plt.subplots_adjust(hspace=0.4)

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=30,
    valinit=10,
)
