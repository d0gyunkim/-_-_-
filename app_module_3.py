import requests
from dotenv import load_dotenv
import os
import json

def handle_content(con):
    # 환경 변수 로드
    load_dotovt

    # Header 설정
    header = {
        "project": "KHU_PROMPTHON_018", 
        "apiKey": os.getenv("WANTED_API_KEY")
    }

    body = {
      "hash": "28a2be4d1b3e5313220524dddd3a71ed6c1fdc71e98294e52201193906b639c7", 
      "params": {"campus": con} 
    }

    # API URL 가져오기
    URL = os.getenv("WANTED_API_URL")

    # POST 요청
    response = requests.post(URL, headers=header, json=body)

    # 응답 출력
    if response.ok:
        content = response.json()["choices"][0]["message"]["content"]
        print("Handled Content in Module 3:", content)
    else:
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
