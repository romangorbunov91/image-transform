# version 1.4 by romangorbunov91
# 25-Jul-2025

import numpy as np
from Functions.user_functions import indx_even
# 'f' - input; np.array (int or float).
# 'coeff' - output; np.array (same type as input).
def daub_5_3_lift(f, int_flag):
    N = len(f)
    d = [0] * (N//2)
    a = [0] * (N//2)
    
    if int_flag:
        if not np.issubdtype(f.dtype, np.integer):
            f = f.astype(int)
    else:
        if np.issubdtype(f.dtype, np.integer):  
            f = f.astype(float)
        
    for k in range(N//2):
        if int_flag:
            d[k] = f[indx_even(2*k+1,N)] - (f[indx_even(2*k,N)] + f[indx_even(2*k+2,N)] + 1) //2
            if k == 0:
                a[k] = f[indx_even(2*k,N)] + (d[k] + 1) //2
            else:
                a[k] = f[indx_even(2*k,N)] + (d[k-1] + d[k] + 2) //4
        else:
            d[k] = f[indx_even(2*k+1,N)] - (f[indx_even(2*k,N)] + f[indx_even(2*k+2,N)]) /2
            if k == 0:
                a[k] = f[indx_even(2*k,N)] + d[k] /2
            else:
                a[k] = f[indx_even(2*k,N)] + (d[k-1] + d[k]) /4
    return np.array(a + d)