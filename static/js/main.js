function forward(){
    fetch('/forward')
        .then(response => response.json)
        .then(data => console.log(data))
}
