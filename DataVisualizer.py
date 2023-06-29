import matplotlib.pyplot as plt

def visualize_data(x_labels, data_values):
    # Adjust the figure size
    plt.figure(figsize=(8, 6))

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

    # Save the chart as an image file
    plt.savefig('bar_chart.png')

    # Display the chart
    plt.show()

# Example usage
categories = ['Category A', 'Category B', 'Category C']
values = [10, 15, 5]

visualize_data(categories, values)
