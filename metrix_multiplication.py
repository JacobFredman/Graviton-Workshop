# import numpy as np
# import multiprocessing

# def matrix_multiply(size):
#     # Generate two random matrices
#     matrix_a = np.random.rand(size, size)
#     matrix_b = np.random.rand(size, size)

#     # Perform matrix multiplication
#     result = np.dot(matrix_a, matrix_b)
#     return result

# def worker(size):
#     while True:
#         matrix_multiply(size)

# def multiple_matrixes():
#     # Size of the matrices (e.g., 1000x1000)
#     matrix_size = 50

#     # Number of CPU cores
#     cpu_count = multiprocessing.cpu_count()

#     # Creating processes for each core
#     for i in range(cpu_count):
#         p = multiprocessing.Process(target=worker, args=(matrix_size,))
#         p.start()
#     return 'success'



import numpy as np
def multiple_matrixes():    
    # Creating two random matrices
    A = np.random.rand(10000, 10000)
    B = np.random.rand(10000, 10000)

    # Multiplying the matrices
    C = A @ B
    return 'success'
    # C now contains the product of A and B
