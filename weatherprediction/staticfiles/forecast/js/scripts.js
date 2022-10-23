// variables controlling the day, high and low temp
let high_temps = document.getElementsByClassName("high");
let low_temps = document.getElementsByClassName("low");
// default temperature setting
let isCelsius = true;
let celsiusButton = document.getElementById("celsius-button");
let fahrButton = document.getElementById("fahr-button");
// display the current time
let d = new Date();
let n = d.toLocaleTimeString('en-US', {
    year: 'numeric',
    month: 'long',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'America/Los_Angeles',
});


function buildCustomForecast(result){
    let customForecast = document.getElementById("custom-forecast");
    // remove previous data
    customForecast.innerHTML = "";

    // build the elements
    let dayname = document.createElement("p");
    dayname.innerText = result["custom_forecast"]["name"];
    let conditionImage = document.createElement("img");
    conditionImage.className = "conditions";
    conditionImage.src = `/static/${result['custom_forecast']['condition']}`;
    let tempContainer = document.createElement("div");
    tempContainer.className = "temperatures";
    let maxtemp = document.createElement("p");
    maxtemp.innerText = result["custom_forecast"]["temp_max"];
    maxtemp.className = "high";
    let mintemp = document.createElement("p");
    mintemp.innerText = result["custom_forecast"]["temp_min"];
    mintemp.className = "low";

    // add elements
    tempContainer.appendChild(maxtemp);
    tempContainer.appendChild(mintemp);

    customForecast.appendChild(dayname);
    customForecast.appendChild(conditionImage);
    customForecast.appendChild(tempContainer);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function dateTime(){
    let dateTimeDiv = document.getElementById("datetime");
    let p = document.createElement("p");
    p.innerText = "Seattle/Washington " + n;
    dateTimeDiv.appendChild(p);
}

function to_celsius(){
    if(isCelsius == false){
        for(let i=0; i < high_temps.length; i++){
            let high = high_temps[i].innerText;
            let celsius_temp = Math.round((high - 32) * 0.5556);
            high_temps[i].innerText = celsius_temp;
        }

        for(let j=0; j < low_temps.length; j++){
            let low = low_temps[j].innerText;
            let celsius_temp = Math.round((low - 32) * 0.5556);
            low_temps[j].innerText = celsius_temp;
        }

        isCelsius = true;
        celsiusButton.style.backgroundColor = "rgb(85, 135, 200)";
        fahrButton.style.backgroundColor = "rgb(180, 180, 180)";
    }
}

function to_fahrenheit(){
    if(isCelsius){
        for(let i=0; i < high_temps.length; i++){
            let high = high_temps[i].innerText;
            let fahr_temp = Math.round((high * 1.8) + 32);
            high_temps[i].innerText = fahr_temp;
        }

        for(let j=0; j < low_temps.length; j++){
            let low = low_temps[j].innerText;
            let fahr_temp = Math.round((low * 1.8) + 32);
            low_temps[j].innerText = fahr_temp;
        }

        isCelsius = false;
        fahrButton.style.backgroundColor = "rgb(85, 135, 200)";
        celsiusButton.style.backgroundColor = "rgb(180, 180, 180)";
    }
}

window.onload = (event) => {
    dateTime();
}