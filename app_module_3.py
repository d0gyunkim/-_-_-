# app_module_3.py: 장학팀에 관한 정보(메일,전화번호,팩스번호)등을 처리하는 함수
from api_utils import send_api_request

def handle_content(con,campus):
    """ 특정 질문 유형에 대한 내용을 처리합니다. """
    content = send_api_request("c0d17e57929ea2d5d3c20361c8274a99ab2178d4907fe04542fc31c9f5987b1d", con,campus)
    print("Handled Content in Module 3:", content)
