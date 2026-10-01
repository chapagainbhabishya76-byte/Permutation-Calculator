# Permutation-Calculator
A beginner-friendly Python package for calculating and working with permutations.

## What is a permutation?

A permutation calculates the number of ways to arrange `r` items chosen from `n` items.

\[
P(n, r) = \frac{n!}{(n-r)!}
\]

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/YOUR-USERNAME/permutation-calculator.git
```

Replace `YOUR-USERNAME` with your GitHub username.

## Usage

```python
from permutation_calculator import P

answer = P(6, 3)

print(answer)
# P(6, 3) = 120

print(answer.Value())
# 120
```

You can also use the result in arithmetic:

```python
from permutation_calculator import P

print(P(6, 3) + 10)
# 130

print(P(5, 2) * 2)
# 40
```

## Input rules

- `n` and `r` must be integers.
- Both values must be zero or positive.
- `n` must be greater than or equal to `r`.

## License

This project uses the MIT License.