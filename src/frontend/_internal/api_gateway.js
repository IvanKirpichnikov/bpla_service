import { Me } from './types/me.js';
import { Uav } from './types/uav.js';

export class ApiGateway {
    async _send_request(
        url,
        method,
        body = null,
        headers = {},
    ) {
        let data = {
            method: method,
            headers: headers,
        }

        if (body) {
            data.body = JSON.stringify(body);
        }

        let response = await fetch(url, data)

        if (response.redirected) {
            window.location.href = response.url;
        }
        return await response.json();
    }
    async get_me() {

    }

    async get_uav(uavId) {
        let data = await this._send_request(
            `/api/uav/${uavId}`,
            'GET',
            {},
            {'Content-Type': 'application/json'},
        );
        return new Uav(
            data.id,
            data.model,
            data.serial_number,
            new Date(data.created_at),
            data.noise_characteristics,
            data.number_of_electric_motors
        );
    }

    async add_uav_flight(uav_flight) {
        let data = await this._send_request(
            `/api/uav_flight`,
            'POST',
            uav,
            {'Content-Type': 'application/json'},
        );
        return new Uav(
            data.id,
            data.model,
            data.serial_number,
            new Date(data.created_at),
            data.noise_characteristics,
            data.number_of_electric_motors
        );
    }

    async get_uavs() {
        let uavs = await this._send_request(
            `/api/uavs`,
            'GET',
            null,
            {'Content-Type': 'application/json'},
        );
        let data = []
        for (const uav of uavs.uavs) {
            data.push(
                new Uav(
                    uav.id,
                    uav.model,
                    uav.serial_number,
                    new Date(uav.created_at),
                    uav.noise_characteristics,
                    uav.number_of_electric_motors
                )
            );
        }
        return data;
    }


}
