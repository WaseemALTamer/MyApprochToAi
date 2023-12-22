import MyData
import random

data = {}

HiddenLayerNeuron = [784,392,196,10]




for i in range(0,len(HiddenLayerNeuron)):
    data[f"Layer_{i}"] = {}
    for j in range (0,HiddenLayerNeuron[i]):
        data[f"Layer_{i}"][f"Neuron{j}"] = []
        if i != 0:
            for k in range(0,HiddenLayerNeuron[i-1]+1):
                data[f"Layer_{i}"][f"Neuron{j}"].append(random.random())

MyData.data = data
MyData.WriteNeuronData()