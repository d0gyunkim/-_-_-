# app_module_0.py: 질문 유형 분류를 처리하는 모듈
# app_module_0.py
from api_utils import send_api_request
from app_module_3 import handle_content

def main():
    while True:
        user_input = input("질문을 입력하세요 (종료하려면 '종료' 입력): ")
        if user_input.lower() == '종료':
            print("질문 입력을 종료합니다.")
            break

        content = send_api_request("deaf7c83c62c5b0f356e3880ddf687c7fc51bc0567a99d83bc88bb48cd0ab091", user_input)
        ques_code, con = content.split(",")

        # ques_code에 따라 적절한 모듈 호출
        if ques_code == '3':
            handle_content(con)
        else:
            print("현재 처리할 수 있는 질문 유형이 아닙니다. 다른 질문 유형의 모듈을 추가하세요.")

if __name__ == "__main__":
    main()

