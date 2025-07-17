# version 0.3 by romangorbunov91
# 15-Jul-2025

import numpy as np
from Functions.daub_5_3_lift import daub_5_3_lift
# Преобразование выполняется в следующей последовательности:
# 1. Преобразование строк.
# 2. Изменение порядка строк (bottom-up).
# 3. Преобразование столбцов.
# 4. Изменение порядка строк (bottom-up).

def daub_5_3_lift_2D(f, int_flag):
    Nrow, Ncol = np.shape(f)
    if int_flag:
        coeff_row = np.zeros((Nrow, Ncol), dtype=int)
    else:
        coeff_row = np.zeros((Nrow, Ncol), dtype=float)
        
    # 1. Преобразование строк.
    for idx in range(Nrow):
        coeff_row[idx,:] = daub_5_3_lift(f[idx,:], int_flag)
    
    # 2. Изменение порядка строк (bottom-up).
    coeff_row = np.flipud(coeff_row)
        
    # 3. Преобразование столбцов.
    # Предварительно - преобразуем столбцы в строки.
    coeff_row = coeff_row.T
    coeff = np.zeros_like(coeff_row)
    for idx in range(Ncol):
        coeff[idx,:] = np.array(daub_5_3_lift(coeff_row[idx,:], int_flag))
    
    # 4. Изменение порядка строк (bottom-up).
    # Предварительно - обратное преобразуем строки в столбцы.
    return np.flipud(coeff.T)