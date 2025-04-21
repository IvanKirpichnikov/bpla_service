function _nullIfEmptyString(value) {
    if (value === '') {
        return null;
    }
    return value;
}

function getModel() {
    return _nullIfEmptyString(document.getElementById('model').value);
}

function getSerialNumber() {
    return _nullIfEmptyString(document.getElementById('serial_number').value);
}

function getNoiseCharacteristics() {
    return _nullIfEmptyString(document.getElementById('noise_characteristics').value);
}

function get_reference_number() {
    return _nullIfEmptyString(document.getElementById('reference_number').value);
}

function getFormData() {
    let model = getModel();
    let serialNumber = getSerialNumber();
    let noiseCharacteristics = getNoiseCharacteristics();
    let reference_number = get_reference_number();

    let dataArray = [model, serialNumber, noiseCharacteristics, reference_number];
    if (dataArray.includes(null)) {
        return null;
    }

    return {
        model: model,
        serial_number: serialNumber,
        noise_characteristics: noiseCharacteristics,
        reference_number: reference_number,
    }
}

async function addUav() {
    let formData = getFormData();
    if (formData === null) {
        alert('Заполни все данные');
        return null;
    }
    let request = await fetch('/api/uav', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });
    alert('БПЛА успешно добавлен');
    window.location = "/me/uavs";
}

function onStartup() {
    document.getElementById('add').addEventListener('click', addUav);
}

onStartup();
