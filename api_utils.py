# api_utils.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_api_request(hash_value, question):
    """ API 요청을 전송하고 응답을 반환합니다. """
    header = {
        "project": "KHU_PROMPTHON_018",
        "apiKey": os.getenv("WANTED_API_KEY")
    }
    body = {
        "hash": hash_value,
        "params": {"question": question}
    }
    url = os.getenv("WANTED_API_URL")

    response = requests.post(url, headers=header, json=body)
    if response.ok:
        return response.json()["choices"][0]["message"]["content"]
    else:
        response.raise_for_status()  # 오류 발생 시 예외를 발생시킵니다.