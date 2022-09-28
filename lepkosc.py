from cProfile import label
from cmath import log10
from distutils.log import Log
from re import A
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math


from setuptools import Command

window = tk.Tk()

window.title("Predominance Area Diagram")
window.geometry('492x420+492+420')

temperatura_podaj = tk.Label(text="Temperature ["+u'\u00B0'+"C]:")
temperatura_podaj.place(x=5, y=5)

lista_temp = []
entry = tk.Entry()
entry.place(x=130, y=5)
chemia = tk.Label(text="Chemical composition")
chemia.place(x=5, y=30)
entry_SiO2 = tk.Entry()
entry_SiO2.place(x=50, y=50)
entry_TiO2 = tk.Entry()
entry_TiO2.place(x=50, y=70)
entry_Al2O3 = tk.Entry()
entry_Al2O3.place(x=50, y=90)
entry_FeO = tk.Entry()
entry_FeO.place(x=50, y=110)
entry_Fe2O3 = tk.Entry()
entry_Fe2O3.place(x=50, y=130)
entry_MnO = tk.Entry()
entry_MnO.place(x=50, y=150)
entry_CaO = tk.Entry()
entry_CaO.place(x=50, y=170)
entry_MgO = tk.Entry()
entry_MgO.place(x=50, y=190)
entry_Na2O = tk.Entry()
entry_Na2O.place(x=50, y=210)
entry_K2O = tk.Entry()
entry_K2O.place(x=50, y=230)
entry_PbO = tk.Entry()
entry_PbO.place(x=50, y=250)
entry_ZnO = tk.Entry()
entry_ZnO.place(x=50, y=270)
entry_Cu2O = tk.Entry()
entry_Cu2O.place(x=50, y=290)
entry_P2O5 = tk.Entry()
entry_P2O5.place(x=50, y=310)
entry_Cr2O3 = tk.Entry()
entry_Cr2O3.place(x=50, y=330)
entry_ZrO2 = tk.Entry()
entry_ZrO2.place(x=50, y=350)
entry_CaF2 = tk.Entry()
entry_CaF2.place(x=50, y=350)
entry_S = tk.Entry()
entry_S.place(x=50, y=370)
entry_NiO = tk.Entry()
entry_NiO.place(x=50, y=390)

#określenie stałych globalnych
SiO2 = 0
SiO2_m = 0
TiO2 = 0
TiO_m = 0
Al2O3 = 0
Al2O3_m = 0
FeO = 0
FeO_m = 0
Fe2O3 = 0
Fe2O3_m = 0
MnO = 0
MnO_m = 0
CaO = 0
CaO_m = 0
MgO = 0
MgO_m = 0
Na2O = 0
Na2O_m = 0
K2O = 0
K2O_m = 0
PbO = 0
PbO_m = 0
ZnO = 0
ZnO_m = 0
Cu2O = 0
Cu2O_m = 0
P2O5 = 0
P2O5_m = 0
Cr2O3 = 0 
Cr2O3_m = 0 
ZrO2 = 0
ZrO2_m = 0
CaF2 = 0
CaF2_m = 0
S = 0
NiO = 0
suma_m = 0
SiO2_pm = 0
TiO_pm = 0
Al2O3_pm = 0
FeO_pm = 0
Fe2O3_pm = 0
MnO_pm = 0
CaO_pm = 0
MgO_pm = 0
Na2O_pm = 0
K2O_pm = 0
PbO_pm = 0
ZnO_pm = 0
Cu2O_pm = 0
P2O5_pm = 0
Cr2O3_pm = 0 
ZrO2_pm = 0
CaF2_pm = 0
#model Giordano
AE = 0
SM = 0
lista_b1 = []
lista_b2 = []
lista_b3 = []
lista_b4 = []
lista_lepkosc = []
lista_temp =[1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400,]
b1_temp = 0
b2_temp = 0
b3_temp = 0
b4_temp = 0
temp = 0
CR=0
Battle_Hager = 0
Reddy_Zhang = 0
#model UW
lista_UW = []
lista_Altman =[]

#okienka zaznaczenia
giordano = tk.IntVar() # zmienna przechowująca dane typu int, która zostanie przypisana do kontrolki
checkbutton = tk.Checkbutton(window, text='Giordano et al. (log' + u'\u03B7'+')', variable=giordano, \
                         onvalue=1, offvalue=0).place(x=200, y=80)
Utigard_Warczok = tk.IntVar() # zmienna przechowująca dane typu int, która zostanie przypisana do kontrolki
checkbutton = tk.Checkbutton(window, text='Utigard & Warczok (log' + u'\u03B7'+')', variable=Utigard_Warczok, \
                         onvalue=1, offvalue=0).place(x=200, y=100)
Altman = tk.IntVar() 
checkbutton = tk.Checkbutton(window, text='Altman et al.(log' + u'\u03B7'+')', variable=Altman, \
                         onvalue=1, offvalue=0).place(x=200, y=120)
Reddy_Zhangb = tk.IntVar() 
checkbutton = tk.Checkbutton(window, text='Reddy_Zhang (ln' + u'\u03B7'+')', variable=Reddy_Zhangb, \
                         onvalue=1, offvalue=0).place(x=200, y=140)

def obliczenia(event):
    global temp
    temp = int(entry.get())
    temp = float(temp)
    global SiO2
    SiO2 = float(entry_SiO2.get())
    global SiO2_m
    SiO2_m = float(SiO2/60.0843)
    global TiO2
    TiO2 = float(entry_TiO2.get())
    global TiO_m
    TiO2_m = float(TiO2/79.8658)
    global Al2O3
    Al2O3 = float(entry_Al2O3.get())
    global Al2O3_m
    Al2O3_m = float(Al2O3/101.9612)
    global FeO
    FeO = float(entry_FeO.get())
    global FeO_m
    FeO_m = float(FeO/71.8464)
    global Fe2O3
    Fe2O3 = float(entry_Fe2O3.get())
    global Fe2O3_m
    Fe2O3_m = float(Fe2O3/159.69)
    global MnO
    MnO = float(entry_MnO.get())
    global MnO_m
    MnO_m = float(MnO/75.9375)
    global CaO
    CaO = float(entry_CaO.get())
    global CaO_m
    CaO_m = float(CaO/56.0774)
    global MgO
    MgO = float(entry_MgO.get())
    global MgO_m
    MgO_m = float(MgO/40.3044)
    global Na2O
    Na2O = float(entry_Na2O.get())
    global Na2O_m
    Na2O_m = float(Na2O/61.979)
    global K2O
    K2O = float(entry_K2O.get())
    global K2O_m
    K2O_m = float(K2O/94.196)
    global PbO
    PbO = float(entry_PbO.get())
    global PbO_m
    PbO_m = float(PbO/223.1994)
    global ZnO
    ZnO = float(entry_ZnO.get())
    global ZnO_m
    ZnO_m = float(ZnO/81.41)
    global Cu2O
    Cu2O = float(entry_Cu2O.get())
    global Cu2O_m
    Cu2O_m = float(Cu2O/143.08)
    global P2O5
    P2O5 = float(entry_P2O5.get())
    global P2O5_m
    P2O5_m = float(P2O5/141.944)
    global Cr2O3
    Cr2O3 = float(entry_Cr2O3.get())
    
    global Cr2O3_m
    Cr2O3_m = float(Cr2O3/151.99)
    global ZrO2
    ZrO2 = float(entry_ZrO2.get())
    global ZrO2_m
    ZrO2_m = float(ZrO2/123.218)
    global suma_m
    suma_m = SiO2_m + TiO2_m + Al2O3_m + FeO_m +Fe2O3_m + MnO_m + CaO_m + MgO_m + Na2O_m + K2O_m + PbO_m + ZnO_m + Cu2O_m + P2O5_m + Cr2O3_m + ZrO2_m
    global SiO2_pm
    SiO2_pm = float(SiO2_m * 100/suma_m)
    global TiO_pm
    TiO_pm = float(TiO2_m * 100/suma_m)
    global Al2O3_pm
    Al2O3_pm = float(Al2O3_m * 100/suma_m)
    global Fe2O3_pm
    FeO_pm = float(FeO_m * 100/suma_m)
    global Fe2O3_pm
    Fe2O3_pm = float(Fe2O3_m * 100/suma_m)
    global MnO_pm
    MnO_pm = float(MnO_m * 100/suma_m)
    global CaO_pm
    CaO_pm = float(CaO_m * 100/suma_m)
    global MgO_pm
    MgO_pm = float(MgO_m * 100/suma_m)
    global Na2O_pm
    Na2O_pm = float(Na2O_m * 100/suma_m)
    global K2O_pm
    K2O_pm = float(K2O_m * 100/suma_m)
    global PbO_pm
    PbO_pm = float(PbO_m * 100/suma_m)
    global ZnO_pm
    ZnO_pm = float(ZnO_m * 100/suma_m)
    global Cu2O_pm
    Cu2O_pm = float(Cu2O_m * 100/suma_m)
    global P2O5_pm
    P2O5_pm = float(P2O5_m * 100/suma_m)
    global AE
    #model Giordano
    global AE
    AE = (Na2O_pm + K2O_pm - Al2O3_pm)
    global SM
    SM = ((FeO_pm/2) + MnO_pm + CaO_pm + MgO_pm +Na2O_pm + K2O_pm)
    global b1_temp
    b1_temp = (-33.5556+0.0351623*temp)/(1-0.0022362*temp-0.00000166697*temp **2) 
    global b2_temp
    b2_temp = (-93.6494+0.2317411*temp)/(1-0.0054597*temp+0.00001361072*temp**2) 
    global b3_temp
    b3_temp = (45.575455-0.0780935*temp)/(1-0.0036108*temp-0.0000000217*temp**2)
    global b4_temp
    b4_temp = (-0.00001292391*(AE/SM)*(temp**2)+0.03577545*(AE/SM)*temp-24.3366274*(AE/SM))
    global lepkosc_temp
    lepkosc_temp = (b1_temp+(b2_temp*b3_temp)/(b3_temp+SM)+b4_temp)
    lepkosc_temp = round(lepkosc_temp, 2)
    label_giordano2 = tk.Label(text= lepkosc_temp).place(x=340, y=80)
    #model UW
    global VR
    VR = (((SiO2 + (1.5 * Cr2O3) + (1.2 * ZrO2) + (1.8 * Al2O3))/((1.2 * FeO) + (0.5 * (Fe2O3 + PbO)) + (0.8 * MgO) + (0.7 * CaO) + (2.3 * (Na2O + K2O)) + (0.7 * Cu2O) + (1.6 * CaF2)))**0.5)
    UW = -0.49 - 5.1 * VR + (-3660 + 12080 *VR)/(temp + 273)
    UW = round(UW, 2)
    label_UW_lb = tk.Label(text= UW).place(x=340, y=100)
    global CR
    CR = (SiO2 + Al2O3 + MgO)/(CaO + FeO + (Fe2O3/1.43*1.287) + ZnO + S)
    Altman = 1.06 * (math.log(CR,10)) + 6801.2/(temp + 273) - 3.9881
    Altman = round(Altman,2)
    label_altman = tk.Label(text=Altman).place(x=340, y = 120)
    WP = ((CaO + MgO+ ZnO + PbO + (Cu2O/0.4440938 * 1.252) + FeO + Fe2O3)/(SiO2 + Al2O3))
    global Reddy_Zhang
    Reddy_Zhang = ((((-575715.3740 * 10**-5) + ((-389437.4952*10**-6 * SiO2) + (-390404.5030*10**-6*Al2O3))) + (((786518.4490*10**-4) + ((-771212.5136*10**-6*MgO) + (-800472.4918*10**-6*CaO) + (-784229.3480*10**-6*ZnO) + (-791899.5395*10**-6*(FeO + Fe2O3/1.43*1.287))+ (-788793.4502*10**-6*PbO) + (-610832.3709*10**-6*(Cu2O/0.4440938 * 1.252)) + (-431765.0764*10**-6*NiO)+ (-902650.2835*10**-6*S)+ (-688434.7979*10**-6*(TiO2 +MnO + Na2O + K2O)))) * 10**3)/(temp + 273)))
    #Reddy_Zhang = ((-31.981886 + (0.543124* SiO2 + 0.548868*Al2O3)) + ((-26.840100 + (0.742236*MgO + 0.683681*CaO + 0.676625*ZnO + 0.673338*(FeO + Fe2O3/1.43*1.287)+ 0.717893*PbO + 0.785696*(Cu2O/0.4440938 * 1.252) + 0.677901*NiO+ 0.588837*S+ 0.737147*(TiO2 +MnO + Na2O + K2O))) * 10**3)/(temp + 273))

   
    Reddy_Zhang = round(Reddy_Zhang,2)

    label_Reddy_Zhang = tk.Label(text=Reddy_Zhang).place(x=340, y = 140)
    
    
     #Urbain model
    #XG = SiO2_pm + P2O5_pm
    #XM = CaO_pm + MgO_pm + FeO_pm + MnO_pm + Na2O_pm + K2O_pm + 2 * (TiO_pm + ZrO2_pm) + CaF2_pm
    #XA = Al2O3_pm + Fe2O3_pm + Cr2O3_pm
    #alfa = XM/(XM + XA)
    #b0_Urbain = float(13.8 + 39.9355 * alfa - 44.049 * alfa ** 2)
    #b0_Urbain = round(b0_Urbain, 2)
    #b1_Urbain = float(30.481 - 117.1505 * alfa +129.9978 * alfa ** 2)
    #b1_Urbain = round(b1_Urbain, 2)
    #b2_Urbain = float(-40.9429 + 234.0486 * alfa - 300.04 * alfa ** 2)
    #b2_Urbain = round(b2_Urbain, 2)
    #b3_Urbain = float(60.7619 - 153.9276 * alfa +211.1616 * alfa **2)
    #b3_Urbain = round(b3_Urbain, 2)
    #b_Urbain = (b0_Urbain + b1_Urbain * SiO2_pm + (b2_Urbain * SiO2_pm ** 2)  + (b3_Urbain * SiO2_pm **3))
    #a_Urbain = float(2.71828 ** (-0.2693 * b_Urbain - 13.9751))
    #lepkosc_Urbain = float(a_Urbain * (temp + 273) * 2.71828 ** ((b_Urbain * 1000)/(temp + 273)))
    #lepkosc_Urbain = round(lepkosc_Urbain, 5)


def plotting(event):
    lista_b1 = [(-33.5556+0.0351623*x)/(1-0.0022362*x-0.00000166697*x **2) for x in lista_temp]
    lista_b2 = [(-93.6494+0.2317411*x)/(1-0.0054597*x+0.00001361072*x**2) for x in lista_temp]
    lista_b3 = [(45.575455-0.0780935*x)/(1-0.0036108*x-0.0000000217*x**2) for x in lista_temp]
    lista_b4 = [(-0.00001292391*(AE/SM)*(x**2)+0.03577545*(AE/SM)*x-24.3366274*(AE/SM)) for x in lista_temp]
    lista_lepkosc = []
    for i in range(len(lista_temp)):
        lista_lepkosc.append(lista_b1[i]+(lista_b2[i]*lista_b3[i])/(lista_b3[i]+SM)+lista_b4[i])
    #UW model
    lista_UW = [(-0.49 - 5.1 * VR + (-3660 + 12080 *VR)/(x + 273)) for x in lista_temp]
    lista_Altman = [(1.06 * (math.log(CR,10)) + 6801.2/(x + 273) - 3.9881) for x in lista_temp]
    #dane z zestawienia
    #lista_Reddy_Zhang = [((((-575715.3740 * 10**-5) + ((-389437.4952*10**-6 * SiO2) + (-390404.5030*10**-6*Al2O3))) + (((786518.4490*10**-4) + ((-771212.5136*10**-6*MgO) + (-800472.4918*10**-6*CaO) + (-784229.3480*10**-6*ZnO) + (-791899.5395*10**-6*(FeO + Fe2O3/1.43*1.287))+ (-788793.4502*10**-6*PbO) + (-610832.3709*10**-6*(Cu2O/0.4440938 * 1.252)) + (-431765.0764*10**-6*NiO)+ (-902650.2835*10**-6*S)+ (-688434.7979*10**-6*(TiO2 +MnO + Na2O + K2O)))) * 10**3)/(x + 273))**0.1) for x in lista_temp]
    #dane ze źródła
    global lista_Reddy_Zhang
    lista_Reddy_Zhang = [((((-31.981886) + ((0.543124* SiO2) + (0.548868*Al2O3))) + (((-26.840100) + ((0.742236*MgO) + (0.683681*CaO) + (0.676625*ZnO) + (0.673338*(FeO + Fe2O3/1.43*1.287))+ (0.717893*PbO) + (0.785696*(Cu2O/0.4440938 * 1.252)) + (0.677901*NiO)+ (0.588837*S)+ (0.737147*(TiO2 +MnO + Na2O + K2O)))) * 10**3)/(x + 273))) for x in lista_temp]


    if giordano.get() == 1:
        plt.plot(lista_temp, lista_lepkosc, color = 'r', linestyle = '-', label = 'Giordano et al. (log' + u'\u03B7'+')')
    if Utigard_Warczok.get() == 1:
        plt.plot(lista_temp, lista_UW, color = 'g', linestyle = '-', label = 'Utigard & Warczok (log' + u'\u03B7'+')')
    if Altman.get() == 1:
        plt.plot(lista_temp, lista_Altman, color = 'y', linestyle = '-', label = 'Altman et al.(log' + u'\u03B7'+')')
    if Reddy_Zhangb.get() == 1:
        plt.plot(lista_temp, lista_Reddy_Zhang, color = 'b', linestyle = '-', label = 'Reddy&Zhang(ln' + u'\u03B7'+')')
    
    
    plt.legend(loc=4)

    plt.xlabel('Temperature ['+u'\u00B0'+'C]')
    plt.ylabel('Viscosity')
    
    # rendering the plot
    plt.show()
    

button = tk.Button(text="Calculate")
button.bind("<Button-1>", obliczenia)

button.pack()
button.place(x=280, y=2)

button2 = tk.Button(text="Plot diagram")
button2.bind("<Button-1>", plotting)


button2.pack()
button2.place(x=200, y=40)

#
label_SiO2 = tk.Label(text = 'SiO2').place(x=10, y=50)
label_TiO2 = tk.Label(text = 'TiO2').place(x=10, y=70)
label_Al2O3 = tk.Label(text = 'Al2O3').place(x=10, y=90)
label_FeO = tk.Label(text = 'FeO').place(x=10, y=110)
label_Fe2O3 = tk.Label(text = 'Fe2O3').place(x=10, y=130)
label_MnO = tk.Label(text = 'MnO').place(x=10, y=150)
label_CaO = tk.Label(text = 'CaO').place(x=10, y=170)
label_MgO = tk.Label(text = 'MgO').place(x=10, y=190)
label_Na2O = tk.Label(text = 'Na2O').place(x=10, y=210)
label_K2O = tk.Label(text = 'K2O').place(x=10, y=230)
label_PbO = tk.Label(text = 'PbO').place(x=10, y=250)
label_ZnO = tk.Label(text = 'ZnO').place(x=10, y=270)
label_Cu2O = tk.Label(text = 'Cu2O').place(x=10, y=290)
label_P2O5 = tk.Label(text = 'P2O5').place(x=10, y=310)
label_Cr2O3 = tk.Label(text = 'Cr2O3').place(x=10, y=330)
label_ZrO2 = tk.Label(text = 'ZrO2').place(x=10, y=350)
label_S = tk.Label(text = 'S').place(x=10, y=370)
label_NiO = tk.Label(text = 'NiO').place(x=10, y=390)
                                                

window.mainloop()