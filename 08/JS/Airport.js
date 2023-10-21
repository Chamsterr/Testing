const PassengerPlane = require('./Planes/PassengerPlane');
const MilitaryPlane = require('./Planes/MilitaryPlane');
const MilitaryType = require('./models/MilitaryType');
const ExperimentalPlane = require('./Planes/ExperimentalPlane');

class Airport {
    constructor(planes) {
        this.planes = planes;
    }

    getPlanesByType(type) {
        return this.planes.filter(plane => plane instanceof type);
    }

    getMilitaryPlanes() {
        return this.getPlanesByType(MilitaryPlane);
    }

    getPassengerPlanes() {
        return this.getPlanesByType(PassengerPlane);
    }

    getExperimentalPlanes() {
        return this.getPlanesByType(ExperimentalPlane);
    }

    getMilitaryPlanesByType(militaryType) {
        return this.getMilitaryPlanes().filter(plane => plane.getMilitaryType() === militaryType);
    }

    getTransportMilitaryPlanes() {
        return this.getMilitaryPlanesByType(MilitaryType.TYPE_TRANSPORT);
    }

    getBomberMilitaryPlanes() {
        return this.getMilitaryPlanesByType(MilitaryType.BOMBER);
    }

    getPassengerPlaneWithMaxPassengersCapacity() {
        return this.getPassengerPlanes().reduce((maxPlane, plane) => 
            plane.getPassengersCapacity() > maxPlane.getPassengersCapacity() ? plane : maxPlane
        );
    }

    sortByMaxDistance() {
        this.planes.sort((a, b) => a.getMaxFlightDistance() - b.getMaxFlightDistance());
        return this;
    }

    sortByMaxSpeed() {
        this.planes.sort((a, b) => a.getMaxSpeed() - b.getMaxSpeed());
        return this;
    }

    sortByMaxLoadCapacity() {
        this.planes.sort((a, b) => a.getMinLoadCapacity() - b.getMinLoadCapacity());
        return this;
    }

    static print(planes) {
        return JSON.stringify(planes);
    }
}

module.exports = Airport;