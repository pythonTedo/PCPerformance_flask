import requests
DEF_URL = "http://localhost:5000"

def test_home():
    resp = requests.get(f"{DEF_URL}/")

    assert resp.status_code == 200

    print(resp.text)

    assert "Python" in resp.text


def test_info():
    resp = requests.get(f"{DEF_URL}/info")

    assert resp.status_code == 200
    assert "Hostname" in resp.text
    

def test_page_content():
    resp = requests.get(f"{DEF_URL}/")

    assert resp.status_code == 200
    assert "Coleman" in resp.text