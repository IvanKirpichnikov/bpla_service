export class Me {
    constructor(id, fio, email, created_at) {
        this._id = id;
        this._fio = fio;
        this._email = email;
        this._created_at = created_at;
    }

    get id() {
        return this._id;
    }

    get fio() {
        return this._fio;
    }

    get email() {
        return this._email;
    }

    get created_at() {
        return this._created_at;
    }
}
