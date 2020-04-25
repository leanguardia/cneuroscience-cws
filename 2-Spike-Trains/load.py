import os
import numpy as np

def load_data(filename, Type):
    data_array = [Type(line.strip()) for line in open(filename, 'r')]
    return data_array

file_path = os.getenv('ABS_PATH') + "/rho.dat"
spikes = load_data(file_path, int)

print(len(spikes))
print(spikes[0:18])

spikes_mean = np.mean(spikes)
spikes_var = np.var(spikes)

fano_factor = spikes_var / spikes_mean

print("Fano Factor", fano_factor)

#stimulus=[float(x) for x in load_data("stim.dat")]
# stimulus = load_data("stim.dat",float)

# print(len(stimulus))
# print(stimulus[0:5])
