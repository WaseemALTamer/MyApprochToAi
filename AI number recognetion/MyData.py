import json


data = {}


def WriteNeuronData():
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)


def GrapNeuronData():
    global data
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    return data


