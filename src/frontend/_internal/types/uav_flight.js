class UavFlight {
    constructor(
        id,
        uav_id,
        uav_model,
        location,
        start_at,
        end_at,
        created_at,
    ) {
        this._id = id;
        this._uav_id = uav_id;
        this._uav_model = uav_model;
        this._location = location;
        this._start_at = start_at;
        this._end_at = end_at;
        this._created_at = created_at;
    }

    get id() {
        return this._id;
    }
    get uav_id() {
        return this._uav_id;
    }
    get uav_model() {
        return this._uav_model;
    }
    get location() {
        return this._location;
    }
    get start_at() {
        return this._start_at;
    }
    get end_at() {
        return this._end_at;
    }
    get created_at() {
        return this._created_at;
    }
}
