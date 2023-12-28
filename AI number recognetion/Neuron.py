import math


def NeuronCal(inputs, NeuronData):
    final_ans = 0
    for i in range (0,len(inputs)):
        final_ans += inputs[i]*NeuronData[i+1]
    final_ans = final_ans + NeuronData[0]
    return final_ans