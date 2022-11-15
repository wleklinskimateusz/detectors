import os
import numpy as np
import matplotlib.pyplot as plt
from data import main_peak_Ar, fwhm_Ar, back_peak_Ar, back_fwhm_Ar, V_Ar, main_peak_Xe, fwhm_Xe, back_peak_Xe, back_fwhm_Xe, V_Xe
OUTPUT_DIR = "output"


def create_dir(path):
    if (not os.path.exists(path)):
        os.mkdir(path)


def savefig(x, y, xlabel, ylabel, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'o')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    fig.savefig(filename)


def analise(element, peak, fwhm, back_peak, back_fwhm, V):
    element_dir = os.path.join(OUTPUT_DIR, element)
    create_dir(element_dir)
    R = fwhm / peak
    savefig(V, R, "V [V]", "R", os.path.join(element_dir, "R.png"))

    R_back = back_fwhm / back_peak
    savefig(V, R_back, "V [V]", "R", os.path.join(element_dir, "R_back.png"))

    back_peak_main_peak = back_peak / peak
    savefig(V, back_peak_main_peak, "V [V]", "R", os.path.join(
        element_dir, "back_peak_main_peak.png"))


def main():
    create_dir(OUTPUT_DIR)
    print(V_Xe)
    analise("Ar", main_peak_Ar, fwhm_Ar, back_peak_Ar, back_fwhm_Ar, V_Ar)
    analise("Xe", main_peak_Xe, fwhm_Xe, back_peak_Xe, back_fwhm_Xe, V_Xe)


if __name__ == "__main__":
    main()
