import json


def test_create_job(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "TestHoo",
        "company_url": "https://www.testhoo.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-20"
    }

    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200