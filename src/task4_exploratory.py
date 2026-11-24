import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    numeric_df = df.select_dtypes(include=[np.number])
    
    desc_table = numeric_df.describe().T
    desc_table["median"] = numeric_df.median()
    desc_table["variance"] = numeric_df.var()
    modes = numeric_df.mode()
    desc_table["mode"] = modes.iloc[0] if not modes.empty else np.nan
    
    print("=== Descriptive Statistics ===")
    print(desc_table.to_string())
    print(
        "\nDescriptive stats summary: Compare mean vs. median to spot skewness, "
        "variance/std to gauge spread, and mode for most frequent values.\n"
    )
    
    fig_box, ax_box = plt.subplots(figsize=(8,5))
    sns.boxplot(data=numeric_df, ax=ax_box)
    ax_box.set_title("Box Plot for Outlier Detection")
    ax_box.set_xlabel("Features")
    ax_box.set_ylabel("Values")
    print(
        "Outlier summary: Points outside the whiskers (beyond 1.5 * IQR) "
        "from Q1/Q3) indicate potential outliers and distribution skew.\n"
    )
    
    corr_matrix = numeric_df.corr()
    fig_corr, ax_cor = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax_cor)
    ax_cor.set_title("Correlation Matrix Heatmap")
    print(
        "Correlation summary: Values near +1 or -1 indicate strong positive "
        "or negative linear relationships; values near 0 indicate weak linear correlation.\n"
    )
    
    return fig_box, fig_corr, desc_table
    

if __name__ == '__main__':
    # Example data
    df = pd.DataFrame({
        'A': np.random.rand(50),
        'B': np.random.rand(50) * 10,
        'C': np.random.rand(50) * 100
    })
    perform_eda(df)
