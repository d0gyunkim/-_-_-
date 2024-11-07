import requests
from dotenv import load_dotenv
import os
import json
from app_module_3 import handle_content  # app_module_3에서 함수를 가져옵니다

# 환경 변수 로드
load_dotenv()

user_input = input("질문을 입력하세요: ")
# Header 설정
header = {
    "project": "KHU_PROMPTHON_018", 
    "apiKey": os.getenv("WANTED_API_KEY")
}

# Body 설정
body = {
  "hash": "deaf7c83c62c5b0f356e3880ddf687c7fc51bc0567a99d83bc88bb48cd0ab091", 
 "params": {"question": user_input} 
}

# API URL 가져오기
URL = os.getenv("WANTED_API_URL")

# POST 요청서ㅇ
response = requests.post(URL, headers=header, json=body)

# 응답 출력
if response.ok:
    content = response.json()["choices"][0]["message"]["content"]
    print("Content:", content)
    ques_code, con = content.split(",")
    print("ques_code:", ques_code)
    # 만약 ques_code == 3 일경우, app_module_3의 handle_content 함수를 호출
    if ques_code == '3':
       handle_content(con)
else:
    print("Response status code:", response.status_code)
    print("Response content:", response.text)
