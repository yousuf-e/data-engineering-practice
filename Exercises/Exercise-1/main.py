from sys import path
import requests
import os
from zipfile import ZipFile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # your code here
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
    

    for url in download_uris:
        zip_file_name = url.split('.com/')[1]
        file_path = f"./downloads/{zip_file_name}"

        try:
            r = requests.get(url=url)
            r.raise_for_status()
        except requests.exceptions.RequestException as e: 
            print(f"{e}")
        
        if r and r.ok:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'wb') as file:
                file.write(r.content)

            with ZipFile(file_path, 'r') as zip:
                zip.extractall('./downloads')

        else:
            print('zip file download not successful')



if __name__ == "__main__":
    main()``
