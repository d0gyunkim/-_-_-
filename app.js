require('dotenv').config(); // 환경 변수 로드
const express = require('express');
const axios = require('axios');
const cors = require('cors'); // CORS 설정
const app = express();
const PORT = 3000;

// 환경 변수에서 API URL과 API 키 가져오기
const WANTED_API_URL = process.env.WANTED_API_URL;
const WANTED_API_KEY = process.env.WANTED_API_KEY;

app.use(cors()); // CORS 설정으로 프론트엔드와 통신 허용

// 추천 요청을 처리하는 엔드포인트
app.get('/recommend', async (req, res) => {
    const { cuisine, location, price_range } = req.query;

    try {
        // 원티드 API에 요청 보내기
        const response = await axios.post(
            WANTED_API_URL,
            {
                messages: [
                    { role: "user", content: `Please recommend a restaurant for ${cuisine} near ${location} within the price range ${price_range}.` }
                ]
            },
            {
                headers: {
                    Authorization: `Bearer ${WANTED_API_KEY}`,
                    "Content-Type": "application/json"
                }
            }
        );

        // 원티드 API 응답을 클라이언트에 전달
        res.json(response.data.choices[0].message); // 응답 메시지
    } catch (error) {
        console.error("Error fetching data from Wanted API:", error);
        res.status(500).json({ message: "Failed to fetch recommendation from Wanted API." });
    }
});

// 서버 시작
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
