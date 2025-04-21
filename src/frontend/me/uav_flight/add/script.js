function _null_if_empty_string(value) {
    if (value === '') {
        return null;
    }
    return value;
}

function get_location() {
    return _null_if_empty_string(document.getElementById('location').value);
}

function get_uav_id() {
    return _null_if_empty_string(document.getElementById('uav').value);
}

function get_start_at() {
    return _null_if_empty_string(document.getElementById('start_at').value);
}

function get_end_at() {
    return _null_if_empty_string(document.getElementById('end_at').value);
}

function get_form_data() {
    let location = get_location();
    let uav_id = get_uav_id();
    let start_at = get_start_at();
    let end_at = get_end_at();

    let data_array = [location, uav_id, start_at, end_at];
    if (data_array.includes(null)) {
        return null;
    }

    return {
        location: location,
        uav_id: uav_id,
        start_at: start_at,
        end_at: end_at
    }
}

async function add_uav_flight() {
    let form_data = get_form_data();
    if (form_data === null) {
        alert('Заполни все данные');
        return null;
    }

    let request = await fetch('/api/uav_flight', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(form_data),
    });
    alert('Полет успешно добавлен');
    back();
}

function set_uavs(uavs) {
    let uav_select = document.getElementById('uav');
    for (let uav of uavs.uavs) {
        let option = document.createElement('option');
        option.value = uav.id;
        option.text = uav.model;
        uav_select.add(option);
    }
}

function back() {
    document.location.href = '/me/uav_flights';
}

fetch(
    '/api/uavs',
    {
        method: 'GET',
    },
).then(
    (response) => {
        response.json().then(set_uavs)
    },
)
document
    .getElementById('add')
    .addEventListener('click', add_uav_flight);

document
    .getElementById('back')
    .addEventListener('click', back);