import random
import MyData

def RoleANumber(percentage):
    random_value = random.random() * 100  
    return 1 if random_value < percentage else 0


def GenerateBaisWeight():
    data = {}
    HiddenLayerNeuron = [784,100,50,10]
    for i in range(0,len(HiddenLayerNeuron)):
        data[f"Layer_{i}"] = {}
        for j in range (0,HiddenLayerNeuron[i]):
            data[f"Layer_{i}"][f"Neuron{j}"] = []
            if i != 0:
                for k in range(0,HiddenLayerNeuron[i-1]+1):
                    data[f"Layer_{i}"][f"Neuron{j}"].append(random.random())
    return data


def MutateBaisWeight(percentage,data):
    for i in range (1, len(data)):
        for j in range(0,len(data[f"Layer_{i}"])):
            for y in range(0,len(data[f"Layer_{i}"][f"Neuron{j}"])):
                if RoleANumber(percentage) == 1:
                    data[f"Layer_{i}"][f"Neuron{j}"][y] = random.random()
    return data
