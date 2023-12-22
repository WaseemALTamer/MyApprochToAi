import ImageToData
import MyData
import Neuron
import time


MyData.GrapNeuronData()
data = MyData.data

Noutput = []
TempNoutput = []


timer = time.time() + 1
times = 0

def GrapImage(imageNum):
    global data
    image = ImageToData.image(imageNum)
    for i in range(0,len(data["Layer_0"])):
        data["Layer_0"][f"Neuron{i}"].append(image[0][i])
    return image[0]

Noutput = GrapImage(1)



def function():
    global timer, TempNoutput, data, Noutput, times
    while True:
        for i in range (0,len(data["Layer_1"])):
            x = Neuron.NeuronCal(Noutput,data["Layer_1"][f"Neuron{i}"])
            TempNoutput.append(x)
        
        Noutput = TempNoutput
        TempNoutput = []

        for i in range (0,len(data["Layer_2"])):
            x = Neuron.NeuronCal(Noutput,data["Layer_2"][f"Neuron{i}"])
            TempNoutput.append(x)

        Noutput = TempNoutput
        TempNoutput = []

        for i in range (0,len(data["Layer_3"])):
            x = Neuron.NeuronCal(Noutput,data["Layer_3"][f"Neuron{i}"])
            TempNoutput.append(x)
        Noutput = GrapImage(0)
        print(TempNoutput)

        TempNoutput = []

        times += 1

        if timer < time.time():
            print(times,)
            times = 0 
            timer = time.time() + 1


            
function()