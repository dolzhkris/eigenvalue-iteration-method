# eigenvalue-iteration-method
Finding the dominant eigenvalue and corresponding eigenvector of a symmetric matrix using the power iteration method in Python.

## About

The program allows the user to enter a matrix, performs several power iterations, and calculates an approximation of the largest eigenvalue and its corresponding eigenvector. The project was developed as part of university work during the second year of university.

## Key Variables

* matrix - input matrix;
* vector - right-hand side vector;
* n - size of the matrix;
* x - solution vector;
* x0 - initial approximation;
* x_new - updated approximation;
* EPS - convergence accuracy;
* max_iter - maximum number of iterations.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/eigenvalue-iteration-method.git
```

2. Install the required dependency:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python main.py
```

First, enter the dimension of the matrix:

```text
Введите размерность матрицы:
```

Then enter the matrix elements.
