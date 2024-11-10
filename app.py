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
    "0": "f8313ae5c1fe28fb0c8b404c4170ab87b09a4eeb55e0e2c8ce82a7ed96ab4fe9",
    "2": "ebd6fa183228d8748c95f4ec649c5121fde4d0b3cc0730cd69c52a1432ac5bc8",
    "3": "c0d17e57929ea2d5d3c20361c8274a99ab2178d4907fe04542fc31c9f5987b1d",
    "99": "f47196f6724e7022fd3b99472ecbbd7c0278a0b8103e3c98466d48c2c7571550"
}

params_dict = {
    "0": None,
    "2": None,
    "3": {"today_datetime": datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")},
    "99": None
}

module_num = "0"
ask_for_input = True

# log.txt 파일 생성
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write("")

while True:
    print("While loop 시작")

    # 질문 입력
    if ask_for_input:
        # 사용자 입력 받기
        user_input = input("무엇이 궁금하세요?: ")
        if user_input == "exit":
            break
        
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write("user: " + user_input + "\n")
        with open('log.txt', 'r', encoding='utf-8') as f:
            log = f.read()
        
        recall_body = {
            "hash": "0c9e4ff01af16290c09306f5ead960cc6357340fe129f56125458c57317d6191",
            "messages": [{"role": "user", "content": log}]
        }
            
        # 요약 모듈 호출
        print("Recall Module 호출")
        recall_output = requests.post(URL, headers=header, json=recall_body)

        if recall_output.ok:
            recall_content = recall_output.json()["choices"][0]["message"]["content"]
            # recall_log.txt 파일 생성
            with open('recall_log.txt', 'w', encoding='utf-8') as f:
                f.write(recall_content)

            api_input = recall_content + "\n 사용자 질문:" + user_input
        else:
            print("Recall Error\n")
            print("Recall module response status code:", recall_output.status_code)
            api_input = user_input
    
    print("api_input: ", api_input)

    # 모듈 0 호출
    print("모듈 0 호출")
    
    # body 생성
    module_0_body = create_body(module_hash["0"], params=None, input=api_input)

    content, module_num = call_module(URL, header, module_0_body, module_num="0")
        
    # 다른 모듈 호출
    print("모듈 " + module_num + " 호출")
    module_body = create_body(module_hash[module_num], params=params_dict[module_num], input=content)

    content = call_module(URL, header, module_body, module_num)[0]

    # log.txt 파일에 답변내용 기록하고 출력
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write("AI: " + content + "\n")
    print("답변: " + content)

# log.txt 및 recall_log.txt 파일 삭제
os.remove('log.txt')
os.remove('recall_log.txt')

if __name__ == "__main__":
    pass