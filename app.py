import requests
from dotenv import load_dotenv
import os
import json

# 환경 변수 로드
load_dotenv()


# Header와 Body 설정
header = {
    "project": "KHU_PROMPTHON_018", 
    "apiKey": os.getenv("WANTED_API_KEY")
}
# 동적으로 값을 넣기 위한 예시 값들
현재회사 = "경희대"
직무 = "학생"
경력기간 = "2년"
주요업무 = "공부"
소속 = "빅응"
작성언어 = "한국어"

body = {
    "hash": "2cc6f00d01058516d8d0ac3b062a2547679aaef311d22b82400aa82f8ef4be47", 
    "params": {
        "task": f"1. 현재 회사: {현재회사}\n2. 직무: {직무}\n3. 경력기간: {경력기간}\n4. 주요업무: {주요업무}\n5. 소속: {소속}\n작성 언어: {작성언어}",
        "현재회사": 현재회사,
        "직무": 직무,
        "경력기간": 경력기간,
        "주요업무": 주요업무,
        "소속": 소속,
        "작성언어": 작성언어
    }
}

# URL 가져오기
URL = os.getenv("WANTED_API_URL")

# json 매개변수를 사용하여 POST 요청
response = requests.post(URL, headers=header, json=body)

# 응답 출력
# 응답에서 content 키의 값만 출력
if response.ok:
    content = response.json()["choices"][0]["message"]["content"]
    print("Content:", content)
else:
    print("Response status code:", response.status_code)
    print("Response content:", response.text)