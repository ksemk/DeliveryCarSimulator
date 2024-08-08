import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = 'DeliveryCarSimulator\simulation_results'
def read_and_plot(csv_files, labels):
    # Validate inputs
    if not csv_files or not labels:
        raise ValueError("The csv_files and labels lists cannot be empty.")
    
    if len(csv_files) != len(labels):
        raise ValueError("The csv_files and labels lists must have the same length.")
    
    for csv_file in csv_files:
        if not os.path.isfile(csv_file):
            raise FileNotFoundError(f"The file {csv_file} does not exist or is not readable.")
    
    plt.figure(figsize=(12, 8))

    for csv_file, label in zip(csv_files, labels):
        # Load the data
        try:
            data = pd.read_csv(csv_file, header=None, usecols=[2, 3])
        except pd.errors.EmptyDataError:
            raise ValueError(f"The file {csv_file} is empty.")
        except pd.errors.ParserError:
            raise ValueError(f"The file {csv_file} could not be parsed.")
        
        data.columns = ['Failure Costs, [PLN]', 'Maintenance Costs, [PLN]']

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

# Save the plot
    output_file = os.path.join(output_dir, 'failure_vs_maintenance_costs_plot.png')
    plt.savefig(output_file)
    plt.close()


# List of CSV files and their corresponding labels
csv_files = ['DeliveryCarSimulator\simulation_results\policy1_results.csv', 'DeliveryCarSimulator\simulation_results\policy2_results.csv', 'DeliveryCarSimulator\simulation_results\policy3_results.csv']
labels = ['Maintenance Policy 1', 'Maintenance Policy 2', 'Maintenance Policy 3']

# Call the function to create the plot
read_and_plot(csv_files, labels)
