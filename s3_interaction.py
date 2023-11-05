import boto3
import pandas as pd

#Creating a client to interact with aws' s3

s3_client = boto3.client('s3')

#downloading files from s3

s3_client.download_file('datalake-nicholasdasilvaloureiro','data/data_gas.csv','data_gas_dwn.csv')

df = pd.read_csv("data_gas_dwn.csv")

# making sure everything is correct
print(df)

#uploading the file on s3
s3_client.upload_file('data_gas_dwn.csv','datalake-nicholasdasilvaloureiro','data/data_gas_up.csv')
