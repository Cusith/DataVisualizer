import matplotlib.pyplot as plt

def visualize_data(x_labels, data_values):
    # Create a bar chart using Matplotlib
    plt.bar(x_labels, data_values)
    
    # Customize the chart
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Data Visualization')
    
    # Display the chart
    plt.show()

# Example usage
categories = ['Category A', 'Category B', 'Category C']
values = [10, 15, 5]

visualize_data(categories, values)
