import scipy.io


# trX - training set, each row represents a sample
# trY - training labels, 0 and 1 represent class 'tshirt' and class 'trouser' respectively
# tsX - testing set, each row represents a sample
# tsY - testing labels, 0 and 1 represent class 'tshirt' and class 'trouser' respectively

class Data:
    AllSamples = scipy.io.loadmat('C:/Users/magraw12/PycharmProjects/pythonProject/AllSamples.mat',
                           variable_names='AllSamples').get('AllSamples')

