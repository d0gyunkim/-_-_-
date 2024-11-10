import os
import sys
import requests
import json

def create_body(module_hash, params=None, input=None):
    # Body 설정
    body = {
        "hash": module_hash,
        "params": params
    }
    if input is not None:
        body["messages"] = [{"role": "user", "content": input}]

    return body


def call_module(URL, header, body, module_num):
    # POST 요청
    response = requests.post(URL, headers=header, json=body)

    # save response to json file
    with open('response.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

    # 모듈에서 받은 응답 확인
    if response.ok:
        content = response.json()["choices"][0]["message"]["content"]

        if module_num == "0":
            output, ques_code = content.split("---")
            return output, ques_code
        else:
            return content, None
        
    else:
        print("Error: Response status code:", response.status_code)
        print("Response content:", response.text)

        return None, None