# app_module_3.py
from api_utils import send_api_request

def handle_content(con):
    """ 특정 질문 유형에 대한 내용을 처리합니다. """
    content = send_api_request("28a2be4d1b3e5313220524dddd3a71ed6c1fdc71e98294e52201193906b639c7", con)
    print("Handled Content in Module 3:", content)
