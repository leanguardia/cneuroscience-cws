import random as rnd

def get_spike_train(rate, big_t, tau_ref):

    if 1 <= rate * tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []

    exp_rate = rate / (1 - tau_ref * rate)
    spike_train = []

    t = rnd.expovariate(exp_rate)
    while t < big_t:
        spike_train.append(t)
        t += tau_ref + rnd.expovariate(exp_rate)

    return spike_train

######### MAIN #########

Hz = 1.0
sec = 1.0
ms = 0.001

rate = 15.0 * Hz
tau_ref = 5 * ms

big_t = 5 * sec

print("Input params")
print("Hz:", Hz)
print("sec:", sec)
print("ms:", ms)
print("rate:", rate)
print("tau_ref:", tau_ref)
print("big_t:", big_t)

spike_train = get_spike_train(rate, big_t, tau_ref)

length = len(spike_train)
print("Length", length)

print("XYZ", length / big_t)

# print(spike_train)
