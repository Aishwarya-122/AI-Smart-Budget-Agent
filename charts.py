import matplotlib.pyplot as plt

def plot_category(summary):
    if summary.empty:
        return None  # prevent crash

    summary.plot(kind='bar')
    plt.title("Category-wise Spending")
    plt.ylabel("Amount")
    return plt