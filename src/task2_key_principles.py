import matplotlib
matplotlib.use("Agg")

import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    
    sns.set_theme(style="whitegrid")
    
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x="x", y="y", ax=ax)
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Relationship between x and y")
    ax.grid(True)
    
    return fig


if __name__ == '__main__':
    # Example data
    data = pd.DataFrame({
        'x': np.random.rand(50),
        'y': np.random.rand(50)
    })
    create_scatter_plot(data)