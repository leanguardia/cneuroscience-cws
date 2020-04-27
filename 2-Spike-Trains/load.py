import os
import numpy as np
from poisson import fano_factor, coefficient_of_variation

def load_data(filename, Type):
    data_array = [Type(line.strip()) for line in open(filename, 'r')]
    return data_array

def generate_spiking_times(event_sequence, sample_time = 0.002):
  elapsed_time = 0
  spike_train = []
  for event in event_sequence:
    if event: spike_train.append(elapsed_time)
    elapsed_time += sample_time
  return spike_train


##### Q2 #####
if __name__ == "__main__":
  
  file_path = os.getenv('ABS_PATH') + "/rho.dat"
  spikes = load_data(file_path, int)

  print("Lenght of data:",len(spikes))
  print("Firing Events:", np.sum(spikes))
  # print(spikes[0:18])

  # Generate Spike Train
  spike_train = generate_spiking_times(spikes)
  print("Activations detected:", len(spike_train))
  # print(spike_train[0:10])
  # print(spike_train[-10:])
  # print(spike_train[:-10])

  # Fano Factor
  big_t = 1200 # seconds  
  interval_window = 10
  fano_factor = fano_factor(spike_train, big_t, interval_window)
  print("Fano Factor:", fano_factor)

  # Coeff of Variance
  coeff_of_var = coefficient_of_variation(spike_train)
  print("Coeff of Var:", coeff_of_var)

  #stimulus=[float(x) for x in load_data("stim.dat")]
  # stimulus = load_data("stim.dat",float)

  # print(len(stimulus))
  # print(stimulus[0:5])
