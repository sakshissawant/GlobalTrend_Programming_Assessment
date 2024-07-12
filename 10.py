import numpy as np

def transpose(matrix):
    new_matrix = []
    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[0]):
            new_matrix.append(matrix[j][i])
    Final = np.array(new_matrix)
    Final = Final.reshape(matrix.shape[1],matrix.shape[0])
    return Final
