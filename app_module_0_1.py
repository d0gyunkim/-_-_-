# app_module_0.py
from api_utils import send_api_request
from app_module_3_1 import handle_content

def main():
    user_input = input("질문을 입력하세요: ")
    content = send_api_request("deaf7c83c62c5b0f356e3880ddf687c7fc51bc0567a99d83bc88bb48cd0ab091", user_input)
    ques_code, con = content.split(",")

    if ques_code == '3':
        handle_content(con)

if __name__ == "__main__":
    main()
