var date_time_options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };

function setUav(uav_flight) {
    let tr_uav = document.createElement('tr');
    let location_td = document.createElement('td');
    let model_td = document.createElement('td');
    let status_td = document.createElement('td');
    let start_at_td = document.createElement('td');
    let end_at_td = document.createElement('td');
    let created_at_td = document.createElement('td');

    tr_uav.className = 'hover:bg-gray-100';
    tr_uav.addEventListener('click', () => window.location.href = `/me/uav_flight?uav_flight_id=${uav_flight.id}`);

    location_td.innerHTML += uav_flight.location;
    location_td.classNaze = 'py-2 px-4 border-b';

    fetch(
        `/api/uav/${uav_flight.uav_id}`,
        {
            method: 'GET',
        },
    ).then(
        response => response.json().then(uav => model_td.innerHTML += uav.model)
    )
    model_td.className = 'py-2 px-4 border-b';

    status_td.innerHTML += status_map.get(uav_flight.status);
    status_td.className = 'py-2 px-4 border-b';

    start_at_td.innerHTML += (new Date(uav_flight.start_at)).toLocaleString('ru-RU', date_time_options);
    start_at_td.className = 'py-2 px-4 border-b';

    end_at_td.innerHTML += (new Date(uav_flight.end_at)).toLocaleString('ru-RU', date_time_options);
    end_at_td.className = 'py-2 px-4 border-b';

    created_at_td.innerHTML += (new Date(uav_flight.created_at)).toLocaleString('ru-RU', date_time_options);
    created_at_td.className = 'py-2 px-4 border-b';

    tr_uav.appendChild(location_td);
    tr_uav.appendChild(model_td);
    tr_uav.appendChild(status_td);
    tr_uav.appendChild(start_at_td);
    tr_uav.appendChild(end_at_td);
    tr_uav.appendChild(created_at_td);

    return tr_uav;
}

function setUavs(uavs) {
    let tBody = document.getElementById('tbody');
    for (const uav of uavs) {
        tBody.appendChild(setUav(uav));
    }
}
let status_map = new Map(
    [
        ["accepted", "Принят"],
        ["rejected", "Отклонен"],
        ["finished", "Завершен"],
        ["under_review", "В обработке"],
    ],
)
fetch(
    '/api/uav_flights',
    {
        method: 'GET',
    },
).then(
    (response) => {
        response.json().then(setUavs)
    },
);


document
    .getElementById('add-uav-flight')
    .addEventListener(
        'click',
        () => { window.location.href = '/me/uav_flight/add' },
    );

document
    .getElementById('back')
    .addEventListener(
        'click',
        () => { document.location.href = '/me' },
    );