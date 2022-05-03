import os
import pandas as pd

# Create empty list to store data for Pandas DataFrame
data = []

# Use os.listdir to iterate through the folder names and file names
for folder in sorted(os.listdir('C:\QL Clustering\MortgageCoupons')):
    for file in sorted(os.listdir('C:\QL Clustering\MortgageCoupons/' + folder)):
    # Use .endswith to filter only ".pdf" and ".tiff" file extension names
        if file.endswith((".pdf", ".tiff")):
            data.append((folder, file))

# Create DataFrame using the folder names and file names
df = pd.DataFrame(data, columns=['Folder', 'File'])

# Write to CSV from DataFrame
df.to_csv('filenames.csv', index = False)
