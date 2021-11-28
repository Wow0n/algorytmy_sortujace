import numpy as np

if __name__ == '__main__':
    size = 500000

    arrayMinToMax = np.arange(1, size)
    arrayMaxToMin = arrayMinToMax[::-1]

    np.save("arrayMinToMax.npy", arrayMinToMax)
    np.save("arrayMaxToMin.npy", arrayMaxToMin)

    np.random.shuffle(arrayMinToMax)
    np.save("arrayRandom.npy", arrayMaxToMin)
