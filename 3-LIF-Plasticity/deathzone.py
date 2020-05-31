def plot_q2_synapse(title, filename, time_range, collection):
    fig = plt.figure(figsize=(14,4))
    ax = fig.add_subplot()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title(title)
    ax.set_xlabel("Synapse Number")
    ax.set_ylabel("Synapse Strength (nS)")
    
    x = range(1,41)
    for conductances in collection:
        y = conductances * 1000
        ax.fill_between(x, y, color='dodgerblue', alpha=0.1)
    ax.set_xticks(x)
#     fig.savefig(f"plots/{filename}-{int(ti.time())}.png", dpi=100,
#                 bbox_inches='tight', pad_inches=0.2
#                )
title = "Synaptic Strengths after 300 seconds of simulation"
plot_q2_synapse(title, "b_q2_strenghts", time_range, conductances_collection)