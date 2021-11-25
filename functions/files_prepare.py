from random import randint

if __name__ == '__main__':
    arrayRandom = []
    arrayMinToMax = []
    arrayMaxToMin = []

    for i in range(0, 3490):
        arrayRandom.append(randint(0, 3490))
        arrayMinToMax.append(i + 1)

    with open('../arrays/arrayRandom.txt', 'w') as f:
        for item in arrayRandom:
            f.write("%s\n" % str(item))

    with open('../arrays/arrayMinToMax.txt', 'w') as f:
        for item in arrayMinToMax:
            f.write("%s\n" % str(item))

    with open('../arrays/arrayMaxToMin.txt', 'w') as f:
        for item in reversed(arrayMinToMax):
            f.write("%s\n" % str(item))
