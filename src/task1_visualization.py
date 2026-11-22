import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    
    counts = collections.Counter(data)
    categories = list(counts.keys())
    frequencies = list(counts.values())
    
    fig, ax = plt.subplots()
    colors = plt.cm.tab10(np.linspace(0, 1, max(len(categories), 1)))
    
    ax.bar(categories, frequencies, color=colors[:len(categories)])
    ax.set_xlabel("Category")
    ax.set_ylabel("Frequency")
    ax.set_title("Category Distribution")

    return fig

if __name__ == '__main__':
    # Example data
    data = np.random.choice(['A', 'B', 'C'], size=100)
    plot_distribution(data)
