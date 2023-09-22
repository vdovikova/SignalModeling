import math
import matplotlib.pyplot as plt

timeArray = []


def graphHarmonic(f, tarr):
    fd = 1000
    omega = 2 * math.pi * f / fd
    A = 1
    xArray = []
    for t in range(0, 1000):
        x = A * math.sin(omega * t)
        xArray.append(x)
        tarr.append(t)
    return xArray


fig, axs = plt.subplots(4)
fig.suptitle('Harmonic signals')

axs[0].plot(timeArray, graphHarmonic(1, timeArray), color='green')
axs[0].set_title('1 Hz')
timeArray = []
axs[1].plot(timeArray, graphHarmonic(2, timeArray), color='blue')
axs[1].set_title('2 Hz')
timeArray = []
axs[2].plot(timeArray, graphHarmonic(4, timeArray), color='red')
axs[2].set_title('4 Hz')
timeArray = []
axs[3].plot(timeArray, graphHarmonic(8, timeArray), color='black')
axs[3].set_title('8 Hz')
plt.show()
