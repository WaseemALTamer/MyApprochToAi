import Evolver
import instatingNeuronsBW
import numpy as np
import ProcessStats
import random
import MyData




def instating_Gen_0():
    ApexMutation = []
    GenerationOutput = []

    for i in range(0,100):
        Evolver.data = instatingNeuronsBW.GenerateBaisWeight()
        RawData = Evolver.TestEvolution(random.randint(0,69999))
        output = [ProcessStats.LargestNum(RawData[0]),RawData[1]]

        if output[0][1] == output[1]:
            if ApexMutation != []:
                if ApexMutation[0][0] < output[0][0]:
                    ApexMutation = output
                    GenerationOutput = Evolver.data
            else:
                ApexMutation = output
                GenerationOutput = Evolver.data
    return GenerationOutput


NextGenData = MyData.GrapNeuronData()
try:
    with open('ApexMutationResults.txt', 'r') as file:
        lines = file.readlines()
        ApexMutation = [(float(lines[0]),int(lines[1])),int(lines[2])]
    
except:
    ApexMutation = [(0,1),0]


def instating_Gen_Next():
    global NextGenData, ApexMutation
    Evolver.data = NextGenData

    
    GenerationOutput = Evolver.data

    for i in range(0,100):
        RawData = Evolver.TestEvolution(random.randint(0,69999))
        output = [ProcessStats.LargestNum(RawData[0]),RawData[1]]

        if output[0][1] == output[1]:
            if ApexMutation[0][0] <= output[0][0]:
                ApexMutation = output
                GenerationOutput = Evolver.data

        Evolver.data = instatingNeuronsBW.MutateBaisWeight(50,Evolver.data)

    return [GenerationOutput,ApexMutation]


for i in range(0,10):
    output = instating_Gen_Next()
    print(f"Gen{i} ==> {output[1]}")
    NextGenData = output[0]



with open('ApexMutationResults.txt', 'w') as file:
    file.write(f"{ApexMutation[0][0]}\n")
    file.write(f"{ApexMutation[0][1]}\n")
    file.write(f"{ApexMutation[1]}\n")

MyData.data = output[0]
MyData.WriteNeuronData()