import random as rnd
import numpy as np

# the function returns a spike trains for the interval [0, big_t]
# with overall firing rate and refractory period tau_ref.
def get_spike_train(rate, big_t, tau_ref):
    if 1 <= rate * tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []

    # The rate the Poisson process must have to give the correct overall
    # firing rate given the refractory period.
    exp_rate = rate / (1 - tau_ref * rate)
    spike_train = []

    t = rnd.expovariate(exp_rate)
    while t < big_t:
        spike_train.append(t)
        t += tau_ref + rnd.expovariate(exp_rate)

    return spike_train

def spike_counts(spike_train, big_t, interval_window):
    total_bins = int(big_t / interval_window)
    spike_counts = np.zeros(total_bins)
    bin = 1
    for spike_time in spike_train:
        if spike_time >= (bin * interval_window): bin += 1
        spike_counts[bin - 1] += 1
    return spike_counts

def fano_factor(spike_train, big_t, interval_window):
    counts = spike_counts (spike_train, big_t, interval_window)
    variance = np.var(counts)
    mean  = np.mean(counts)
    return variance / mean

def time_intervals(spike_train):
    intervals = []
    for i in range(1,len(spike_train)):
        intervals.append(spike_train[i] - spike_train[i - 1])
    return intervals

def coefficient_of_variation(spike_train):
    intervals = time_intervals(spike_train)
    standard_dev = np.std(intervals)
    mean = np.mean(intervals)
    return standard_dev / mean


######### MAIN #########

Hz = 1.0
ms = 0.001
sec = 1.0

rate = 15.0 * Hz
tau_ref = 5 * ms
big_t = 5 * sec

print("Input params")
print("Firing Rate:", rate, "Hz")
print("Refractory Period:", tau_ref, "ms")
print("Big T:", big_t, "sec")

spike_train = get_spike_train(rate, big_t, tau_ref)
spikes_count = len(spike_train)

print("Spikes", spikes_count)
print("-->", spikes_count / big_t, "spikes/sec")
print(spike_train)

# Q1
# Fano Factor
interval_window = 100 * ms
fano = fano_factor(spike_train, big_t, interval_window)
print(fano)

# time_intervals = time_intervals(spike_train)
# print(len(time_intervals))
# print(time_intervals)

coeff_of_var = coefficient_of_variation(spike_train)
print(coeff_of_var)