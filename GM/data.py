import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# plt.xkcd()
OUTPUT = "output"
Umax = 2000


def get_U(tick, Umax):
    return tick / 10 * Umax


def get_tick(U, Umax):
    return U / Umax * 10


def get_ticks(counts, first_tick):
    ticks = np.array([first_tick + 0.1 * i for i in range(len(counts))])
    return ticks


def get_average(down, up, first_tick):
    U = get_U(get_ticks(up, first_tick), Umax)
    if down is None:
        return U, up
    if (len(down) != len(up)):
        raise ValueError("down and up must be of the same length")
    output = (np.flip(down) + up) / 2
    return U, output


def fit(x, y, skip_first=0, skip_last=None):
    if len(x) != len(y):
        raise ValueError("x and y must be of the same length")
    xdata = x[skip_first:-skip_last] if skip_last else x[skip_first:]
    ydata = y[skip_first:-skip_last] if skip_last else y[skip_first:]
    return np.polyfit(xdata, ydata, 1)


def add_fit_plot(ax, x, m, b, label=None):
    x = np.linspace(x[0], x[-1], 100)
    y = m * x + b
    ax.plot(x, y, label=label)


def add_plots(ax, xdata, y_arr, xlabel, ylabel, labels=None):
    if labels is None:
        labels = [None] * len(xdata)

    for y, label in zip(y_arr, labels):
        ax.scatter(xdata, y, label=label)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    ax.legend()


def analise_data(countUp, countDown, first_tick, name, skip_first=0, skip_last=None):
    U, count = get_average(countDown, countUp, first_tick)
    m, b = fit(U, count, skip_first, skip_last)
    fig, ax = plt.subplots()
    add_fit_plot(ax, U, m, b)
    if (countDown is not None):
        add_plots(ax, U, [count, np.flip(countDown),
                          countUp], "U [V]", "counts", ["average", "down", "up"])
    else:
        add_plots(ax, U, [count],
                  "U [V]", "counts", ["up"])
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT, f"{name}.png"))
    df = pd.DataFrame({"U [V]": U, "count": count})
    df.set_index("U [V]", inplace=True)
    df.to_csv(f"{OUTPUT}/{name}.csv")

    return m, b


# Cosmic Radiation
first_tick = 6.8
countsUpCosmic = np.array([27, 1365, 1662, 1745, 1769, 1738,
                           1749, 1713, 1680, 1828, 1849, 1901, 1906])
countsDownCosmic = np.array([1974, 1938, 1742, 1771, 1788,
                             1758, 1812, 1771, 1795, 1674, 1643, 1384, 28])


# Co-60
# 6.7
countsUpCo60 = np.array(
    [2, 1093, 4455, 4437, 4501, 4431, 4401, 4521, 4526,
     4568, 4543, 5521, 5336, 4771, 4602, 4585, 5350, 7590])


BigDeath_time = np.array([
    470, 400, 360, 310, 300, 280, 220,
])  # μs

SmallDeath_time = np.array([
    240, 220, 200, 184, 176, 170, 164, 160, 140, 120, 100
])


# Death Time


def analyse_death_time(V0, Vstep, times, name):
    V = np.array([V0 + Vstep * i for i in range(len(times))])
    fig, ax = plt.subplots()
    ax.scatter(V, times)
    ax.set_xlabel("V [V]")
    ax.set_ylabel("t [μs]")
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT, f"{name}.png"))
    df = pd.DataFrame({"V [V]": V, "t [μs]": times})
    df.set_index("V [V]", inplace=True)
    df.to_csv(f"{OUTPUT}/{name}.csv")


if __name__ == "__main__":
    # if output dir doesnt exist, create it
    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)
    mCosmic, bCosmic = analise_data(
        countsUpCosmic, countsDownCosmic, 6.8, "cosmic", 2, 3)

    mCo60, bCo60 = analise_data(countsUpCo60, None, 6.9, "co60", 2, 3)
    analyse_death_time(1360, 20, BigDeath_time, "big_death_time")
    analyse_death_time(1400, 20, SmallDeath_time, "small_death_time")
