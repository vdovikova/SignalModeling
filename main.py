import math
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq
from numpy import heaviside as hvsd
from numpy import abs as np_abs

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


def graphDigital(f, timeArray):
    fd = 1000
    w = 2 * math.pi * f / fd
    xArray = []
    for t in range(0, 1000):
        x = hvsd(math.sin(w * t), 1)
        xArray.append(x)
        timeArray.append(t)
    return xArray


fig, axs = plt.subplots(4, 2)
fig.suptitle('Harmonic signals')
fig.tight_layout(h_pad=2)

func = graphHarmonic(1, timeArray)
axs[0, 0].plot(timeArray, func, color='g')
axs[0, 0].set_title('1 Hz', fontsize=8)
spector_sin = rfft(func)
axs[0, 1].plot(rfftfreq(1000, 1. / 1000), np_abs(spector_sin) / 1000)
axs[0, 0].set_xlabel("ms", fontsize=7, loc='left')
axs[0, 1].set_xlim([0, 10])
axs[0, 1].set_title('1 Hz, spectrum', fontsize=8)
axs[0, 1].set_xlabel("Hz", fontsize=7, loc='left')
timeArray = []

func = graphHarmonic(2, timeArray)
axs[1, 0].plot(timeArray, func, color='blue')
axs[1, 0].set_title('2 Hz', fontsize=8)
axs[1, 0].set_xlabel("ms", fontsize=7, loc='left')
spector_sin = rfft(func)
axs[1, 1].plot(rfftfreq(1000, 1. / 1000), np_abs(spector_sin) / 1000)
axs[1, 1].set_xlim([0, 10])
axs[1, 1].set_title('2 Hz, spectrum', fontsize=8)
axs[1, 1].set_xlabel("Hz", fontsize=7, loc='left')
timeArray = []

func = graphHarmonic(4, timeArray)
axs[2, 0].plot(timeArray, func, color='m')
axs[2, 0].set_title('4 Hz', fontsize=8)
axs[2, 0].set_xlabel("ms", fontsize=7, loc='left')
spector_sin = rfft(func)
axs[2, 1].plot(rfftfreq(1000, 1. / 1000), np_abs(spector_sin) / 1000)
axs[2, 1].set_xlim([0, 10])
axs[2, 1].set_title('4 Hz, spectrum', fontsize=8)
axs[2, 1].set_xlabel("Hz", fontsize=7, loc='left')
timeArray = []

func = graphHarmonic(8, timeArray)
axs[3, 0].plot(timeArray, func, color='r')
axs[3, 0].set_title('8 Hz', fontsize=8)
axs[3, 0].set_xlabel("ms", fontsize=7, loc='left')
spector_sin = rfft(func)
axs[3, 1].plot(rfftfreq(1000, 1. / 1000), np_abs(spector_sin) / 1000)
axs[3, 1].set_xlim([0, 10])
axs[3, 1].set_title('8 Hz, spectrum', fontsize=8)
axs[3, 1].set_xlabel("Hz", fontsize=7, loc='left')
plt.show()
timeArray = []

########################################
fig, axs = plt.subplots(4, 2)
fig.suptitle('Digital signals')
fig.tight_layout(h_pad=2)

func = graphDigital(1, timeArray)
axs[0, 0].plot(timeArray, func, color='green')
axs[0, 0].set_title('1 Hz', fontsize=8)
axs[0, 0].set_xlabel("ms", fontsize=7, loc='left')
spector_sin = rfft(func)
y = np_abs(spector_sin) / 1000
y[0] = 0
axs[0, 1].plot(rfftfreq(1000, 1. / 1000), y)
axs[0, 1].set_xlim([0, 50])
axs[0, 1].set_title('1 Hz, spectrum', fontsize=8)
axs[0, 1].set_xlabel("Hz", fontsize=7, loc='left')
timeArray = []

func = graphDigital(2, timeArray)
axs[1, 0].plot(timeArray, func, color='b')
axs[1, 0].set_title('2 Hz', fontsize=8)
axs[1, 0].set_xlabel("ms", fontsize=7, loc='left')
spector_sin = rfft(func)
y = np_abs(spector_sin) / 1000
y[0] = 0
axs[1, 1].plot(rfftfreq(1000, 1. / 1000), y)
axs[1, 1].set_xlim([0, 50])
axs[1, 1].set_title('2 Hz, spectrum', fontsize=8)
axs[1, 1].set_xlabel("Hz", fontsize=7, loc='left')
timeArray = []

func = graphDigital(4, timeArray)
axs[2, 0].plot(timeArray, func, color='m')
axs[2, 0].set_title('4 Hz', fontsize=8)
axs[2, 0].set_xlabel("ms", fontsize=7, loc='left')
spector_sin = rfft(func)
y = np_abs(spector_sin) / 1000
y[0] = 0
axs[2, 1].plot(rfftfreq(1000, 1. / 1000), y)
axs[2, 1].set_xlim([0, 50])
axs[2, 1].set_title('4 Hz, spectrum', fontsize=8)
axs[2, 1].set_xlabel("Hz", fontsize=7, loc='left')
timeArray = []

func = graphDigital(8, timeArray)
axs[3, 0].plot(timeArray, func, color='r')
axs[3, 0].set_title('8 Hz', fontsize=8)
axs[3, 0].set_xlabel("ms", fontsize=7, loc='left')
spector_sin = rfft(func)
y = np_abs(spector_sin) / 1000
y[0] = 0
axs[3, 1].plot(rfftfreq(1000, 1. / 1000), y)
axs[3, 1].set_xlim([0, 50])
axs[3, 1].set_title('8 Hz, spectrum', fontsize=8)
axs[3, 1].set_xlabel("Hz", fontsize=7, loc='left')
plt.show()
