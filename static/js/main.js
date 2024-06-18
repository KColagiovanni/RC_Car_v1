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

//function toggleLights(){
//    fetch('/flashingLights')
//        .then(response => response.json)
//        .then(data => console.log(data))
//}

function sequentialFlashing(){
    var slow = document.getElementById("slowFlashSpeed");
    var intermediate = document.getElementById("intermediateFlashSpeed");
    var fast = document.getElementById("fastFlashSpeed");
    var flashSpeed;

    if (slow.checked == true){
        flashSpeed = 0.5
    } else if (intermediate.checked == true){
        flashSpeed = 0.25
    } else {
        flashSpeed = 0.1
    }
    response = {'data': flashingSpeed}
    fetch('/sequentialFlashing')
        .then(response => response.json)
        .then(data => console.log(data))

    console.log("Sequential Flashing Lights")
}

function policeLights(){
    fetch('/policeLights')
        .then(response => response.json)
        .then(data => console.log(data))

    console.log("Police Lights")
}

function pairedFlashing(){
    fetch('/pairedFlashing')
        .then(response => response.json)
        .then(data => console.log(data))

    console.log("Paired Flashing Lights")
}

//function toggleLights(){
//    let flashing_lights =
//    fetch('/flashingLights')
//        .then(response => response.json)
//        .then(data => console.log(data))
//}