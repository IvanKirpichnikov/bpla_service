const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

async function authCallback() {
    if (emailInput.value && passwordInput.value) {
        const request = await fetch(
            '/api/auth',
            {
                method: 'POST',
                body: JSON.stringify({
                    email: emailInput.value,
                    password: passwordInput.value,
                },
            ),
            headers: {'Content-Type': 'application/json'},
        });
        console.log(request);
        if (request.status === 200) {
            window.location.href = '/me';
        }
        else {
            alert('Неправильный логин или пароль');
        }
    }
    else {
        alert('Заполни все поля');
    }
}


document.getElementById('auth_button').addEventListener('click', authCallback);