# version 1.4 by romangorbunov91
# 25-Jul-2025

import numpy as np
from Functions.user_functions import indx_even
# 'coeff' - input; np.array (int or float).
# 'f' - output; np.array (same type as input).
def idaub_5_3_lift(coeff, int_flag):
    N = len(coeff)
    f = [0] * N
    
    if int_flag:
        if not np.issubdtype(coeff.dtype, np.integer):
            coeff = coeff.astype(int)
    else:
        if np.issubdtype(coeff.dtype, np.integer):  
            coeff = coeff.astype(float)
    
    a = coeff[:(N//2)]
    d = coeff[(N//2):]
    
    # odd-indexed values.
    if int_flag:
        # k == 0.
        f[0] = a[0] - (d[0] + 1) //2
        for k in range(1,N//2):
            f[2*k] = a[k] - (d[k-1] + d[k] + 2) //4
    else:
        # k == 0.
        f[0] = a[0] - d[0] /2
        for k in range(1,N//2):
            f[2*k] = a[k] - (d[k-1] + d[k]) /4
    
    # even-indexed values.
    if int_flag:
        for k in range(N//2):
            f[2*k+1] = d[k] + (f[2*k] + f[indx_even(2*k+2,N)] + 1) //2
    else:
        for k in range(N//2):
            f[2*k+1] = d[k] + (f[2*k] + f[indx_even(2*k+2,N)]) /2

    return f