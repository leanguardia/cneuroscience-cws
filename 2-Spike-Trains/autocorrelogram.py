#!/usr/bin/env python
# coding: utf-8

# ### Q3 - Correlogram

# In[77]:


import os
import numpy as np
from poisson import coefficient_of_variation
from load import load_data, generate_spiking_times
import matplotlib.pyplot as plt


# In[120]:


file_path = os.getenv('ABS_PATH') + "/rho.dat"
spikes = load_data(file_path, int)

print("Lenght of data:",len(spikes))
print("Firing Events:", np.sum(spikes))
print(spikes[0:18])


# In[121]:


spike_train = generate_spiking_times(spikes)
spike_train[0:5]


# In[125]:


raw_correlations = np.zeros(50)
train_length = len(spike_train)

for i, spike_time in enumerate(spike_train[:100]):
#     print("Spike", i, spike_time)
    j = i + 1

    while j < train_length:
        next_spike = spike_train[j]
        time_diff_ms = next_spike - spike_time
        
        if time_diff_ms <= 0.100:
            adj_bin = int(time_diff_ms * 1000)
            adj_bin = int(adj_bin/2)
            raw_correlations[adj_bin] += 1
#             print(j, time_diff_ms, adj_bin)
        else:
            break
            
        j += 1

positive_correlations = np.array(raw_correlations)
print(len(positive_correlations))
positive_correlations


# In[126]:


negative_correlations = np.flip(positive_correlations)[:-1]
# print(len(negative_correlations))
# negative_correlations
correlations = np.append(negative_correlations, positive_correlations)
print(len(correlations))
correlations


# In[127]:


x = np.arange(-99,99,2)
print(x.shape)
x


# In[162]:



fig = plt.figure(figsize=(12,5))
ax = fig.add_axes([0.1,0.1,0.85,0.85])

ax.bar(x, correlations, align='edge', width=1.7)
plt.ylabel("Number of correlations")
plt.xlabel("Time Interval (ms)")
plt.title("Q3 - Autocorrelogram")
plt.show()
fig.savefig('autocorrelations.png', dpi=fig.dpi)


# In[ ]:





# In[ ]:




