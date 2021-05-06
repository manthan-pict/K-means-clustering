# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
center1 = np.array([[7.83816267, 2.49139275],
                        [8.06160243, 4.04423262]])
print(center1.ndim, center1.shape)

center2 = np.array([[7.83816267, 2.49139275],
                        [8.06160243, 4.04423262],
                        [6.11106851, 6.23497555],
                        [6.63352332, 0.98020705],
                        [7.94375954, 8.21165063],
                        [8.21897526, 8.9510505],
                        [6.63352332, 0.98020705],
                        [7.90345455, 2.28430161],
                        [7.56399709, 7.83135288],
                        [2.38952606, 7.22195564],
                        [8.21897526, 8.9510505],
                        [7.90345455, 2.28430161],
                        [3.0226944, 0.86402039],
                        [5.02471033, 8.23879873],
                        [1.51180219, 7.48293717]], dtype=np.float64)

print(center2.ndim, center2.shape)

# print("original center:", center)
# center1 = np.array([[2.05924902, 7.20598798],
#                     [2.05924902, 7.20598798],
#                     [8.06160243, 4.04423262],
#                     [6.11106851, 6.23497555],
#                     [6.63352332, 0.98020705],
#                     [7.94375954, 8.21165063],
#                     [8.21897526, 8.9510505],
#                     [6.63352332, 0.98020705],
#                     [7.90345455, 2.28430161],
#                     [7.56399709, 7.83135288],
#                     [2.38952606, 7.22195564],
#                     [8.21897526, 8.9510505],
#                     [7.90345455, 2.28430161],
#                     [3.0226944, 0.86402039],
#                     [5.02471033, 8.23879873],
#                     [1.51180219, 7.48293717]])
# print(AllSamples)
# print(center1)

# center[0][0] = 1
# center[0][1] = 1
# center[1][0] = 1
# center[1][1] = 1
# print("eucli :",euclidean_distance(center22[0], AllSamples[0]))
# print("eucli :vjberjfefbebhyu", center1[0], center1[1], np.allclose(center[0], center[1]))