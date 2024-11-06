require('dotenv').config(); // 환경 변수 로드
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

// 환경 변수에서 API 키와 URL 가져오기
const WANTED_API_KEY = process.env.WANTED_API_KEY;
const WANTED_API_URL = process.env.WANTED_API_URL;

// 사용자가 추천 요청을 보낼 때마다 처리하는 엔드포인트
app.get('/recommend', async (req, res) => {
    const { cuisine, location, price_range } = req.query;

    try {
        const response = await axios.post(
            WANTED_API_URL,
            { prompt: `Please recommend a restaurant for ${cuisine} near ${location} within the price range ${price_range}.` },
            { headers: { Authorization: `Bearer ${WANTED_API_KEY}`, "Content-Type": "application/json" } }
        );

        res.json(response.data);
    } catch (error) {
        console.error('Error fetching data from Wanted API:', error);
        res.status(500).json({ message: "Failed to fetch recommendation from Wanted API." });
    }
});

// 서버 시작
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
