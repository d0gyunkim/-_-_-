document.querySelectorAll('.keyword').forEach(item => {
    item.addEventListener('click', event => {
        const keyword = item.textContent;
        document.getElementById('detailContent').textContent = `${keyword}에 대한 정보를 여기서 찾을 수 있습니다.`;
    });
});

document.getElementById('recommendBtn').addEventListener('click', () => {
    const priceRange = document.getElementById('priceRange').value;
    const people = document.getElementById('people').value;
    alert(`추천 결과: 가격대 ${priceRange}에서 ${people}와 함께 할 수 있는 맛집을 찾습니다.`);
});
