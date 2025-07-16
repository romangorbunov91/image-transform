# 2D (Image) Transform
## Исходное изображение
Импортирована монохромная картинка размером 512x512.

В [notebook.ipynb](notebook.ipynb) реализован кратномасштабный анализ этого двумерного массива с возможностью выбирать тип вейвлета.

<img src='readme_img/original.png' style='width:100%; height:auto;'>

## Кратномасштабный анализ

<img src='readme_img/transform.png' style='width:100%; height:auto;'>

## Реконструкция массива

<img src='readme_img/reconstruction.png' style='width:100%; height:auto;'>

<img src='readme_img/comparison.png' style='width:100%; height:auto;'>

## Энергия трендовой составляющей в зависимости от уровня разложения

<img src='readme_img/trends.png' style='width:100%; height:auto;'>
<img src='readme_img/energy_pywt.png' style='width:100%; height:auto;'>

## Пользовательские функции
- [split_matrices.py](Functions/split_matrices.py) - расчленяет исходную матрицу симметрично на 4 составляющие cA, cH, cV, cD, в соответствии со схемой PyWavelet.
- [combine_matrices.py](Functions/combine_matrices.py) - объединяет cA, cH, cV, cD в единую матрицу в соответствии со схемой PyWavelet.

<img src='readme_img/2D_wavelet.png' style='width:60%; height:auto;'>

[Link](https://pywavelets.readthedocs.io/en/latest/ref/2d-dwt-and-idwt.html)