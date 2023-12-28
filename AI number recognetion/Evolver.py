import ImageToData
import Neuron
import instatingNeuronsBW




data = {}




def GrapImage(imageNum):
    global data
    image = ImageToData.image(imageNum)
    for i in range(0,len(data["Layer_0"])):
        data["Layer_0"][f"Neuron{i}"] = image[0][i]
    return image




def TestEvolution(imageNum):
    global TempNoutput, data, Noutput

    Noutput = []
    TempNoutput = []
    
    ImageToData = GrapImage(imageNum)
    Noutput = ImageToData[0]

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

    array = TempNoutput
    Added = 0

    for i in range (0,len(array)):
        Added += array[i]

    for i in range (0,len(array)):
        array[i] /= Added

    return array, int(ImageToData[1])