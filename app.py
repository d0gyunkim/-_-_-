import os
import sys
import requests
import json
from dotenv import load_dotenv
from functions import *
from datetime import datetime

# 환경 변수 로드
load_dotenv()

# API URL 가져오기
URL = os.getenv("WANTED_API_URL")

# Header 설정
header = {
    "project": "KHU_PROMPTHON_018", 
    "apiKey": os.getenv("WANTED_API_KEY")
}

# 모듈 hash 딕셔너리 만들기
module_hash = {
    "0": "1302b0ca506baadf1ae4b5090e10d21c82d71e3eb63c746670496f85cd8cd3d6",
    "3": "c0d17e57929ea2d5d3c20361c8274a99ab2178d4907fe04542fc31c9f5987b1d"
}

params_dict = {
    "0": None,
    "3": {"today_datetime": datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")}
}

module_num = "0"
ask_for_input = True

while True:
    print("현재 모듈:", module_num)

    # 질문 입력
    if ask_for_input:
        user_input = input("무엇이 궁금하세요?: ")
        if user_input == "exit":
            break

    # body 생성
    body = create_body(module_hash[module_num], params=params_dict[module_num], input=user_input)

    content, module_num = call_module(URL, header, body)

    if module_num in ["98", "99"]:
        module_num = "0"

    # 출력값과 사용자 입력값 비교
    if user_input in content:
        ask_for_input = False
    else:
        ask_for_input = True
        print(content)
    
    user_input = content


if __name__ == "__main__":
    pass