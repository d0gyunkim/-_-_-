function getRecommendation() {
    const cuisine = document.getElementById('cuisine').value;
    const location = document.getElementById('location').value;
    const price_range = document.getElementById('price_range').value;

    const url = `http://localhost:3000/recommend?cuisine=${cuisine}&location=${location}&price_range=${price_range}`;

    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error("추천 결과가 없습니다.");
            return response.json();
        })
        .then(data => {
            displayRecommendations(data);
        })
        .catch(error => {
            console.error('Error fetching recommendations:', error);
            alert('조건에 맞는 추천 식당이 없습니다.');
        });
}

function displayRecommendations(data) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ''; // 기존 결과 초기화

    data.recommendations.forEach(restaurant => {
        const restaurantDiv = document.createElement('div');
        restaurantDiv.classList.add('restaurant');
        restaurantDiv.innerHTML = `
            <h3>${restaurant.name}</h3>
            <p>종류: ${restaurant.cuisine}</p>
            <p>위치: ${restaurant.location}</p>
            <p>가격대: ${restaurant.price_range}</p>
            <p>추천 대상: ${restaurant.recommended_for}</p>
        `;
        resultDiv.appendChild(restaurantDiv);
    });
}
