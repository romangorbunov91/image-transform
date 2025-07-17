# version 1.2 by romangorbunov91
# 15-Jul-2025

from Functions.user_functions import indx_even

def daub_5_3_lift(f, int_flag):
    N = len(f)
    d = [0] * (N//2)
    a = [0] * (N//2)
    
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
    return a + d