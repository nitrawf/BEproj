from .liver import forward_propagation
import pickle
import numpy as np

def result_liver(X):
    x = np.asarray(X)
    x = x.reshape(x.shape[0], 1)
    with open("Modules\liver_parameters.txt", "rb") as pr:
        data = pickle.load(pr)
    parameters = data["parameters"]
    mean = data["mean"]
    std = data["std"]
    x = (x-mean)/std
    result, _ = forward_propagation(x, parameters)
    return result



'''X = [10,125,70,26,115,31.1,0.205,41]
result = result_diabetus(X)
print(np.squeeze(result))'''