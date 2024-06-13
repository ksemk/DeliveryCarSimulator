import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  # For numerical operations


def read_and_plot(csv_files, labels):
    plt.figure(figsize=(12, 8))

    for csv_file, label in zip(csv_files, labels):
        # Load the data
        data = pd.read_csv(csv_file, header=None)
        data.columns = ['Time in Use, [days]', 'Total Costs, [PLN]', 'Failure Costs, [PLN]', 'Maintenance Costs, [PLN]']

        if data['Maintenance Costs, [PLN]'].nunique() == 1:  # Check if all x-values are the same
            # Draw a vertical line if all maintenance costs are the same
            unique_value = data['Maintenance Costs, [PLN]'].iloc[0]
            plt.axvline(x=unique_value, label=f'{label} (all maintenance costs are {unique_value})', linestyle='--')
        else:
            # Plot line normally
            sns.lineplot(data=data, x='Maintenance Costs, [PLN]', y='Failure Costs, [PLN]', label=label)

    # Adding title and labels
    plt.title('Failure Costs vs. Maintenance Costs Across Maintenance Policies')
    plt.xlabel('Maintenance Costs, [PLN]')
    plt.ylabel('Failure Costs, [PLN]')
    plt.grid(True)
    plt.legend(title='Policy', title_fontsize='13', fontsize='11')
    plt.show()


# List of CSV files and their corresponding labels
csv_files = ['policy1_results.csv', 'policy2_results.csv', 'policy3_results.csv']
labels = ['Maintenance Policy 1', 'Maintenance Policy 2', 'Maintenance Policy 3']

# Call the function to create the plot
read_and_plot(csv_files, labels)
