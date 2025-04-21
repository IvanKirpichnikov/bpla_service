var date_time_options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };

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
    let main_div = document.createElement('div');
    main_div.className = "bg-white rounded-lg shadow-md overflow-hidden border border-gray-200";
    main_div.addEventListener('click', () => window.location.href = `/me/uav?uav_id=${uav.id}`);

    let name_div = document.createElement('div');
    name_div.className = "bg-blue-50 px-4 py-3 border-b border-gray-200";

    let name_h3 = document.createElement('h3');
    name_h3.className = "font-semibold text-lg text-gray-800";
    name_h3.innerHTML = uav.model;

    name_div.appendChild(name_h3);
    main_div.appendChild(name_div);

    let characteristics_div = document.createElement('div');
    characteristics_div.className = "p-4";

    let serial_number_div = document.createElement('div')
    serial_number_div.className = "mb-3";

    let serial_number_title_p = document.createElement('p');
    serial_number_title_p.className = "text-sm text-gray-500";
    serial_number_title_p.innerHTML = "Серийный номер";

    let serial_number_value_p = document.createElement('p');
    serial_number_value_p.className = "font-medium";
    serial_number_value_p.innerHTML = uav.serial_number;

    serial_number_div.appendChild(serial_number_title_p);
    serial_number_div.appendChild(serial_number_value_p);
    characteristics_div.appendChild(serial_number_div);

    let noise_characteristics_div = document.createElement('div')
    noise_characteristics_div.className = "mb-3";

    let noise_characteristics_title_p = document.createElement('p');
    noise_characteristics_title_p.className = "text-sm text-gray-500";
    noise_characteristics_title_p.innerHTML = "Шумовые характеристики";

    let noise_characteristics_value_p = document.createElement('p');
    noise_characteristics_value_p.className = "font-medium";
    noise_characteristics_value_p.innerHTML = uav.noise_characteristics + " Гц.";

    noise_characteristics_div.appendChild(noise_characteristics_title_p);
    noise_characteristics_div.appendChild(noise_characteristics_value_p);
    characteristics_div.appendChild(noise_characteristics_div);

    let reference_number_div = document.createElement('div')
    reference_number_div.className = "mb-3";

    let reference_number_title_p = document.createElement('p');
    reference_number_title_p.className = "text-sm text-gray-500";
    reference_number_title_p.innerHTML = "Учетный номер";

    let reference_number_value_p = document.createElement('p');
    reference_number_value_p.className = "font-medium";
    reference_number_value_p.innerHTML = uav.reference_number;

    reference_number_div.appendChild(reference_number_title_p);
    reference_number_div.appendChild(reference_number_value_p);
    characteristics_div.appendChild(reference_number_div);

    let created_at_div = document.createElement('div')
    created_at_div.className = "mb-3";

    let created_at_title_p = document.createElement('p');
    created_at_title_p.className = "text-sm text-gray-500";
    created_at_title_p.innerHTML = "Дата добавления";

    let created_at_value_p = document.createElement('p');
    created_at_value_p.className = "font-medium";
    created_at_value_p.innerHTML = uav.created_at.toLocaleString('ru-RU');

    created_at_div.appendChild(created_at_title_p);
    created_at_div.appendChild(created_at_value_p);
    characteristics_div.appendChild(created_at_div);

    main_div.appendChild(characteristics_div);

    return main_div;
}

function setUavs(uavs) {
    let tBody = document.getElementById('uavs');
    for (const uav of uavs) {
        tBody.appendChild(setUav(uav));
    }
}

getUavs().then((uavs) => setUavs(uavs.uavs))

document.getElementById('add-uav').addEventListener('click', () => {window.location.href = '/me/uav/add'});
