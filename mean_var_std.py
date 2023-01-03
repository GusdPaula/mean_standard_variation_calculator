import numpy as np


def calculate(list):
    n_array = np.array(list)

    try:
        
        n_matrix = n_array.reshape((3, 3))

    except ValueError:
        raise ValueError("List must contain nine numbers.")

    else:
        mean = [n_matrix.mean(axis=0).tolist(), n_matrix.mean(axis=1).tolist(), n_matrix.mean().tolist()]
        var = [n_matrix.var(axis=0).tolist(), n_matrix.var(axis=1).tolist(), n_matrix.var().tolist()]
        standard_deviation = [n_matrix.std(axis=0).tolist(), n_matrix.std(axis=1).tolist(), n_matrix.std().tolist()]
        max = [n_matrix.max(axis=0).tolist(), n_matrix.max(axis=1).tolist(), n_matrix.max().tolist()]
        min = [n_matrix.min(axis=0).tolist(), n_matrix.min(axis=1).tolist(), n_matrix.min().tolist()]
        sum = [n_matrix.sum(axis=0).tolist(), n_matrix.sum(axis=1).tolist(), n_matrix.sum().tolist()]

        calculations = {
            'mean': mean,
            'variance': var,
            'standard deviation': standard_deviation,
            'max': max,
            'min': min,
            'sum': sum
        }

    return calculations
