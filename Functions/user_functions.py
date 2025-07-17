# version 1.0 by romangorbunov91
# 15-Jul-2025

# Функция преобразования индексов по правилу "even symmetry".
def indx_even(k, N):
    reminder = abs(k) % (2*(N-1))
    if reminder <= (N-1):
        # rise
        return reminder
    else:
        # fall
        return 2*(N-1) - reminder