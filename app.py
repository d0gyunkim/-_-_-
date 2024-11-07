import requests
from dotenv import load_dotenv
import os

load_dotenv()
header = {
    "project": os.getenv("KHU_PROMPTHON_018"), 
    "apiKey": os.getenv("WANTED_API_KEY")
   }
body = {
     "hash": "2cc6f00d01058516d8d0ac3b062a2547679aaef311d22b82400aa82f8ef4be47", 
    "params": {"현재 회사":"경희대","직무":"학생","경력기간":"2년","주요업무":"공부","소속":"빅응","작성언어":"한글"} 
   }

URL = os.getenv("WANTED_API_URL")
response = requests.post(URL, headers=header, json=body)
