require('dotenv').config(); // 환경 변수 로드
const axios = require('axios');
const express = require('express');
const app = express();
const PORT = 3000;

// 환경 변수에서 API 정보 로드
const WANTED_API_URL = process.env.WANTED_API_URL;
const WANTED_API_KEY = process.env.WANTED_API_KEY;
const PROJECT_CODE = process.env.PROJECT_CODE;
const PRESET_HASH = process.env.PRESET_HASH;

// 추천 요청을 처리하는 엔드포인트
app.get('/recommend', async (req, res) => {
    const { cuisine, location, price_range } = req.query;
    const prompt = `Please recommend a restaurant for ${cuisine} near ${location} within the price range ${price_range}.`;

    try {
        // 원티드 LAAS API의 특정 프리셋 호출
        const response = await axios.post(
            WANTED_API_URL,
            { hash: PRESET_HASH, messages: [{ role: "user", content: prompt }] },
            {
                headers: {
                    project: PROJECT_CODE,
                    apiKey: WANTED_API_KEY,
                    "Content-Type": "application/json; charset=utf-8"
                }
            }
        );

        // 응답을 클라이언트에 전달
        res.json(response.data.choices[0].message);
    } catch (error) {
        console.error("Error fetching data from Wanted API:", error);
        res.status(500).json({ message: "Failed to fetch recommendation from Wanted API." });
    }
});

// 서버 실행
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
