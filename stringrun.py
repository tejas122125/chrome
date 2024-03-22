# code  = """import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('Player.csv')

# batting_hand_counts = df['Batting_Hand'].value_counts()
# batting_hand_counts.plot(kind='bar')
# plt.title('Batting Hand Distribution')
# plt.xlabel('Batting Hand')
# plt.ylabel('Count')
# plt.savefig('chart.png')"""
# exec(code)

import requests

def download_csv(url, save_path):
    # Send a GET request to the URL to download the file
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the local file in binary write mode and write the content of the response
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"CSV file downloaded successfully and saved as {save_path}")
    else:
        print(f"Failed to download CSV file. Status code: {response.status_code}")

# Example usage:
url = 'https://cloud.appwrite.io/v1/storage/buckets/658da6ec42519f39311a/files/65fdc0a5cd567a08f5ce/view?project=658c3e666ed66b56edb7&mode=admin'  # Replace with the URL of the CSV file
save_path = 'data.csv'   # Replace with the path where you want to save the file

download_csv(url, save_path)
