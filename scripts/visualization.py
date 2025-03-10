import matplotlib.pyplot as plt
import numpy as np

def plot_rose_chart(data):
    pivot_data = data.pivot(index='month', columns='location', values='death_rate').fillna(0)

    # Set angles and labels
    months = pivot_data.index
    num_months = len(months)
    angles = np.linspace(0, 2 * np.pi, num_months, endpoint=False).tolist()

    # Plot setup
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Plot data for each continent
    continents = pivot_data.columns
    width = 2 * np.pi / num_months

    for continent in continents:
        values = pivot_data[continent].values
        ax.bar(angles, values, width=width, label=continent, alpha=0.7)

    # Add labels and legend
    ax.set_xticks(angles)
    ax.set_xticklabels(months.strftime('%b %Y'), fontsize=10)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.title('Monthly COVID-19 Death Rates by Continent', size=15)
    plt.show()
