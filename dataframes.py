import pandas as pd

# 2D Data
header2d = ['Alpha', 'Cd', 'Cl', 'Cm', 'Cn', 'Ct', 'Cd-press', 'Cl-press', 'Re', 'M', 'Q', 'V', 'Z_w.r.', 'Flap', 'Cpu_001', 'Cpu_002', 'Cpu_003', 'Cpu_004', 'Cpu_005', 'Cpu_006', 'Cpu_007', 'Cpu_008', 'Cpu_009', 'Cpu_010', 'Cpu_011', 'Cpu_012', 'Cpu_013', 'Cpu_014', 'Cpu_015', 'Cpu_016', 'Cpu_017', 'Cpu_018', 'Cpu_019', 'Cpu_020', 'Cpu_021', 'Cpu_022', 'Cpu_023', 'Cpu_024', 'Cpu_025', 'Cpu_026', 'Cpu_027', 'Cpl_001', 'Cpl_002', 'Cpl_003', 'Cpl_004', 'Cpl_005', 'Cpl_006', 'Cpl_007', 'Cpl_008', 'Cpl_009', 'Cpl_010', 'Cpl_011', 'Cpl_012', 'Cpl_013', 'Cpl_014', 'Cpl_015', 'Cpl_016', 'Cpl_017', 'Cpl_018', 'Cpl_019', 'Cpl_020', 'Cpl_021', 'Cpl_022', 'Cpl_023', 'Cpl_024', 'Cpl_025', 'Cpl_026', 'Cpl_027', 'Cn-corr', 'Ct-corr', 'Cm-corr']
df2d = pd.read_csv("Data Analysis/data/cpdata/2D/corr_test.txt", sep="\s+", skiprows=2, index_col=0)
df2d.columns = header2d

# 3D Data
header3d = ['Alpha', 'Beta', 'CL', 'CD', 'Cyaw', 'Cm_p_qc', 'Ct', 'Cn', 'Cside','Cm_roll', 'Cm_pitch', 'Cm_yaw', 'V', 'Re', 'M']
df3d = pd.read_csv("Data Analysis/data/cpdata/3D/corr_test.txt", sep="\s+", skiprows=2, index_col=0)
df3d.columns = header3d

# Xfoil Data
dfxfoil = pd.read_csv("Simulations/xflr5/SimResults/xfoil.csv", sep="\s+")

# XFLR5 Data
dfltt = pd.read_csv("Simulations/xflr5/SimResults/LTT.csv", sep="\s+")
dfpanels = pd.read_csv("Simulations/xflr5/SimResults/Panels.csv", sep="\s+")
dfvlm1 = pd.read_csv("Simulations/xflr5/SimResults/VLM1.csv", sep="\s+")
dfvlm2 = pd.read_csv("Simulations/xflr5/SimResults/VLM2.csv", sep="\s+")

# Cp data
dfcp = pd.read_csv("Data Analysis/data/cpdata/2D/corr_test.csv", sep="\s+")