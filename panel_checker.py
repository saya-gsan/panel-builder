#Step 1: Read the panel CSV, collect all the fluorochromes into one list. 
import csv # Import the csv module to read CSV files
import argparse # Import the argparse module to handle command-line arguments
def load_panel(filename): # Define a function called load_panel that opens a CSV file and reads its contents
    panel_fluorochromes = [] # Create an empty list called panel_fluorochromes to store the fluorochromes from the CSV file
    filename = "my_panel.csv" # Define the filename of the CSV file to read
    with open(filename) as f:# Open the CSV file called "my_panel.csv for reading as variable f
        reader = csv.DictReader(f) # Read the CSV file as a dictionary using the DictReader function from the csv module, and store it in the variable reader # Looks at the first row of the CSV file to determine the field names (keys) for the dictionary
        for row in reader: # Goes through each row in the reader (which is a dictionary for each row of the CSV file)
            #print(f"{row['Fluorochrome']} -> {row['Channel']}") # For each row, it prints the value for the "Fluorochrome" key follwed by n arrow and the value for the "Channel" key. This will output the fluorochrome and its corresponding channel for each of the rows in the CSV file.
            panel_fluorochromes.append(row["Channel"])
            #print(panel_fluorochromes)
    return panel_fluorochromes

def check_conflicts(panel_fluorochromes): # Define a function called check_conflicts that takes a list of panel_fluorochromes as an argument
    panel_fluorochromes = set(panel_fluorochromes) # Convert the list of panel_fluorochromes to a set to remove duplicates and allow for faster lookups
    conflict_pairs = [["PE", "PE-CF594"],["PerCP", "PerCP-Cy5.5"],["PE-Cy5", "PE-Cy5.5"],["FITC", "PE"]]
    conflict_found = False
    for pair in conflict_pairs:
        if pair[0] in panel_fluorochromes and pair[1] in panel_fluorochromes:
            print(f"Warning: {pair[0]} and {pair[1]} are known to have spectral overlap and may cause issues in your panel design.")
            conflict_found = True
    if not conflict_found:
        print("No conflicts detected based on the current panel design.")

def main():
    parser = argparse.ArgumentParser(description="Check for conflicts in a flow cytometry panel.")
    parser.add_argument("-p", "--panel", help="Path to the CSV panel file.")
    args = parser.parse_args()

    filename = args.panel # Define the filename of the CSV file to read
    panel_fluorochromes = load_panel(filename) # Call the load_panel function with the filename and store the result in panel_fluorochromes
    check_conflicts(panel_fluorochromes) # Call the check_conflicts function with the list of panel_fluorochromes to check for any conflicts

main() # Call the main function to execute the program


#TODO: replace the conflict_pairs list with a database of known fluorochrome-channel conflicts, and implement a function to check for conflicts based on the data read from the CSV file. 
