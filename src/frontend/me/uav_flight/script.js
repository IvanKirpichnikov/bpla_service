function set_uav_flight(uav_flight) {
    let location_div = document.getElementById('location');
    let uav_model_div = document.getElementById('uav_model');
    let status_div = document.getElementById('status');
    let start_at_div = document.getElementById('start_at');
    let end_at_div = document.getElementById('end_at');
    let created_at_div = document.getElementById('created_at');

    location_div.textContent = uav_flight.location;
    location_div.className = location_div.className.replace(' animate-pulse', '');

    fetch(
        `/api/uav/${uav_flight.uav_id}`,
        { method: 'GET' },
    ).then(
        response => response.json().then(uav => uav_model_div.textContent = uav.model)
    )
    uav_model_div.className = uav_model_div.className.replace(' animate-pulse', '');

    status_div.textContent = status_map.get(uav_flight.status);
    status_div.className = status_div.className.replace(' animate-pulse', '');

    start_at_div.textContent = (new Date(uav_flight.start_at)).toLocaleString('ru-RU', date_time_options);
    start_at_div.className = start_at_div.className.replace(' animate-pulse', '');

    end_at_div.textContent = ( new Date(uav_flight.end_at)).toLocaleString('ru-RU', date_time_options);
    end_at_div.className = end_at_div.className.replace(' animate-pulse', '');

    created_at_div.textContent = ( new Date(uav_flight.start_at)).toLocaleString('ru-RU', date_time_options);
    created_at_div.className = created_at_div.className.replace(' animate-pulse', '');
}

let status_map = new Map(
    [
        ["accepted", "Принят"],
        ["rejected", "Отклонен"],
        ["finished", "Завершен"],
        ["under_review", "В обработке"],
    ],
)

var date_time_options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
let query_params = new URLSearchParams(window.location.search);
let uav_flight_id = query_params.get('uav_flight_id');

if (uav_flight_id == null) {
    document.location.href = '/me/uav_flights';
}

fetch(
    `/api/uav_flight/${uav_flight_id}`,
    { method: 'GET' },
).then(response => response.json().then(set_uav_flight));

document.getElementById('back').addEventListener('click', () => {document.location.href = '/me/uav_flights'});
