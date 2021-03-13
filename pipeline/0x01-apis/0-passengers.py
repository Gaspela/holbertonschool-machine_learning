#!/usr/bin/env python3
"""
Can I join?
"""
import requests as rq


def availableShips(passengerCount):
    """
    Number of passengers
    List of ships
    """
    vehicles = []
    page = 1
    state = True

    while state:
        url = "https://swapi-api.hbtn.io/api/starships/?page=" + str(page)
        r = rq.get(url)
        data = r.json()
        results = data['results']
        for vehicle in results:
            passenger = vehicle['passengers']
            passenger = passenger.replace(',', "")
            if passenger.isnumeric() and int(passenger) >= passengerCount:
                vehicles.append(vehicle['name'])
        if data['next'] is None:
            state = False
        page += 1

    return (vehicles)
