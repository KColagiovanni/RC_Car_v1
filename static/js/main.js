function forward(){
    fetch('/forward')
        .then(response => response.json)
        .then(data => console.log(data))
}

function backward(){
    fetch('/backward')
        .then(response => response.json)
        .then(data => console.log(data))
}

function left(){
    fetch('/left')
        .then(response => response.json)
        .then(data => console.log(data))
}

function right(){
    fetch('/right')
        .then(response => response.json)
        .then(data => console.log(data))
}

function stop(){
    fetch('/stop')
        .then(response => response.json)
        .then(data => console.log(data))
}

function toggleLights(){
    fetch('/flashingLights')
        .then(response => response.json)
        .then(data => console.log(data))
}

function sequentialFlashing(){
    console.log("Sequential Flashing Lights")
}

function policeLights(){
    console.log("Police Lights")
}

function pairedFlashing(){
    console.log("Paired Flashing Lights")
}

//function toggleLights(){
//    let flashing_lights =
//    fetch('/flashingLights')
//        .then(response => response.json)
//        .then(data => console.log(data))
//}