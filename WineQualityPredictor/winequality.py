import numpy as np
from sklearn import tree
from sklearn import svm
from sklearn import linear_model
from sklearn import neighbors

# data loading
data = np.genfromtxt('winequality-red.csv',dtype= np.float32, delimiter = ';',
                    skip_header = 1,usecols = range(0,12))

X = data[:,range(0,11)]     # array holding the training samples
Y = data[:,11]              # array holding the class labels

# model building
classifier = []
classifier.append(tree.DecisionTreeClassifier(random_state=0))
classifier.append(svm.SVC(random_state=0))
classifier.append(linear_model.LogisticRegression(random_state=0))
classifier.append(neighbors.KNeighborsClassifier(n_neighbors= 5))

for i in range(len(classifier)):
    classifier[i] = classifier[i].fit(X,Y)

# main code
while True:
    # check menu choice
    print('1. Predict wine quality\n2. Quit\n')
    menu = int(input('> '))
    if menu == 2:
        break
    
    elif menu == 1:
        # store test_sample
        print('\nInput the values of a wine:')
        test_sample = []
        test_sample.append(float(input('1. fixed acidity: ')))
        test_sample.append(float(input('2. volatile acidity: ')))
        test_sample.append(float(input('3. citric acid: ')))
        test_sample.append(float(input('4. residual sugar: ')))
        test_sample.append(float(input('5. chlorides: ')))
        test_sample.append(float(input('6. free sulfur dioxide: ')))
        test_sample.append(float(input('7. total sulfur dioxide: ')))
        test_sample.append(float(input('8. density: ')))
        test_sample.append(float(input('9. pH: ')))
        test_sample.append(float(input('10. sulphates: ')))
        test_sample.append(float(input('11. alcohol: ')))
        test_samples = []
        test_samples.append(test_sample)

        # predict the class of the test sample
        print('\nPredicted wine quality:')
        predicted_class = classifier[0].predict(test_samples)
        print('1. Decision tree: {}'.format((int)(predicted_class[0])))
        predicted_class = classifier[1].predict(test_samples)
        print('2. Support vector machine: {}'.format((int)(predicted_class[0])))
        predicted_class = classifier[2].predict(test_samples)
        print('3. Logistic regression: {}'.format((int)(predicted_class[0])))
        predicted_class = classifier[3].predict(test_samples)
        print('4. k-NN classifier: {}\n'.format((int)(predicted_class[0])))
