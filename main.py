import math
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq
from numpy import array, arange, abs as np_abs

timeArray = []


def graphHarmonic(f, tarr):
    fd = 1000  # частота дискретизации
    omega = 2 * math.pi * f / fd
    A = 1
    xArray = []
    for t in range(0, 1000):
        x = A * math.sin(omega * t)
        xArray.append(x)
        tarr.append(t)
    return xArray


fig, axs = plt.subplots(4, 2)
fig.suptitle('Harmonic signals')
fig.tight_layout(h_pad=2)

func = graphHarmonic(1, timeArray)
axs[0, 0].plot(timeArray, func, color='green')
axs[0, 0].set_title('1 Hz', fontsize=8)
spectr_sin = rfft(func)
axs[0, 1].plot(rfftfreq(1000, 1./1000), np_abs(spectr_sin)/1000)
axs[0, 1].set_title('1 Hz, spectrum', fontsize=8)
timeArray = []

func = graphHarmonic(2, timeArray)
axs[1, 0].plot(timeArray, func, color='blue')
axs[1, 0].set_title('2 Hz', fontsize=8)
spectr_sin = rfft(func)
axs[1, 1].plot(rfftfreq(1000, 1./1000), np_abs(spectr_sin)/1000)
axs[1, 1].set_title('2 Hz, spectrum', fontsize=8)
timeArray = []

func = graphHarmonic(4, timeArray)
axs[2, 0].plot(timeArray, func, color='red')
axs[2, 0].set_title('4 Hz', fontsize=8)
spectr_sin = rfft(func)
axs[2, 1].plot(rfftfreq(1000, 1./1000), np_abs(spectr_sin)/1000)
axs[2, 1].set_title('4 Hz, spectrum', fontsize=8)
timeArray = []

func = graphHarmonic(8, timeArray)
axs[3, 0].plot(timeArray, func, color='black')
axs[3, 0].set_title('8 Hz', fontsize=8)
spectr_sin = rfft(func)
axs[3, 1].plot(rfftfreq(1000, 1./1000), np_abs(spectr_sin)/1000)
axs[3, 1].set_title('8 Hz, spectrum', fontsize=8)
plt.show()
