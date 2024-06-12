import pandas as pd
import matplotlib.pyplot as plt


def create_graph_from_csv(csv_filename):
    # Load the data
    data = pd.read_csv(csv_filename)

    # Ensure the data columns are named correctly
    data.columns = ['Time in Use, [months]', 'Costs, [$]']

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Time in Use, [months]'], data['Costs, [$]'], color='blue', alpha=0.5)

    # Adding title and labels
    plt.title('Costs vs. Time in Use')
    plt.xlabel('Time in Use, [months]')
    plt.ylabel('Costs, [$]')

    # Display the plot
    plt.grid(True)
    plt.show()


# Example of how to call the function
csv_filename = 'policy1_results.csv'
create_graph_from_csv(csv_filename)
