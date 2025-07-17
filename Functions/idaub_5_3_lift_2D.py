# version 0.2 by romangorbunov91
# 15-Jul-2025

import numpy as np
from Functions.idaub_5_3_lift import idaub_5_3_lift

# Преобразование выполняется в следующей последовательности:
# 1. Изменение порядка строк (bottom-up).
# 2. Преобразование столбцов.
# 3. Изменение порядка строк (bottom-up).
# 4. Преобразование строк.

def idaub_5_3_lift_2D(coeff, int_flag):
    Nrow, Ncol = np.shape(coeff)
    if int_flag:
        coeff_row = np.zeros((Nrow, Ncol), dtype=int)
    else:
        coeff_row = np.zeros((Nrow, Ncol), dtype=float)
    
    # 1. Изменение порядка строк (bottom-up).
    coeff = np.flipud(coeff)
    
    # 2. Преобразование столбцов.
    # Предварительно - преобразуем столбцы в строки.
    coeff = coeff.T
    coeff_row = coeff_row.T
    for idx in range(Ncol):
        coeff_row[idx,:] = idaub_5_3_lift(coeff[idx,:], int_flag)
    
    # 3. Изменение порядка строк (bottom-up).
    # Предварительно - обратное преобразуем строки в столбцы.
    coeff_row = np.flipud(coeff_row.T)
  
    # 4. Преобразование строк.
    f = np.zeros_like(coeff_row)
    for idx in range(Nrow):
        f[idx,:] = np.array(idaub_5_3_lift(coeff_row[idx,:], int_flag))
 
    return f