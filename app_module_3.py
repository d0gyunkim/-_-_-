# app_module_3.py: 장학팀에 관한 정보(메일,전화번호,팩스번호)등을 처리하는 함수
import requests
from dotenv import load_dotenv
import os
import json

def handle_content(con):
    # 환경 변수 로드
    load_dotenv()

    # Header 설정
    header = {
        "project": "KHU_PROMPTHON_018", 
        "apiKey": os.getenv("WANTED_API_KEY")
    }

    body = {
      "hash": "c0d17e57929ea2d5d3c20361c8274a99ab2178d4907fe04542fc31c9f5987b1d", 
       "params": {"question":con,"campus":""} 
}

    # API URL 가져오기
    URL = os.getenv("WANTED_API_URL")

    # POST 요청
    response = requests.post(URL, headers=header, json=body)

    # 응답 출력
    if response.ok:
        content = response.json()["choices"][0]["message"]["content"]
        print("Handled Content in Module 3:", content)
        print("body: ",body)
    else:
        print("Response status code:", response.status_code)
        print("Response content:", response.text)