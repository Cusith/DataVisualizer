import tkinter as tk
import matplotlib.pyplot as plt


def visualize_data(x_labels, data_values):
    # Create a bar chart using Matplotlib
    colors = ['red', 'green', 'blue']  # Custom colors for bars
    bars = plt.bar(x_labels, data_values, color=colors)

    # Add data labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

    # Customize the chart
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Data Visualization')
    plt.xticks(rotation=45)  # Rotate x-axis labels

    # Add a legend
    plt.legend(bars, x_labels)

    # Display the chart
    plt.show()


def on_submit():
    # Retrieve input values from the entry widgets
    categories = entry_categories.get()
    values = entry_values.get()

    # Convert input values to lists
    categories = categories.split(',')
    values = list(map(int, values.split(',')))

    # Call the visualize_data function with the provided input
    visualize_data(categories, values)


# Create the GUI window
window = tk.Tk()
window.title("Data Visualization")
window.geometry("400x200")

# Create labels and entry widgets for input
label_categories = tk.Label(window, text="Categories:")
label_categories.pack()
entry_categories = tk.Entry(window)
entry_categories.pack()

label_values = tk.Label(window, text="Values:")
label_values.pack()
entry_values = tk.Entry(window)
entry_values.pack()

# Create a submit button
submit_button = tk.Button(window, text="Visualize", command=on_submit)
submit_button.pack()

# Start the GUI event loop
window.mainloop()
