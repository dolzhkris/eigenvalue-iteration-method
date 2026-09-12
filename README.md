# eigenvalue-iteration-method
Finding the dominant eigenvalue and corresponding eigenvector of a symmetric matrix using the power iteration method in Python.

## About

The program allows the user to enter a matrix, performs several power iterations, and calculates an approximation of the largest eigenvalue and its corresponding eigenvector. The project was developed as part of university work during my second year of study.

## Example

The project uses the following symmetric matrix for the analytical solution:

```text
A =

┌                        ┐
│ 0.5   1.2   2.0   1.0  │
│ 1.2   2.0   0.6   1.2  │
│ 2.0   0.6   1.0   0.7  │
│ 1.0   1.2   0.7   1.8  │
└                        ┘
```

The eigenvalue problem is defined as:

```text
A · v = λ · v
```

or:

```text
(A - λE) · v = 0
```

where:

* `A` — input matrix;
* `λ` — eigenvalue;
* `v` — corresponding eigenvector;
* `E` — identity matrix.

For the given matrix, the analytical solution gives the following eigenvalues:

```text
λ₁ ≈ 1.358
λ₂ ≈ 0.700
λ₃ ≈ 1.266
λ₄ ≈ 4.692
```

The dominant eigenvalue is therefore approximately:

```text
λmax ≈ 4.692
```

The corresponding eigenvector is approximately:

```text
v ≈ (0.973, 1.078, 0.892, 1)ᵀ
```


## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/eigenvalue-iteration-method.git
```

2. Install the required dependency:

```bash
pip install -r requirements.txt
```

3.Run the program:

```bash
python main.py
```

First, enter the dimension of the matrix:

```text
Введите размерность матрицы:
```

Then enter the matrix elements.
