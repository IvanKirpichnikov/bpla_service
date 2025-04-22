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

    const statusInfo = statusMap.get(uavFlight.status) || { text: uavFlight.status, class: "bg-gray-100 text-gray-800" };

    const header = document.createElement('div');
    header.className = 'bg-blue-50 px-4 py-3 border-b border-gray-200';
    header.innerHTML = `
        <h3 class="font-semibold text-lg text-gray-800 truncate">${uavFlight.location}</h3>
        <span class="inline-block mt-1 px-2 py-1 text-xs font-semibold rounded-full ${statusInfo.class}">
            ${statusInfo.text}
        </span>
    `;

    const content = document.createElement('div');
    content.className = 'p-4';

    const startDate = new Date(uavFlight.start_at).toLocaleString('ru-RU', dateTimeOptions);
    const endDate = new Date(uavFlight.end_at).toLocaleString('ru-RU', dateTimeOptions);
    const createdAt = new Date(uavFlight.created_at).toLocaleString('ru-RU', dateTimeOptions);

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
    container.textContent = '';

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