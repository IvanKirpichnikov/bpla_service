function _nullIfEmptyString(value) {
    if (value === '') {
        return null;
    }
    return value;
}

function getFio() {
    let fioInput = document.getElementById('fio');
    let fio = fioInput.value;
    return _nullIfEmptyString(fio);
}

function getEmail() {
    const emailInput = document.getElementById('email');
    let email = emailInput.value;
    return _nullIfEmptyString(email);
}

function getPassword() {
    const passwordInput = document.getElementById('password');
    let password = passwordInput.value;
    return _nullIfEmptyString(password);
}

function getGender() {
    let genderRadio = document.querySelector('input[name="gender"]:checked')
    if (genderRadio === null) {
        return null;
    }
    let gender = genderRadio.value;
    return _nullIfEmptyString(gender);
}

function getIssuedBy() {
    let issuedByInput = document.getElementById('issued_by');
    let issuedBy = issuedByInput.value;
    return _nullIfEmptyString(issuedBy);
}

function getDateOfIssue() {
    let dateOfIssueInput = document.getElementById('issue_date');
    let dateOfIssue = dateOfIssueInput.value;
    return _nullIfEmptyString(dateOfIssue);
}

function getSubdivisionCode() {
    let subdivisionCodeInput = document.getElementById('subdivision_code');
    let subdivisionCode = subdivisionCodeInput.value;
    return _nullIfEmptyString(subdivisionCode);
}

function getYearOfBirth() {
    let yearOfBirthInput = document.getElementById('year_of_birth');
    let yearOfBirth = yearOfBirthInput.value;
    return _nullIfEmptyString(yearOfBirth);
}

function getPlaceOfBirth() {
    let placeOfBirthInput = document.getElementById('place_of_birth')
    let placeOfBirth = placeOfBirthInput.value;
    return _nullIfEmptyString(placeOfBirth);
}

function getSerialNumber() {
    let serialNumberInput = document.getElementById('serial_number')
    let serialNumber = serialNumberInput.value;
    return _nullIfEmptyString(serialNumber);
}

function getNumber() {
    let numberInput = document.getElementById('number')
    let number = numberInput.value;
    return _nullIfEmptyString(number);
}

function getSnils() {
    let snilsInput = document.getElementById('snils')
    let snils = snilsInput.value;
    return _nullIfEmptyString(snils);
}

function getFormData() {
    let fio = getFio();
    let email = getEmail();
    let password = getPassword();
    let gender = getGender();
    let issuedBy = getIssuedBy();
    let dateOfIssue = getDateOfIssue();
    let subdivisionCode = getSubdivisionCode();
    let yearOfBirth = getYearOfBirth();
    let placeOfBirth = getPlaceOfBirth();
    let serialNumber = getSerialNumber();
    let number = getNumber();
    let snils = getSnils();

    let values = [
        fio,
        email,
        password,
        gender,
        issuedBy,
        dateOfIssue,
        subdivisionCode,
        yearOfBirth,
        placeOfBirth,
        serialNumber,
        number,
        snils,
    ];
    if (values.includes(null)) {
        return null;
    }

    return {
        email: email,
        password: password,
        passport_data: {
            fio: fio,
            gender: gender,
            issued_by: issuedBy,
            date_of_issue: dateOfIssue,
            subdivision_code: subdivisionCode,
            year_of_birth: yearOfBirth,
            place_of_birth: placeOfBirth,
            serial_number: serialNumber,
            number: number,
            snils: snils,
        },
    }
}

async function loginCallback() {
    const formData = getFormData();
    if (!formData) {
        alert('Заполни все поля');
        return;
    }
    const request = await fetch(
        '/api/login',
        {
            method: 'POST',
            body: JSON.stringify(formData),
            headers: {
                'Content-Type': 'application/json',
            },
        }
    );
    if (request.status === 200) {
        window.location.href = '/me';
    }
}

function onStartup() {
    let dateIdInputs = ['year_of_birth', 'issue_date']
    for (const dateIdInput of dateIdInputs) {
        let dateInput = document.getElementById(dateIdInput);
        dateInput.max = new Date().toISOString().split("T")[0];
    }

    document.getElementById('login').addEventListener('click', loginCallback);
}


onStartup();
