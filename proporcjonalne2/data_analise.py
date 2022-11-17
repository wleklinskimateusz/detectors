from data import main_peak_Ar, fwhm_Ar, back_peak_Ar, V_Ar, main_peak_Xe, fwhm_Xe, back_peak_Xe, V_Xe
import pandas as pd
import numpy as np


def get_table(V, main_peak, fwhm, escape):
    output = pd.DataFrame()
    output["U [V]"] = V
    output["E_m [channel]"] = main_peak
    output["FWHM [channel]"] = fwhm
    output["E_e [channel]"] = escape
    output.set_index("U [V]", inplace=True)
    output["R [%]"] = main_peak / fwhm * 100
    output["E_m / E_e"] = main_peak / escape
    return output


Ar_table = get_table(V_Ar, main_peak_Ar, fwhm_Ar, back_peak_Ar)
Ar_table.to_csv("output/Ar/data.csv")

Xe_table = get_table(V_Xe, main_peak_Xe, fwhm_Xe, back_peak_Xe)
Xe_table.to_csv("output/Xe/data.csv")
