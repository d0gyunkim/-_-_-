const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});





function getRecommendation() {
    // 사용자가 입력한 값을 가져옴
    const cuisine = document.getElementById('cuisine').value;
    const location = document.getElementById('location').value;
    const price_range = document.getElementById('price_range').value;

    // 백엔드 서버에 추천 요청 보내기
    const url = `http://localhost:3000/recommend?cuisine=${cuisine}&location=${location}&price_range=${price_range}`;

    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error("추천 결과가 없습니다.");
            return response.json();
        })
        .then(data => {
            displayRecommendation(data);
        })
        .catch(error => {
            console.error("Error fetching recommendations:", error);
            alert("추천을 불러오는 데 문제가 발생했습니다.");
        });
}

// 추천 결과를 화면에 표시
function displayRecommendation(data) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ''; // 기존 결과 초기화

    // 추천 결과를 HTML로 표시
    const message = document.createElement('p');
    message.textContent = data.content; // 챗봇 응답 텍스트
    resultDiv.appendChild(message);
}
