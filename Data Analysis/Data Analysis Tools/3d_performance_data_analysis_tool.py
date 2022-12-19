import pandas as pd
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

header = ['Alpha', 'Beta', 'CL', 'CD', 'Cyaw', 'Cm_p_qc', 'Ct', 'Cn', 'Cside',
       'Cm_roll', 'Cm_pitch', 'Cm_yaw', 'V', 'Re', 'M']
df = pd.read_csv("../data/cpdata/3D/corr_test.txt", sep="\s+", skiprows=2, index_col=0)
df.columns = header

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 12))
plt.tight_layout(pad=5)
plt.suptitle(f'3D Performance Plots', size=15)

axes[0, 0].plot( df['Alpha'][:33], df['CL'][:33], marker='.', color='blue')
axes[0, 0].plot( df['Alpha'][32:], df['CL'][32:], label='Hysteresis', marker='.', color='red')
axes[0, 0].set_xlabel('Alpha [°]')
axes[0, 0].set_ylabel('CL [-]')
axes[0, 0].set_title('Lift Slope')
axes[0, 0].axhline(y=0, color='k')
axes[0, 0].axvline(x=0, color='k')
axes[0, 0].legend()
axes[0, 0].grid()

axes[0, 1].plot( df['Alpha'][:33], df['CD'][:33], marker='.', color='blue')
axes[0, 1].plot( df['Alpha'][32:], df['CD'][32:], label='Hysteresis', marker='.', color='red')
axes[0, 1].set_xlabel('Alpha [°]')
axes[0, 1].set_ylabel('CL [-]')
axes[0, 1].set_title('Drag Slope')
axes[0, 1].axhline(y=0, color='k')
axes[0, 1].axvline(x=0, color='k')
axes[0, 1].legend()
axes[0, 1].grid()

axes[0, 2].plot( df['CD'][:33], df['CL'][:33], marker='.', color='blue')
axes[0, 2].plot( df['CD'][32:], df['CL'][32:], label='Hysteresis', marker='.', color='red')
axes[0, 2].set_xlabel('CL [-]')
axes[0, 2].set_ylabel('CD [-]')
axes[0, 2].set_title('Drag Bucket')
axes[0, 2].axhline(y=0, color='k')
axes[0, 2].axvline(x=0, color='k')
axes[0, 2].legend()
axes[0, 2].grid()

axes[1, 0].plot( df['Alpha'][:33], df['Cm_pitch'][:33], marker='.', color='blue')
axes[1, 0].plot( df['Alpha'][32:], df['Cm_pitch'][32:], label='Hysteresis', marker='.', color='red')
axes[1, 0].set_xlabel('Alpha [°]')
axes[1, 0].set_ylabel('CM Pitch [-]')
axes[1, 0].set_title('Pitching Moment Curve')
axes[1, 0].axhline(y=0, color='k')
axes[1, 0].axvline(x=0, color='k')
axes[1, 0].legend()
axes[1, 0].grid()

axes[1, 1].plot( df['Alpha'][:33], df['Cm_yaw'][:33], marker='.', color='blue')
axes[1, 1].plot( df['Alpha'][32:], df['Cm_yaw'][32:], label='Hysteresis', marker='.', color='red')
axes[1, 1].set_xlabel('Alpha [°]')
axes[1, 1].set_ylabel('Cm Yaw [-]')
axes[1, 1].set_title('Yawing Moment curve')
axes[1, 1].axhline(y=0, color='k')
axes[1, 1].axvline(x=0, color='k')
axes[1, 1].legend()
axes[1, 1].grid()

axes[1, 2].plot( df['Alpha'][:33], df['Cn'][:33], marker='.', color='blue')
axes[1, 2].plot( df['Alpha'][32:], df['Cn'][32:], label='Hysteresis', marker='.', color='red')
axes[1, 2].set_xlabel('Alpha [°]')
axes[1, 2].set_ylabel('Cn [-]')
axes[1, 2].set_title('Cn-curve')
axes[1, 2].axhline(y=0, color='k')
axes[1, 2].axvline(x=0, color='k')
axes[1, 2].legend()
axes[1, 2].grid()
plt.show()