# api_utils.py: , API 요청과 응답 처리를 위한 공통 유틸리티 함수
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_api_request(hash_value, question,campus):
    """ API 요청을 전송하고 응답을 반환합니다. """
    header = {
        "project": "KHU_PROMPTHON_018",
        "apiKey": os.getenv("WANTED_API_KEY")
    }
    body = {
        "hash": hash_value,
         "params": {"question":"경희대 국캠 장학팀 번호","campus":""} 
}
    url = os.getenv("WANTED_API_URL")

    response = requests.post(url, headers=header, json=body)
    if response.ok:
        return response.json()["choices"][0]["message"]["content"]
    else:
        response.raise_for_status()  # 오류 발생 시 예외를 발생시킵니다.
