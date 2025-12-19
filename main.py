import os
import requests
import pandas as pd
from datetime import datetime

# Get API Key from GitHub Secrets
API_KEY = os.getenv("TANKER_API_KEY")
url = f"https://creativecommons.tankerkoenig.de/json/list.php?lat=52.521&lng=13.438&rad=5&sort=dist&type=all&apikey={API_KEY}"

response = requests.get(url).json()

if response["ok"]:
    df = pd.DataFrame(response["stations"])
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save/Append to CSV
    file_exists = os.path.isfile("fuel_history.csv")
    df.to_csv("fuel_history.csv", mode='a', index=False, header=not file_exists)
    print("Prices updated successfully.")
