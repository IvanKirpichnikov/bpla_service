async function logout() {
    let response = await fetch(
        '/api/logout',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        },
    )
    if (response.status === 200) {
        window.location.href = '/';
    }
}

function setMeData(me) {
    let fio = document.getElementById('fio');
    let email = document.getElementById('email');
    let createdAt = document.getElementById('created_at');

    fio.innerHTML = me.fio;
    fio.className = fio.className.replace(' animate-pulse', '');

    email.innerHTML = me.email;
    email.className = email.className.replace(' animate-pulse', '');

    createdAt.innerHTML = me.created_at.toLocaleString('ru-RU', date_time_options);
    createdAt.className = createdAt.className.replace(' animate-pulse', '');
}

async function get_me() {
    let response = await fetch(
        '/api/me',
        {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        },
    );
    let data = await response.json();
    return {
        id: data.id,
        fio: data.fio,
        email: data.email,
        created_at: new Date(data.created_at),
    }
}

var date_time_options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
get_me().then(setMeData);

document.getElementById('logout1').addEventListener('click', logout);
document.getElementById('logout2').addEventListener('click', logout);