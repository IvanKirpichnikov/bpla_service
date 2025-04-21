// var date_time_options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
// 
// function setUav(uav_flight) {
//     let tr_uav = document.createElement('tr');
//     let location_td = document.createElement('td');
//     let model_td = document.createElement('td');
//     let status_td = document.createElement('td');
//     let start_at_td = document.createElement('td');
//     let end_at_td = document.createElement('td');
//     let created_at_td = document.createElement('td');
// 
//     tr_uav.className = 'hover:bg-gray-100';
//     tr_uav.addEventListener('click', () => window.location.href = `/me/uav_flight?uav_flight_id=${uav_flight.id}`);
// 
//     location_td.innerHTML += uav_flight.location;
//     location_td.classNaze = 'py-2 px-4 border-b';
// 
//     fetch(
//         `/api/uav/${uav_flight.uav_id}`,
//         {
//             method: 'GET',
//         },
//     ).then(
//         response => response.json().then(uav => model_td.innerHTML += uav.model)
//     )
//     model_td.className = 'py-2 px-4 border-b';
// 
//     status_td.innerHTML += status_map.get(uav_flight.status);
//     status_td.className = 'py-2 px-4 border-b';
// 
//     start_at_td.innerHTML += (new Date(uav_flight.start_at)).toLocaleString('ru-RU', date_time_options);
//     start_at_td.className = 'py-2 px-4 border-b';
// 
//     end_at_td.innerHTML += (new Date(uav_flight.end_at)).toLocaleString('ru-RU', date_time_options);
//     end_at_td.className = 'py-2 px-4 border-b';
// 
//     created_at_td.innerHTML += (new Date(uav_flight.created_at)).toLocaleString('ru-RU', date_time_options);
//     created_at_td.className = 'py-2 px-4 border-b';
// 
//     tr_uav.appendChild(location_td);
//     tr_uav.appendChild(model_td);
//     tr_uav.appendChild(status_td);
//     tr_uav.appendChild(start_at_td);
//     tr_uav.appendChild(end_at_td);
//     tr_uav.appendChild(created_at_td);
// 
//     return tr_uav;
// }
// 
// function setUavs(uavs) {
//     let tBody = document.getElementById('tbody');
//     for (const uav of uavs) {
//         tBody.appendChild(setUav(uav));
//     }
// }
// let status_map = new Map(
//     [
//         ["accepted", "Принят"],
//         ["rejected", "Отклонен"],
//         ["finished", "Завершен"],
//         ["under_review", "В обработке"],
//     ],
// )
// fetch(
//     '/api/uav_flights',
//     {
//         method: 'GET',
//     },
// ).then(
//     (response) => {
//         response.json().then(setUavs)
//     },
// );

const dateTimeOptions = { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric', 
    hour: 'numeric', 
    minute: 'numeric' 
};

const statusMap = new Map([
    ["accepted", { text: "Одобрено", class: "bg-green-100 text-green-800" }],
    ["rejected", { text: "Отклонено", class: "bg-red-100 text-red-800" }],
    ["finished", { text: "Завершено", class: "bg-blue-100 text-blue-800" }],
    ["under_review", { text: "На рассмотрении", class: "bg-yellow-100 text-yellow-800" }]
]);

function createFlightCard(uavFlight) {
    const card = document.createElement('div');
    card.className = 'bg-white rounded-lg shadow-md overflow-hidden border border-gray-200 hover:shadow-lg transition cursor-pointer';

    card.addEventListener('click', () => {
        window.location.href = `/me/uav_flight?uav_flight_id=${uavFlight.id}`;
    });

    // Статус заявки
    const statusInfo = statusMap.get(uavFlight.status) || { text: uavFlight.status, class: "bg-gray-100 text-gray-800" };

    // Шапка карточки с названием и статусом
    const header = document.createElement('div');
    header.className = 'bg-blue-50 px-4 py-3 border-b border-gray-200';
    header.innerHTML = `
        <h3 class="font-semibold text-lg text-gray-800 truncate">${uavFlight.location}</h3>
        <span class="inline-block mt-1 px-2 py-1 text-xs font-semibold rounded-full ${statusInfo.class}">
            ${statusInfo.text}
        </span>
    `;

    // Основное содержимое карточки
    const content = document.createElement('div');
    content.className = 'p-4';

    // Форматируем даты
    const startDate = new Date(uavFlight.start_at).toLocaleString('ru-RU', dateTimeOptions);
    const endDate = new Date(uavFlight.end_at).toLocaleString('ru-RU', dateTimeOptions);
    const createdAt = new Date(uavFlight.created_at).toLocaleString('ru-RU', dateTimeOptions);

    // Получаем модель БПЛА
    fetch(`/api/uav/${uavFlight.uav_id}`, { method: 'GET' })
        .then(response => response.json())
        .then(uav => {
            content.innerHTML = `
                <div class="mb-3">
                    <p class="text-sm text-gray-500">БПЛА</p>
                    <p class="font-medium truncate">${uav.model}</p>
                </div>
                <div class="mb-3">
                    <p class="text-sm text-gray-500">Дата и время</p>
                    <p class="font-medium">${startDate} - ${endDate}</p>
                </div>
                <div>
                    <p class="text-sm text-gray-500">Создано</p>
                    <p class="font-medium">${createdAt}</p>
                </div>
            `;
        })
        .catch(() => {
            content.innerHTML = `
                <div class="mb-3">
                    <p class="text-sm text-gray-500">БПЛА</p>
                    <p class="font-medium text-gray-400">Не удалось загрузить</p>
                </div>
                <div class="mb-3">
                    <p class="text-sm text-gray-500">Дата и время</p>
                    <p class="font-medium">${startDate} - ${endDate}</p>
                </div>
                <div>
                    <p class="text-sm text-gray-500">Создано</p>
                    <p class="font-medium">${createdAt}</p>
                </div>
            `;
        });

    card.appendChild(header);
    card.appendChild(content);

    return card;
}

function renderFlights(uavFlights) {
    const container = document.getElementById('flights-container');
    container.innerHTML = '';

    uavFlights.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    uavFlights.forEach(uavFlight => {
        container.appendChild(createFlightCard(uavFlight));
    });
}

function loadFlights() {
    fetch('/api/uav_flights', { method: 'GET' })
        .then(response => response.json())
        .then(renderFlights)
        .catch(error => {
            console.error('Ошибка при загрузке заявок:', error);
        });
}

document.addEventListener('DOMContentLoaded', () => {
    loadFlights();
});