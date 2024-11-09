# app_module_0.py : 질문을 특정 숫자로 분류해주는 모듈
import os
import requests
from dotenv import load_dotenv
from app_module_3 import Module3Handler
# 필요한 경우 다른 모듈도 import

# 환경 변수 로드
load_dotenv()

class QuestionClassifier:
    def __init__(self):
        self.header = {
            "project": "KHU_PROMPTHON_018",
            "apiKey": os.getenv("WANTED_API_KEY")
        }
        self.url = os.getenv("WANTED_API_URL")

    def classify_question(self, question):
        body = {
            "hash": "deaf7c83c62c5b0f356e3880ddf687c7fc51bc0567a99d83bc88bb48cd0ab091",
            "params": {"question": question}
        }
        response = requests.post(self.url, headers=self.header, json=body)
        
        if response.ok:
            content = response.json()["choices"][0]["message"]["content"]
            ques_code, con = content.split(",")
            print(f"Question Type Code: {ques_code}, Content: {con}")
            return ques_code, con
        else:
            print("Response status code:", response.status_code)
            print("Response content:", response.text)
            return None, None

    def handle_question(self, ques_code, content):
        if ques_code == '3':
            Module3Handler().handle_content(content)
        # 새로운 질문 유형에 대한 핸들러 추가 가능
        # 예: elif ques_code == '4': Module4Handler().handle_content(content)

class QuestionManager:
    def __init__(self):
        self.classifier = QuestionClassifier()

    def start(self):
        while True:
            user_input = input("질문을 입력하세요 (종료하려면 'exit' 입력): ")
            if user_input.lower() == "exit":
                print("프로그램을 종료합니다.")
                break

            ques_code, content = self.classifier.classify_question(user_input)
            if ques_code:
                self.classifier.handle_question(ques_code, content)

# 실행 예시
if __name__ == "__main__":
    manager = QuestionManager()
    manager.start()
