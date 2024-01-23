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



import random
import string
import numpy as np

# create a function to shortening url
def create_short_url(url):
    try:
        # create a random string of length 5
        letters = string.ascii_lowercase
        short_url = ''.join(random.choice(letters) for i in range(10))
        # append the random string generated to the url
        return short_url
    except Exception as e:
        return str(e)

# result = shorten_url('https://www.google.com/my-page-of-random-text')
# print(result)
