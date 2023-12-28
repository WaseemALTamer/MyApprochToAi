import Evolver
import random
import instatingNeuronsBW
import ProcessStats
import MyData

def instating_test():
    ApexMutation = []
    GenerationOutput = []
    Evolver.data = instatingNeuronsBW.GenerateBaisWeight()

    for i in range(0,100):
        
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
    print(ApexMutation)
    return GenerationOutput


MyData.data = instating_test()
MyData.WriteNeuronData()