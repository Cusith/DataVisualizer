import matplotlib.pyplot as plt

def visualize_data(x_labels, data_values, plot_style='bar'):
    # Adjust the figure size
    plt.figure(figsize=(8, 6))

    if plot_style == 'bar':
        # Create a bar chart using Matplotlib
        colors = ['red', 'green', 'blue']  # Custom colors for bars
        bars = plt.bar(x_labels, data_values, color=colors)
        
        # Add data labels
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

    elif plot_style == 'line':
        # Create a line plot
        plt.plot(x_labels, data_values, marker='o')

    elif plot_style == 'scatter':
        # Create a scatter plot
        plt.scatter(x_labels, data_values, marker='o')

    elif plot_style == 'stacked':
        # Create a stacked bar chart
        plt.bar(x_labels, data_values[0], label='Dataset 1')
        plt.bar(x_labels, data_values[1], label='Dataset 2', bottom=data_values[0])
        plt.bar(x_labels, data_values[2], label='Dataset 3', bottom=[sum(data_values[:i]) for i in range(2)])

        # Add data labels
        for i, val in enumerate(data_values):
            for j, sub_val in enumerate(val):
                plt.text(j, sum(data_values[k][:j+1] for k in range(i)), str(sub_val), ha='center', va='bottom')

    # Customize the chart
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Data Visualization')
    plt.xticks(rotation=45)  # Rotate x-axis labels

    # Add a legend
    plt.legend()

    # Save the chart as an image file
    plt.savefig('chart.png')

    # Display the chart
    plt.show()

# Example usage
categories = ['Category A', 'Category B', 'Category C']
values = [[10, 15, 5], [5, 10, 15], [15, 5, 10]]

visualize_data(categories, values, plot_style='bar')
visualize_data(categories, values, plot_style='line')
visualize_data(categories, values, plot_style='scatter')
visualize_data(categories, values, plot_style='stacked')
