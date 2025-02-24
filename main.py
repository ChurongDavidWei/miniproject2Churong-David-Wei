'''
INF601 - Programming in Python
Assignment # mini project 2
I,     Churong'David'Wei    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

# Import all needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import requests
import os

# Collect data form FCC API
url = "https://opendata.fcc.gov/resource/hicn-aujz.json"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve data")
    data = []

# Store data in panda dataframe
df = pd.DataFrame(data)

# Step 3: Extract Relevant Column
df = df[['maxaddown']].dropna()  # Select only download speed column
df['maxaddown'] = pd.to_numeric(df['maxaddown'])  # Convert to numeric

# Generate graphs using matplotlib
plt.figure(figsize=(10, 5))
plt.hist(df['maxaddown'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Advertised Download Speeds')
plt.xlabel('Download Speed (Mbps)')
plt.ylabel('Frequency')

# Create path and save graphs as png file
os.makedirs("charts", exist_ok=True)

plt.savefig('charts/broadband_speed_distribution.png')
print("Graphs saved in 'charts/' directory.")
plt.close()








