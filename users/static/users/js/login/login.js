let username = document.querySelector('.name'),
    password = document.querySelector('.password'),
    logaut = document.querySelector('.logaut'),
    send = document.querySelector('.send');

function getCookie(name) {
    let cookie = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return cookie ? cookie[2] : null;
}


send.addEventListener('click', () => {
    fetch('http://127.0.0.1:8000/auth/token/login/', {
        method: "POST", headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            'Content-type': 'application/json'
        }, body: JSON.stringify({
            "username": username.value,
            'password': password.value
        }),
    })
        .then(response => response.json())
        .then(resp => {
            localStorage.setItem('token', resp['auth_token'])
            console.log(resp['auth_token'])
        })
})

logaut.addEventListener('click', () => {
    const getToken = localStorage.getItem('token');
    console.log(getToken)
    fetch('http://127.0.0.1:8000/auth/token/logout/', {
        method: "POST", headers: {
            'Authorization': `Token ${getToken}`,
        }
    })
    localStorage.removeItem('token');
})