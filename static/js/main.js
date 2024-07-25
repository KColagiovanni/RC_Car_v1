// Fetch info: https://www.geeksforgeeks.org/javascript-fetch-method/

// Fetch the forward() method from app.py to move the car in the forward direction.
function forward(){
    fetch('/forward')
}

// Fetch the backward() method from app.py to move the car in the backward direction.
function backward(){
    fetch('/backward')
}

// Fetch the left() method from app.py to turn the car to the left.
function left(){
    fetch('/left')
}

// Fetch the right() method from app.py to turn the car to the right.
function right(){
    fetch('/right')
}

// Fetch the stop() method from app.py to stop car movement.
function stop(){
    fetch('/stop')
}

// Fetch the horn() method from app.py to beep the horn.
function horn(){
    fetch('/horn')
}

// Fetch the hornStop() method from app.py to stop the horn from beeping.
function hornStop(){
    fetch('/hornStop')
}
