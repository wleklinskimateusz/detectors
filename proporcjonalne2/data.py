import numpy as np


main_peak_Ar = np.array([
    702.75, 665.43, 700.31, 725.09,
    736.41, 678.50, 760.35, 766.17, 771.65
])
fwhm_Ar = np.array([
    130.43, 123.93, 121.93, 122.45,
    124.95, 113.49, 129.79, 129.94, 142.74
])

back_peak_Ar = np.array([
    353.43, 318.19, 324.57, 346.09,
    360.61, 337.27, 376.99, 362.87, 395.03
])
back_fwhm_Ar = np.array([
    15.68, 23.93, 62.59, 16.31, 10.11, 11.38, 10.75, 3.45, 3.26
])

V_Ar = np.array([1600 - 40 * i for i in range(len(fwhm_Ar))])

main_peak_Xe = np.array(
    [745.25, 670.16, 783.39, 695.48, 731.08, 693.05, 783.76, 769.48, 678.19, 739.3, 728.03, 721.31])
fwhm_Xe = np.array(
    [132.37, 119.36, 131.44, 121.86, 115.30,
        117.62, 122.63, 126.78, 112.63, 125.65, 123.3, 126.94]
)
back_peak_Xe = np.array(
    [207, 196.57, 220, 194.14, 172.81, 189.73,
        196.19, 216, 221.04, 204.01, 193.95, 192.83]
)
back_fwhm_Xe = np.array(
    [1.04, 5.10, 1.08, 1.46, 6.27, 9.79, 1.57, 1.45, 1.89, 15.40, 1.33, 1.25]
)

V_Xe = np.array([1940 + 40 * i for i in range(len(fwhm_Xe))])