import matplotlib.pyplot as plt
import numpy as np
# pik left = 169
# efekt ścianowy
V = np.array([
    60, 73, 77, 83,
    92, 100, 106, 112,
    118, 126, 130, 142,
    146, 153,
])  # [keV]
all = np.array([
    15986, 88426, 150811, 74322,
    54612, 97489, 89674, 185545,
    99393, 94441, 50665, 97988,
    92764, 94953
])  # zliczenia
pik = np.array([
    13147, 71826, 123723, 62030,
    46187, 82895, 76609, 157740,
    85814, 81778, 44074, 85453,
    81099, 83107])  # zliczenia


ratio = pik / all
# plt.scatter(V, ratio)
# # plt.ylim(0, 1)
# plt.show()

x = np.array([180, 197, 673, 766])
y = np.array([5.9, 6.5, 22.2, 24.9])

m, b = np.polyfit(x, y, 1)
print(m, b)


def get_energy(channel):
    return m * channel + b


channelsAm = np.array([169, 197, 360, 403, 536, 631, 643, 672, 767, 814, 1005])
channelsPu = np.array([352, 408, 462, 494, 518, 606, 626])

while True:
    try:
        channel = int(input('Podaj kanał: '))
        print(f"{get_energy(channel)}keV")
    except KeyboardInterrupt:
        break
