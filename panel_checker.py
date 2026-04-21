import csv
with open('my_panel.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Fluorochrome']} -> {row['Channel']}")