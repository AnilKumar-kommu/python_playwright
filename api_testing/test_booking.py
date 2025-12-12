import json

from anyio.streams import file


def test_create_booking():
    import requests

    url = "https://restful-booker.herokuapp.com/booking"
    file=open("create_booking_payload.json", "r")
    payload=json.loads(file.read())
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["booking"]["firstname"] == "john"
    assert response_data["booking"]["lastname"] == "raj"
    assert response_data["booking"]["totalprice"] == 200
    assert response_data["booking"]["depositpaid"] is True
    assert response_data["booking"]["bookingdates"]["checkin"] == "2023-10-01"
    assert response_data["booking"]["bookingdates"]["checkout"] == "2023-10-10"
    assert response_data["booking"]["additionalneeds"] == "Breakfast"
    print("Booking created successfully with ID:", response_data)
test_create_booking()
