import requests
from dotenv import load_dotenv
import os

load_dotenv()
header = {
    "project": "KHU_PROMPTHON_018", 
    "apiKey": "프로젝트의 API KEY" 
   }


URL = "https//"+os.getenv("URL")
response = requests.post(URL, headers=header, json=body)

body = {
     "hash": "2cc6f00d01058516d8d0ac3b062a2547679aaef311d22b82400aa82f8ef4be47", 
    "params": {"task":""} 
   }