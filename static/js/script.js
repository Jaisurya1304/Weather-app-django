function getLocationData() {
    if (!navigator.geolocation) {
        alert("Geolocation is not supported by this browser.");
        return;
    }

    navigator.geolocation.getCurrentPosition((position) => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        fetch(`/weather/?lat=${latitude}&lon=${longitude}`, { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                updateWeatherUI(data);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error fetching weather data. Please try again later.');
            });
    });
}

function updateWeatherUI(data) {
    document.getElementById("city").textContent = data.city;
    document.getElementById("temperature-degree").textContent = `${data.temp} °C`;
    document.getElementById("humidity-degree").textContent = `${data.humidity} %`;
    document.getElementById("feelslike-degree").textContent = `${data.feels_like} °C`;
    document.getElementById("description-text").textContent = data.description;
    document.getElementById("description-img").src = `http://openweathermap.org/img/wn/${data.icon}.png`;
}
