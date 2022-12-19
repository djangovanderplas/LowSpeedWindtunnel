from matplotlib import pyplot as plt
import numpy as np
from dataframes import dfcp

point = 20 # Select which point to plot

alpha = dfcp.iloc[point][f'Alpha']

loc_up = ['100.00', '95.20', '90.10','85.20', '80.10', '75.00', '70.20', '65.00', '59.80', '55.20', '50.10', '45.20', '40.20', '35.10', '30.10', '25.00', '20.00', '15.10', '10.10', '8.90', '7.10', '5.50', '4.30', '3.10', '1.80', '0.80', '0.00']
loc_low = ['0.00', '0.60', '1.60', '3.00', '4.20', '5.40', '6.90', '8.40', '9.80', '15.00', '19.90', '24.90', '29.90', '34.90', '40.00', '45.00', '49.60', '55.10', '60.10', '65.00', '69.90', '75.00', '80.00', '85.00', '90.00', '95.20', '100.00']
print(len(loc_up))

up = []
cps_up = []
xc_up = []
xc_low = []
cps_low = []
for i in np.arange(1, 28, 1):
    if i < 10:
        value_up = -dfcp.iloc[point][f'Cpu_00{i}']
        value_low = -dfcp.iloc[point][f'Cpl_00{i}']
    else:
        value_up = -dfcp.iloc[point][f'Cpu_0{i}']
        value_low = -dfcp.iloc[point][f'Cpl_0{i}']
    xc_up.append(float(loc_up[i-1])/100)
    xc_low.append(float(loc_low[i-1])/100)
    cps_up.append(value_up)
    cps_low.append(value_low)

plt.title(f'Cp plot for {alpha}°')
plt.xlabel('x/c [-]')
plt.ylabel('-Cp [-]')
plt.plot(xc_up, cps_up, color='blue')
plt.plot(xc_low, cps_low, color='blue')
plt.grid()
plt.show()