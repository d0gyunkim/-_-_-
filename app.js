require('dotenv').config(); // 환경 변수 로드
const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
const PORT = 3000;

// 환경 변수에서 API 정보 로드
const WANTED_API_URL = "https://api-laas.wanted.co.kr/api/preset/v2/chat/completions";
const WANTED_API_KEY = process.env.WANTED_API_KEY;
const PROJECT_CODE = process.env.PROJECT_CODE;
const PRESET_HASH = process.env.PRESET_HASH;

app.use(cors()); // CORS 설정

// 사용자 질문을 처리하는 엔드포인트
app.get('/chat', async (req, res) => {
    const userQuestion = req.query.question;

    try {
        // 원티드 챗봇 API 호출
        const response = await axios.post(
            WANTED_API_URL,
            { hash: PRESET_HASH, messages: [{ role: "user", content: userQuestion }] },
            {
                headers: {
                    project: PROJECT_CODE,
                    apiKey: WANTED_API_KEY,
                    "Content-Type": "application/json; charset=utf-8"
                }
            }
        );

        // 챗봇 응답을 클라이언트에 전달
        res.json(response.data.choices[0].message);
    } catch (error) {
        console.error("Error calling Wanted API:", error);
        res.status(500).json({ message: "Failed to fetch response from Wanted API." });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
