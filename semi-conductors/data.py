import os
import matplotlib.pyplot as plt
import numpy as np
# pik left = 169
# efekt ścianowy
V = np.array([
    60, 73, 77, 83,
    92, 100, 106, 112,
    118, 126, 130, 142,
    146, 153, 160
])  # [keV]
all = np.array([
    15986, 88426, 150811, 74322,
    54612, 97489, 89674, 185545,
    99393, 94441, 50665, 97988,
    92764, 94953, 97535
])  # zliczenia
pik = np.array([
    13147, 71826, 123723, 62030,
    46187, 82895, 76609, 159740,
    85814, 81778, 44074, 85453,
    81099, 83107, 85510])  # zliczenia

half_width = np.array([
    0.3, 0.3, 0.25, 0.25,
    0.2, 0.15, 0.2, 0.15,
    0.1, 0.1, 0.15, 0.1,
    0.15, 0.15, 0.1
])

main_peaks = np.array([
    3.2, 2.9, 2.9, 2.9,
    2.9, 2.8, 2.8, 2.8,
    2.9, 2.9, 2.8, 2.9,
    2.9, 2.9, 2.9
])

configuration_x = np.array([180, 197, 673, 766])  # [channels]
configuration_y = np.array([5.9, 6.5, 22.2, 24.9])  # [keV]

channelsAm = np.array([169, 197, 360, 403, 536, 631, 643, 672, 767, 814, 1005])
channelsPu = np.array([352, 408, 462, 494, 518, 606, 626])


def make_calibration():
    m, b = np.polyfit(configuration_x, configuration_y, 1)

    def calculate_energy(channel):
        return m * channel + b
    # plot calibration line
    fig, ax = plt.subplots()
    ax.scatter(configuration_x, configuration_y, label="calibration points")
    x_data = np.linspace(0, 1024)
    ax.plot(x_data, m * x_data + b, label="calibration line")
    ax.set_xlabel("channel")
    ax.set_ylabel("energy [keV]")
    ax.legend()
    fig.tight_layout()
    fig.savefig("output/calibration.png")
    return calculate_energy


def plot_R():
    R = half_width / main_peaks * 100  # [%]
    fig, ax = plt.subplots()
    ax.scatter(V, R)
    ax.set_xlabel("V [keV]")
    ax.set_ylabel("R [%]")
    ax.set_ylim(0, 20)
    fig.tight_layout()
    fig.savefig("output/R.png")


def plot_ratio():
    ratio = pik / all
    print(ratio.mean())
    fig, ax = plt.subplots()
    ax.scatter(V, ratio)
    ax.set_xlabel("V [keV]")
    ax.set_ylabel("ratio")
    fig.tight_layout()
    fig.savefig("output/ratio.png")


def main():
    # if output doesnt exist, create it
    if not os.path.exists("output"):
        os.makedirs("output")
    plot_ratio()
    plot_R()
    get_energy = make_calibration()
    print(get_energy(channelsAm))
    print(get_energy(channelsPu))


if __name__ == '__main__':
    main()
