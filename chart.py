import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_combined_graph(csv_files, labels):
    # Initialize an empty DataFrame
    all_data = pd.DataFrame()

    # Iterate over the provided CSV files and labels
    for csv_file, label in zip(csv_files, labels):
        # Load the data
        data = pd.read_csv(csv_file, header=None)
        data.columns = ['Time in Use, [days]', 'Costs, [PLN]']  # Set column names
        data['Policy'] = label  # Add a column for the policy label
        data.sort_values(by='Time in Use, [days]', inplace=True)  # Sort data to make line plots work correctly

        # Append to the full dataset
        all_data = pd.concat([all_data, data], ignore_index=True)

    # Create a figure for plotting
    plt.figure(figsize=(12, 8))

    # Plot lines
    sns.lineplot(data=all_data, x='Time in Use, [days]', y='Costs, [PLN]', hue='Policy', style='Policy',
                 linewidth=2, alpha=0.7)

    # Adding title and labels
    plt.title('Comparison of Costs vs. Time in Use Across Maintenance Policies')
    plt.xlabel('Time in Use, [days]')
    plt.ylabel('Costs, [$]')
    plt.grid(True)

    # Enhance legend
    plt.legend(title='Policy', title_fontsize='13', fontsize='11')

    # Display the plot
    plt.show()

# List of CSV files and their corresponding labels
csv_files = ['policy1_results.csv', 'policy2_results.csv', 'policy3_results.csv']
labels = ['Maintenance Policy 1', 'Maintenance Policy 2', 'Maintenance Policy 3']

# Call the function to create the plot
create_combined_graph(csv_files, labels)
