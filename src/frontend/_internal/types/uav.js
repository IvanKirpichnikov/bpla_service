export class Uav {
    constructor(
        id,
        model,
        serial_number,
        created_at,
        noise_characteristics,
        number_of_electric_motors,
    ) {
        this._id = id;
        this._model = model;
        this._serial_number = serial_number;
        this._created_at = created_at;
        this._noise_characteristics = noise_characteristics;
        this._number_of_electric_motors = number_of_electric_motors;
    }

    get id() {
        return this._id;
    }

    get model() {
        return this._model;
    }

    get serial_number() {
        return this._serial_number;
    }

    get created_at() {
        return this._created_at;
    }
}
