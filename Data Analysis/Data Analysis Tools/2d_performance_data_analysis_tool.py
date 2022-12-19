import pandas as pd
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

header = ['Alpha', 'Cd', 'Cl', 'Cm', 'Cn', 'Ct', 'Cd-press', 'Cl-press', 'Re', 'M', 'Q', 'V', 'Z_w.r.', 'Flap', 'Cpu_001', 'Cpu_002', 'Cpu_003', 'Cpu_004', 'Cpu_005', 'Cpu_006', 'Cpu_007', 'Cpu_008', 'Cpu_009', 'Cpu_010', 'Cpu_011', 'Cpu_012', 'Cpu_013', 'Cpu_014', 'Cpu_015', 'Cpu_016', 'Cpu_017', 'Cpu_018', 'Cpu_019', 'Cpu_020', 'Cpu_021', 'Cpu_022', 'Cpu_023', 'Cpu_024', 'Cpu_025', 'Cpu_026', 'Cpu_027', 'Cpl_001', 'Cpl_002', 'Cpl_003', 'Cpl_004', 'Cpl_005', 'Cpl_006', 'Cpl_007', 'Cpl_008', 'Cpl_009', 'Cpl_010', 'Cpl_011', 'Cpl_012', 'Cpl_013', 'Cpl_014', 'Cpl_015', 'Cpl_016', 'Cpl_017', 'Cpl_018', 'Cpl_019', 'Cpl_020', 'Cpl_021', 'Cpl_022', 'Cpl_023', 'Cpl_024', 'Cpl_025', 'Cpl_026', 'Cpl_027', 'Cn-corr', 'Ct-corr', 'Cm-corr']
df2d = pd.read_csv("../data/cpdata/2D/corr_test.txt", sep="\s+", skiprows=2, index_col=0)
df2d.columns = header

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 12))
plt.tight_layout(pad=5)
plt.suptitle(f'2D Performance Plots', size=15)

axes[0, 0].plot(df2d['Alpha'][:33], df2d['Cl'][:33], marker='.', color='blue')
axes[0, 0].plot(df2d['Alpha'][31:], df2d['Cl'][31:], label='Hysteresis', marker='.', color='red')
axes[0, 0].set_xlabel('Alpha [°]')
axes[0, 0].set_ylabel('Cl [-]')
axes[0, 0].set_title('Lift Slope')
axes[0, 0].axhline(y=0, color='k')
axes[0, 0].axvline(x=0, color='k')
axes[0, 0].legend()
axes[0, 0].grid()

axes[0, 1].plot(df2d['Alpha'][:33], df2d['Cd'][:33], marker='.', color='blue')
axes[0, 1].plot(df2d['Alpha'][31:], df2d['Cd'][31:], label='Hysteresis', marker='.', color='red')
axes[0, 1].set_xlabel('Alpha [°]')
axes[0, 1].set_ylabel('Cl [-]')
axes[0, 1].set_title('Drag Slope')
axes[0, 1].axhline(y=0, color='k')
axes[0, 1].axvline(x=0, color='k')
axes[0, 1].legend()
axes[0, 1].grid()

axes[0, 2].plot(df2d['Cd'][:33], df2d['Cl'][:33], marker='.', color='blue')
axes[0, 2].plot(df2d['Cd'][31:], df2d['Cl'][31:], label='Hysteresis', marker='.', color='red')
axes[0, 2].set_xlabel('Cd [-]')
axes[0, 2].set_ylabel('Cl [-]')
axes[0, 2].set_title('Drag Bucket')
axes[0, 2].axhline(y=0, color='k')
axes[0, 2].axvline(x=0, color='k')
axes[0, 2].legend()
axes[0, 2].grid()

axes[1, 0].plot(df2d['Alpha'][:33], df2d['Cm'][:33], marker='.', color='blue')
axes[1, 0].plot(df2d['Alpha'][31:], df2d['Cm'][31:], label='Hysteresis', marker='.', color='red')
axes[1, 0].set_xlabel('Alpha [°]')
axes[1, 0].set_ylabel('Cm [-]')
axes[1, 0].set_title('Moment Curve')
axes[1, 0].axhline(y=0, color='k')
axes[1, 0].axvline(x=0, color='k')
axes[1, 0].legend()
axes[1, 0].grid()

axes[1, 1].plot(df2d['Alpha'][:33], df2d['Cn'][:33], marker='.', color='blue')
axes[1, 1].plot(df2d['Alpha'][31:], df2d['Cn'][31:], label='Hysteresis', marker='.', color='red')
axes[1, 1].set_xlabel('Alpha [°]')
axes[1, 1].set_ylabel('Cn [-]')
axes[1, 1].set_title('Cn-curve')
axes[1, 1].axhline(y=0, color='k')
axes[1, 1].axvline(x=0, color='k')
axes[1, 1].legend()
axes[1, 1].grid()

axes[1, 2].plot(df2d['Alpha'][:33], df2d['Ct'][:33], marker='.', color='blue')
axes[1, 2].plot(df2d['Alpha'][31:], df2d['Ct'][31:], label='Hysteresis', marker='.', color='red')
axes[1, 2].set_xlabel('Alpha [°]')
axes[1, 2].set_ylabel('Ct [-]')
axes[1, 2].set_title('Ct-curve')
axes[1, 2].axhline(y=0, color='k')
axes[1, 2].axvline(x=0, color='k')
axes[1, 2].legend()
axes[1, 2].grid()
plt.show()