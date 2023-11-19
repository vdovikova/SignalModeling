import math
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, ifft, fft
import numpy as np
from numpy import heaviside as hvsd
from numpy import abs as np_abs

timeArray = list(range(0, 1000))
freq = 30


def graphHarmonic(f):
    fd = 1000  # частота дискретизации
    w = 2 * math.pi * f / fd
    A = 1
    xArray = []
    for t in timeArray:
        x = A * math.sin(w * t)
        xArray.append(x)
    return xArray


def graphDigital(f):
    fd = 1000
    w = 2 * math.pi * f / fd
    xArray = []
    for t in timeArray:
        x = hvsd(math.sin(w * t), 1)
        xArray.append(x)
    return xArray


def printPlotHarmonic(freqList):
    fig, axs = plt.subplots(len(freqList), 2)
    fig.suptitle('Harmonic signal')
    fig.tight_layout(h_pad=2)
    j = 0

    for i in freqList:
        f = graphHarmonic(i)
        axs[j, 0].plot(timeArray, f, color='g')
        s = str(i) + 'Hz'
        axs[j, 0].set_title(s, fontsize=8)
        spector_sin = rfft(f)
        axs[j, 1].plot(rfftfreq(1000, 1. / 1000), np_abs(spector_sin) / 1000)
        axs[j, 0].set_xlabel("ms", fontsize=7, loc='left')
        axs[j, 1].set_xlim([0, 10])
        s = str(i) + 'Hz, spectrum'
        axs[j, 1].set_title(s, fontsize=8)
        axs[j, 1].set_xlabel("Hz", fontsize=7, loc='left')
        j += 1

    plt.show()


def printPlotDigital(freqList):
    fig, axs = plt.subplots(4, 2)
    fig.suptitle('Digital signal')
    fig.tight_layout(h_pad=2)
    j = 0

    for i in freqList:
        f = graphDigital(i)
        axs[j, 0].plot(timeArray, f, color='g')
        s = str(i) + 'Hz'
        axs[j, 0].set_title(s, fontsize=8)
        axs[j, 0].set_xlabel("ms", fontsize=7, loc='left')
        spector_sin = rfft(f)
        y = np_abs(spector_sin) / 1000
        y[0] = 0
        axs[j, 1].plot(rfftfreq(1000, 1. / 1000), y)
        axs[j, 1].set_xlim([0, 50])
        s = str(i) + 'Hz, spectrum'
        axs[j, 1].set_title(s, fontsize=8)
        axs[j, 1].set_xlabel("Hz", fontsize=7, loc='left')
        j += 1

    plt.show()


def getSpectrum(f):
    spector_sin = fft(f)
    spectrum = (0.1 / 1000) * abs(spector_sin[0:len(timeArray)])
    spectrum[0] = 0
    return spectrum


def ampModulation(f1, f2):
    res = []
    for t in timeArray:
        res.append(f1[t] * f2[t])
    return res


def frequencyModulation(f):
    res = []
    for t in timeArray:
        res.append(math.sin(2 * math.pi * freq/1000 * (f[t]+1) * t))
    return res


def phaseModulation(f):
    res = []
    for t in timeArray:
        res.append(math.sin(2 * np.pi * 2 * freq/1000 * t + f[t]))
    return res


def plotModulatedSignal(f1, f2, s):
    fig, axs = plt.subplots(3, 2)

    if s == 'A':
        f = ampModulation(f1, f2)
        fig.suptitle('A-Modulated harmonic signal')
    elif s == 'F':
        f = frequencyModulation(f2)
        fig.suptitle('F-Modulated harmonic signal')
    else:
        f = phaseModulation(f2)
        fig.suptitle('P-Modulated harmonic signal')

    fig.tight_layout(h_pad=2)
    axs[0, 1].set_xlim([0, 100])
    axs[1, 1].set_xlim([0, 100])
    axs[2, 1].set_xlim([0, 100])

    axs[0, 0].set_xlabel("ms", fontsize=7, loc='left')
    axs[0, 0].plot(timeArray, f, color='g')
    axs[1, 0].set_xlabel("ms", fontsize=7, loc='left')
    axs[1, 0].plot(timeArray, f1, color='r')
    axs[2, 0].set_xlabel("ms", fontsize=7, loc='left')
    axs[2, 0].plot(timeArray, f2, color='purple')

    axs[0, 1].set_title('Hz, spectrum', fontsize=8)
    axs[0, 1].set_xlabel("Hz", fontsize=7, loc='left')
    axs[0, 1].plot(timeArray, getSpectrum(f))
    axs[1, 1].set_xlabel("Hz", fontsize=7, loc='left')
    axs[1, 1].plot(timeArray, getSpectrum(f1))
    axs[2, 1].set_xlabel("Hz", fontsize=7, loc='left')
    axs[2, 1].plot(timeArray, getSpectrum(f2))


def plotSignalSynthesisBySpectrum(f):
    fig, axs = plt.subplots(3, 1)
    fig.suptitle('Synthesis Of Modulating Signal By AM-Signal Spectrum')
    fig.tight_layout(h_pad=2)

    # Spectrum filter
    s = np.abs(getSpectrum(f))
    spector = []
    for i in s[0:len(timeArray)]:
        if np.abs(i) >= 0.01:
            spector.append(np.abs(i))
        else:
            spector.append(0)

    # Reversed spectrum transform
    f1 = ifft(s)
    ff = np.abs(f1)

    # Envelope
    envelope = []
    for t in range(40, len(timeArray)+40):
        envelope.append(sum(ff[t-40:t])/40)
    axs[0].plot(timeArray, ff, color='g')
    axs[0].plot(timeArray, envelope, color='r')

    # Recreating digital signal
    res = []
    for i in envelope:
        if i >= max(envelope)/2:
            res.append(1)
        else:
            res.append(0)

    axs[1].plot(timeArray, res, color='purple')
    axs[2].plot(timeArray, spector)
    axs[2].set_xlim([0, 100])
    return


func1 = graphHarmonic(freq)
func2 = graphDigital(3)
plotModulatedSignal(func1, func2, 'A')
plt.show()
plotModulatedSignal(func1, func2, 'F')
plt.show()
plotModulatedSignal(func1, func2, 'P')
plt.show()
plotSignalSynthesisBySpectrum(ampModulation(func1, func2))
plt.show()
