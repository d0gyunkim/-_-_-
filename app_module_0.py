# app_module_0.py 수정된 버전
from api_utils import send_api_request
from app_module_3 import handle_content
import uuid

# 세션 데이터를 저장할 딕셔너리
sessions = {}

def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {"history": []}
    return sessions[session_id]

def main():
    session_id = str(uuid.uuid4())  # 신규 세션 ID 생성

    while True:
        user_input = input("질문을 입력하세요 (종료하려면 '종료' 입력): ")
        if user_input.lower() == '종료':
            print("질문 입력을 종료합니다.")
            break

        session = get_session(session_id)  # 세션 정보 가져오기
        content = send_api_request("deaf7c83c62c5b0f356e3880ddf687c7fc51bc0567a99d83bc88bb48cd0ab091", user_input)
        ques_code, con = content.split(",")

        # 질문 기록을 세션에 저장
        session["history"].append({"question": user_input, "response": content})

        # ques_code에 따라 적절한 모듈 호출
        if ques_code == '3':
            handle_content(con, session_id)  # 세션 ID를 함께 전달
        else:
            print("현재 처리할 수 있는 질문 유형이 아닙니다. 다른 질문 유형의 모듈을 추가하세요.")

if __name__ == "__main__":
    main()
