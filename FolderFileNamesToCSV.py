import os
import pandas as pd

path = 'your_own/filepath/'

# Create empty list to store data for Pandas DataFrame
data = []

# Use os.listdir to iterate through the folder names and file names in file path
for folder in sorted(os.listdir(path)):
    for file in sorted(os.listdir(path + folder)):
    # Use .endswith to filter only ".pdf" and ".tiff" file extension names
        if file.endswith((".pdf", ".tiff")):
            data.append((folder, file))

# Create DataFrame using the folder names and file names
df = pd.DataFrame(data, columns=['Folder', 'File'])

# Write to CSV from DataFrame
df.to_csv('filenames.csv', index = False)
