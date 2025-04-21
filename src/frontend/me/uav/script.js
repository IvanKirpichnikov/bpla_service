function setUav(uav) {
    let model = document.getElementById('model');
    let serialNumber = document.getElementById('serial_number');
    let createdAt = document.getElementById('created_at');
    let noiseCharacteristics = document.getElementById('noise_characteristics');
    let reference_number = document.getElementById('reference_number');

    model.innerHTML = uav.model;
    model.className = model.className.replace(' animate-pulse', '');

    serialNumber.innerHTML = uav.serial_number;
    serialNumber.className = serialNumber.className.replace(' animate-pulse', '');

    createdAt.innerHTML = (new Date(uav.created_at)).toLocaleString('ru-RU', date_time_options);
    createdAt.className = createdAt.className.replace(' animate-pulse', '');

    noiseCharacteristics.innerHTML = uav.noise_characteristics;
    noiseCharacteristics.className = noiseCharacteristics.className.replace(' animate-pulse', '');

    reference_number.innerHTML = uav.reference_number;
    reference_number.className = reference_number.className.replace(' animate-pulse', '');
}

var date_time_options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
const urlParams = new URLSearchParams(window.location.search);
const uavId = urlParams.get('uav_id');
if (uavId == null) {
    document.location.href = '/me/uavs';
};

fetch(`/api/uav/${uavId}`, { method: 'GET' }).then(response => response.json()).then(setUav);

document.getElementById('back').addEventListener('click', () => {document.location.href = '/me/uavs'});
