import os
import numpy as np
import matplotlib.pyplot as plt
from data import main_peak_Ar, fwhm_Ar, back_peak_Ar, back_fwhm_Ar, V_Ar, main_peak_Xe, fwhm_Xe, back_peak_Xe, back_fwhm_Xe, V_Xe
OUTPUT_DIR = "output"


def create_dir(path):
    if (not os.path.exists(path)):
        os.mkdir(path)


def create_fig(x, y, xlabel, ylabel, title=None, filename=None, ylim=None, label=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'o', label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title is not None:
        ax.set_title(title)
    if ylim is not None:
        ax.set_ylim(ylim)
    fig.tight_layout()
    if filename is not None:
        fig.savefig(filename)
    return fig, ax


def analise(element, peak, fwhm, back_peak, back_fwhm, V):
    element_dir = os.path.join(OUTPUT_DIR, element)
    create_dir(element_dir)
    R = fwhm / peak
    create_fig(
        V, R * 100,
        xlabel="V [V]",
        ylabel="R [%]",
        title=element,
        filename=os.path.join(element_dir, "R.png"),
        ylim=(10, 25),
    )

    # R_back = back_fwhm / back_peak
    # create_fig(
    #     V, R_back,
    #     xlabel="V [V]",
    #     ylabel="R",
    #     title=element,
    #     filename=os.path.join(element_dir, "R_back.png")
    # )

    back_peak_main_peak = back_peak / peak
    fig, ax = create_fig(
        V, back_peak_main_peak,
        xlabel="V [V]",
        ylabel="R",
        title=element,
        ylim=(0, 1),
        label="punkty pomiarowe"
    )
    ax.plot(V, 0.5*np.ones_like(V), 'k--', label="wartość teoretyczna")
    ax.legend()
    fig.savefig(os.path.join(element_dir, "back_peak_main_peak.png"))


def main():
    create_dir(OUTPUT_DIR)
    print(V_Xe)
    analise("Ar", main_peak_Ar, fwhm_Ar, back_peak_Ar, back_fwhm_Ar, V_Ar)
    analise("Xe", main_peak_Xe, fwhm_Xe, back_peak_Xe, back_fwhm_Xe, V_Xe)


if __name__ == "__main__":
    main()
