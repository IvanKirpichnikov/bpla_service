async function getUavs() {
    let request = await fetch('/api/uavs', { method: 'GET' });
    let data = await request.json();
    let uavsArray = []
    for (const uav of data.uavs) {
        uavsArray.push(
            {
                id: uav.id,
                model: uav.model,
                serial_number: uav.serial_number,
                created_at: new Date(uav.created_at),
                noise_characteristics: uav.noise_characteristics,
                reference_number: uav.reference_number,
            },
        );
    }
    return {uavs: uavsArray};
}

function setUav(uav) {
    let trUav = document.createElement('tr');
    let modelTd = document.createElement('td');
    let serialNumberTd = document.createElement('td');
    let createdAtTd = document.createElement('td');
    let noiseCharacteristicsTd = document.createElement('td');
    let reference_number_td = document.createElement('td');

    trUav.className = 'hover:bg-gray-100';
    trUav.addEventListener('click', () => window.location.href = `/me/uav?uav_id=${uav.id}`);

    modelTd.innerHTML = uav.model;
    modelTd.className = 'py-2 px-4 border-b';

    serialNumberTd.innerHTML = uav.serial_number;
    serialNumberTd.className = 'py-2 px-4 border-b';

    noiseCharacteristicsTd.innerHTML = uav.noise_characteristics;
    noiseCharacteristicsTd.className = 'py-2 px-4 border-b';

    reference_number_td.innerHTML = uav.reference_number;
    reference_number_td.className = 'py-2 px-4 border-b';

    createdAtTd.innerHTML = uav.created_at.toLocaleString('ru-RU');
    createdAtTd.className = 'py-2 px-4 border-b';

    trUav.appendChild(modelTd);
    trUav.appendChild(serialNumberTd);
    trUav.appendChild(noiseCharacteristicsTd);
    trUav.appendChild(reference_number_td);
    trUav.appendChild(createdAtTd);

    return trUav;
}

function setUavs(uavs) {
    let tBody = document.getElementById('tbody');
    for (const uav of uavs) {
        tBody.appendChild(setUav(uav));
    }
}


var date_time_options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };

getUavs().then((uavs) => setUavs(uavs.uavs))

document.getElementById('add-uav').addEventListener('click', () => {window.location.href = '/me/uav/add'});
document.getElementById('back').addEventListener('click', () => {document.location.href = '/me'});
