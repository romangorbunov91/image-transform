import numpy as np
import pywt
from Functions.combine_matrices import combine_matrices
from Functions.split_matrices import split_matrices
from matplotlib import pyplot as plt
from PIL import Image

# Load a BMP image
image_path = 'images/couple.bmp'
img = Image.open(image_path)

# Display basic information about the image
print(f"Image Format: {img.format}")
print(f"Image Size: {img.size}")
print(f"Image Mode: {img.mode}")

f = (np.matrix(img) / 255).astype(float)

plt.imshow(f, cmap='gray')
plt.title('original')
plt.show()

K = 4
[Nrow, Ncol] = np.shape(f)

print('Total Energy (Signal)', np.sum(np.array(f)**2))

# Transform.
wavelet = 'haar'
tr = np.empty(K, dtype='object')

for k in range(K):
    if k == 0:
        tr[k] = f.copy()
    else:
        tr[k] = tr[k-1].copy()
    cA, (cH, cV, cD) = pywt.dwt2(tr[k][:Ncol//2**k,:Ncol//2**k], wavelet)
    tr[k][:Ncol//2**k,:Ncol//2**k] = combine_matrices(cA, cH, cV, cD)
    
# Inverse transform.
inv_tr = np.empty(K, dtype='object')

for k in reversed(range(K)):
    inv_tr[k] = tr[k].copy()
    cA, (cH, cV, cD) = split_matrices(tr[k][:Ncol//2**k,:Ncol//2**k])
    inv_tr[k][:Ncol//2**k,:Ncol//2**k] = pywt.idwt2((cA, (cH, cV, cD)), wavelet)

# Plot.
fig, axs = plt.subplots(ncols=K, nrows=1)
for k, ax in enumerate(axs.flat):
    ax.imshow(tr[k], cmap='gray', interpolation='none')
    ax.set_title('Level ' + str(k + 1))
    print('Total Energy', np.round(np.sum(np.array(tr[k])**2),1))
    print('Energy of trend subimage', np.round(np.sum(np.array(tr[k][:Ncol//2**k,:Ncol//2**k])**2),1))
plt.text(-350, -50, 'Transform', fontsize=14)
plt.show()

# Plot.
fig, axs = plt.subplots(ncols=K, nrows=1)
for k, ax in enumerate(axs.flat):
    ax.imshow(inv_tr[k], cmap='gray', interpolation='none')
    ax.set_title('Level ' + str(k))
plt.text(-350, -50, 'Inverse Transform', fontsize=14)
plt.show()

fig, axs = plt.subplots(ncols=K+1, nrows=1)
for k, ax in enumerate(axs.flat):
    if k == 0:
        ax.imshow(f, cmap='gray', interpolation='none')
        ax.set_title('original')
    else:    
        ax.imshow(tr[k-1][:Ncol//2**k,:Ncol//2**k], cmap='gray', interpolation='none')
        ax.set_title('Level ' + str(k))
plt.show()