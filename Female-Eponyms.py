import pandas as pd
import matplotlib.pyplot as plt

# Data File Preparation
raw_data = pd.read_csv('WomenPlantGenera_v1-3.csv')

# Selecting relevant columns
selected_data = raw_data[['genus-name', 'genus-wfo-status', 'family-name-wfo', 'eponymy-name', 'eponymy-yob', 'eponymy-yod', 'eponymy-occupation', 'eponymy-is-real', 'eponymy-country']]

# Get user input
plant_name = input('Please enter the plant name you want to check: ')

# Filter entries based on user input
connected_entries = selected_data[selected_data['genus-name']==plant_name]

# Function to display plant information
def plant_information(plant_name):
    if connected_entries.empty:
        print(f'The plant name "{plant_name}" does not exist in the selected data.')
    else:
        print(exist_information(plant_name))
       
# Function to return detailed information about the plant
def exist_information(plant_name):
    return f'The plant name "{plant_name}" exists in the selected data. It has {len(connected_entries)} result(s):\n{combined_eponomy_information()}{combined_exist_informations()}'

# Function to return combined eponomy information
def combined_eponomy_information():
    if (len(connected_entries) == 1) or (connected_entries['genus-name'].nunique()==1 and connected_entries['eponymy-yob'].nunique()==1):
        return eponomy_information()
    else:
        return f'The different plants come from different women with the same name. To the first woman in the list, the following information is aviable: {eponomy_information()}' #### Mögliche Erweiterung: tatsächlich einzeln nennen ###

# Function to return one eponomy information
def eponomy_information():
    return f'The flowers namesake is {connected_entries["eponymy-name"].iloc[0]}. She {reality_information()}'
    
# Function to return further information depending on whether namesake was a real person or not
def reality_information():
    if connected_entries['eponymy-is-real'].iloc[0]:
        return f'was a {connected_entries["eponymy-occupation"].iloc[0]} and lived from {connected_entries["eponymy-yob"].iloc[0]} to {connected_entries["eponymy-yod"].iloc[0]} in {connected_entries["eponymy-country"].iloc[0]}. \n'
    else:
        return f'is a {connected_entries["eponymy-occupation"].iloc[0]}. \n'

# Function to return combined information for each entry
def combined_exist_informations():
    individual_rows = []
    for i, (index, row) in enumerate(connected_entries.iterrows(), start = 1):
        row_info = indiv_exist_information(row, i)
        individual_rows.append(row_info)
    return '\n'.join(individual_rows)

# Function to return information for each entry
def indiv_exist_information(row_data, number):
    return f'Entry number {number} belongs to the wfo-family of the {row_data["family-name-wfo"]}. Its wfo-Status is: {row_data["genus-wfo-status"]}'

# Function to plot visualization
def plot_visualization():
    if connected_entries['eponymy-is-real'].iloc[0]:
        target_country = connected_entries['eponymy-country'].iloc[0]
        plot_country_visualization(target_country)
    else:
        target_occupation = connected_entries['eponymy-occupation'].iloc[0]
        plot_category_visualization(target_occupation)

# Function to plot country visualization
def plot_country_visualization(target_country):
    target_count = (selected_data['eponymy-country'] == target_country).sum()
    other_countries_count = (selected_data['eponymy-country'] != target_country).sum()

    visualization_data = pd.DataFrame({'Country': [target_country, 'Other Countries'], 'Count': [target_count, other_countries_count]})
    plot_pie_chart(visualization_data, 'Country', 'Plants Named After Real People - Country Visualization')

# Function to plot category visualization
def plot_category_visualization(target_occupation):
    target_count = (selected_data['eponymy-occupation'] == target_occupation).sum()
    other_occupations_counts = selected_data['eponymy-occupation'].value_counts()

    visualization_data = pd.DataFrame({'Occupation': [target_occupation, 'Other Occupations'], 'Count': [target_count, other_occupations_counts.sum()]})
    plot_pie_chart(visualization_data, 'Occupation', 'Plants Named After Mythical/Fictional Characters - Category Visualization', ylabel='Number of Plants')
    
# Function to plot a pie chart
def plot_pie_chart(data, label_col, title, ylabel=''):
    data.plot(kind='pie', y='Count', labels=data[label_col], autopct='%1.1f%%', colors=['skyblue', 'lightcoral'], startangle=90)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()

# Display plant information
result = plant_information(plant_name)

# Plot visualization if there are connected entries
if not connected_entries.empty:
    plot_visualization()