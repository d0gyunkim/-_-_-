# 장학팀에 관한 정보를 내보내주는 모듈
import os
import requests
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

class Module3Handler:
    def __init__(self):
        self.header = {
            "project": "KHU_PROMPTHON_018",
            "apiKey": os.getenv("WANTED_API_KEY")
        }
        self.url = os.getenv("WANTED_API_URL")

    def handle_content(self, content):
        # 장학금 관련 질문 처리
        body = {
            "hash": "c0d17e57929ea2d5d3c20361c8274a99ab2178d4907fe04542fc31c9f5987b1d",
            "params": {
                "question": content,
                "campus": "",
                "today_datetime": "11/8/2024 3pm"
            }
        }
        
        response = requests.post(self.url, headers=self.header, json=body)
        
        if response.ok:
            response_content = response.json()["choices"][0]["message"]["content"]
            print("Handled Content in Module 3:", response_content)
        else:
            print("Response status code:", response.status_code)
            print("Response content:", response.text)
