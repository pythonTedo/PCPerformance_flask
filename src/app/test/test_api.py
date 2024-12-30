import json
import requests 

DEF_URL = "http://localhost:5000"

def test_api_process():
    resp = requests.get(f"{DEF_URL}/api/process")
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    

    resp_payload = resp.json()
    assert len(resp_payload["processes"]) > 0
    assert resp_payload["processes"][0]["memory_percent"] > 0

def test_api_monitor():
    resp = requests.get(f"{DEF_URL}/api/monitor")

    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

    resp_payload = resp.json()
    assert "cpu" in resp_payload and isinstance(resp_payload["cpu"], float)
    assert "mem" in resp_payload and isinstance(resp_payload["mem"], float)
    assert "disk" in resp_payload and isinstance(resp_payload["disk"], float)
    assert "net_send" in resp_payload and isinstance(resp_payload["net_send"], int)
    assert "net_recv" in resp_payload and isinstance(resp_payload["net_recv"], int)
    assert "disk_write" in resp_payload and isinstance(resp_payload["disk_write"], int)
    assert "disk_read" in resp_payload and isinstance(resp_payload["disk_read"], int)


