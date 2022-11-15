import os
import numpy as np
import matplotlib.pyplot as plt


def analise_data(data_string):
    data = data_string.replace(",", ".").split("\n")
    V, I = [], []
    for line in data:
        element = line.split()
        V.append(float(element[0]))
        I.append(float(element[1]))

    V = np.array(V, dtype=float)
    I = np.array(I, dtype=float)
    eta = I / I.max()
    return V, I, eta


V_Sr_flat, I_Sr_flat, eta_Sr_flat = analise_data("""0,2	3
0,4	10
0,6	21
0,8	28,5
1	34
2	54
3	65
4	73
5	79
6	83
7	87
8	89
9	91
10	93
20	99
30	100
40	102
50	101,5
60	102
70	101,5
80	102
90	102
100	102
110	102
120	102
130	102""")

V_Fe_flat, I_Fe_flat, eta_Fe_flat = analise_data("""0,2	2,5
0,4	8
0,6	12
0,8	16
1	18
2	27
3	33
4	37
5	40
6	42
7	44
8	44,5
9	45
10	45,5
20	47,5
30	48
40	48
50	48,5
60	48,5
70	49
79,9	49
90	49
100	49
110	49
120,1	49
130	49""")

V_Sr_Cyl, I_Sr_Cyl, eta_Sr_Cyl = analise_data("""1	12,5
2	25,5
3	38,3
4	51,7
5	63,5
6	75,3
7	86,9
8	98
9	109
10	120
12	140,5
14	160
16	178
18	196
20	213,7
22	227
24	240,5
26	254
28	267
30	278
40	327
50	359
60	383
70	399
80	411
90	420
100	427
110	433
120	438
130	442""")

V_Fe_Cyl, I_Fe_Cyl, eta_Fe_Cyl = analise_data("""1	3,4
2	6,5
3	9,4
4	12,3
5	15,1
6	18
7	20,7
8	23,5
9	26,1
10	28,6
12	33,7
14	39
16	44
18	49
20	53,8
22	58,6
24	63,3
26	68,1
28	72,9
30	77,3
40	100
50	122
60	143
70	163
80	183
90	202
100	220
110	238
120	255
130	272""")

# if output doesn't exist, create it
if not os.path.exists("output"):
    os.makedirs("output")


def plot_I(V, I, label):
    plt.scatter(V, I)
    plt.xlabel("V [V]")
    plt.ylabel("I [nA]")
    plt.title(label)
    plt.savefig("output/" + label + ".png")
    plt.show()


def plot_eta(V, etaFe, etaSr, label):
    plt.scatter(V, etaFe, label="Fe")
    plt.scatter(V, etaSr, label="Sr")
    plt.xlabel("V [V]")
    plt.ylabel("eta")
    plt.title(label)
    plt.legend()
    plt.savefig("output/" + label + ".png")
    plt.show()


def plot_single_eta(V, eta, label):
    plt.scatter(V, eta)
    plt.xlabel("V [V]")
    plt.ylabel("eta")
    plt.title(label)
    plt.savefig("output/" + label + ".png")
    plt.show()


plot_single_eta(V_Sr_flat, eta_Sr_flat, "eta Sr dla płaskiej komory")
plot_single_eta(V_Fe_flat, eta_Fe_flat, "eta Fe dla płaskiej komory")

plot_single_eta(V_Sr_Cyl, eta_Sr_Cyl, "eta Sr dla cylindrycznej komory")
plot_single_eta(V_Fe_Cyl, eta_Fe_Cyl, "eta Fe dla cylindrycznej komory")

plot_eta(V_Sr_flat, eta_Fe_flat, eta_Sr_flat, "eta dla płaskiej komory")
plot_eta(V_Sr_Cyl, eta_Fe_Cyl, eta_Sr_Cyl, "eta dla cylindrycznej komory")

plot_I(V_Sr_Cyl, I_Sr_Cyl, "Prąd dla Sr w cylindrycznej komorze")
plot_I(V_Fe_Cyl, I_Fe_Cyl, "Prąd dla Fe w cylindrycznej komorze")

plot_I(V_Sr_flat, I_Sr_flat, "Prąd dla Sr w płaskiej komorze")
plot_I(V_Fe_flat, I_Fe_flat, "Prąd dla Fe w płaskiej komorze")
