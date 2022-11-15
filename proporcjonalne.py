import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Cd-109, pierwsza grupa pików - artefakty z ksenonu śmieci, kolejny pik to podwójny pik (nie widać) - od (moze) kryptonu, chuj wie, chuj wie, Kα Kadmu, Kβ Kadmu


# Cd-109 z Mo
# od lewej
# pierwszy nie wazny
# kolejne trze prawdopodobnie z krypotonem
# Kα molibnenu (na prawym zboczu jest Kβ - chuja widać)
L = 16.2  # cm
channels = 1024


def get_channel(length):
    return np.round(length / L * channels)


# Al-27
# od lewej
# wszystko na pewno nie Aluminium
labels = ["Kα Cd-109", "Κβ Cd-109", "Kβ Κr", "Kα Kr"]
lengths = np.array([14.95, 13.2, 7.4, 5.75, 4.85])
energies_teo = np.array([24.9, 22.16])  # keV
m, b = np.polyfit(get_channel(lengths[:len(energies_teo)]), energies_teo, 1)

# plot the calibration line
x = np.linspace(0, 1024, 100)
y = m * x + b
plt.plot(x, y, label="calibration line")
plt.scatter(get_channel(lengths[:len(energies_teo)]),
            energies_teo, label="measured energies")
plt.xlabel("channel")
plt.ylabel("energy [keV]")
plt.legend()
plt.show()


def get_energy(length):
    return length * 22.16/13.2


print(m, b)


# for length in lengths:
#     print(f"Channel: {get_channel(length)}")
#     print(f"E = {get_energy(length)}")

while True:
    try:
        length = float(input("Enter length [cm]: "))
        print(f"E = {get_energy(length)} keV")
    except KeyboardInterrupt:
        break
