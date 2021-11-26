import pandas as pd
import numpy as np
import mlp as newmlp
import mlp_PSO as mlp_pso
import csv
import os.path
import time

data = pd.read_csv("data_banknote_authentication.csv")
print("original dataset rows = {}".format(data.shape[0]))
print("original dataset columns = {}".format(data.shape[1]))

banknotes = pd.DataFrame(data)
training = banknotes.sample(frac=0.6)
test = banknotes.drop(training.index)

print("train data rows = {}".format(training.shape[0]))
print("train data columns = {}".format(training.shape[1]))
print("test data rows = {}".format(test.shape[0]))
print("test data columns = {}".format(test.shape[1]))

X_train = training.iloc[:, :4]
y_train = np.array(training.iloc[:, 4])

X_test = test.iloc[:, :4]
y_test = np.array(test.iloc[:, 4])

print()
myMLP_PSO = mlp_pso.MLP_PSO(2, [10, 1], [2, 1], 'cross_entropy')
print("Accuracy(%): "+str(myMLP_PSO.fit_and_transform(X_train, X_test, y_train, y_test, 30, 100, 10, 1, 1.5, 1.5, 1, 0.35)))
# learning_rate_list = [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]
#
# for epochs in range(4,60,4):
#     rowA = []
#     rowT = []
#     for numberOfNeurons in range(5,50,5):
#         for learningRate in learning_rate_list:
#             accuracy_avg = 0
#             duration_avg = 0
# for i in range(20):
#     start_time = time.time()
#
# myMLP = newmlp.MLP(2, [8, 1], ['Leaky_ReLU', 'sigmoid'], 0.5, 'cross_entropy')
# result = np.array(myMLP.fit_and_transform(X_train, X_test, y_train, 35))
#
# f = pd.concat([pd.DataFrame(result), pd.DataFrame(y_test)], axis=1)
# f.columns = ['result', 'Outcome']
# f['pred'] = f['result'].apply(lambda x: 0 if x < 0.5 else 1)
# accuracy = (f.loc[f['pred'] == f['Outcome']].shape[0] / f.shape[0] * 100)
# print("Accuracy (Loss minimization):")
# print(accuracy)
#
#     time_taken = time.time() - start_time
#
#     # accuracy_avg += accuracy
#     # duration_avg += time_taken
#
#     file_exists = os.path.isfile("results.csv")
#
# with open("results.csv", "a", newline='') as file:
#     header = ["Number of layers", "Number of neurons", "Activation functions", "Learning rate",
#               "Number of epochs",
#               "Type of loss function", "Accuracy", "Duration"]
#     writer = csv.writer(file)
#
#     if not file_exists:
#         # prints header into file if file doesn't exist yet, otherwise just prints results as row.
#         writer.writerow(header)
#
#     result_data = [myMLP.number_of_layers, myMLP.number_of_neurons, myMLP.activation_functions,
#                    myMLP.learning_rate,
#                    myMLP.epochs, myMLP.loss_function, accuracy, time_taken]
#     writer.writerow(result_data)
#         file.close()


#         rowA.append(accuracy_avg/20)
#         rowT.append(duration_avg/20)
#
# with open("newResultsA.csv", "a", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(rowA)
#     file.close()
#
# with open("newResultsT.csv", "a", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(rowT)
#     file.close()
# for i in range(20):

