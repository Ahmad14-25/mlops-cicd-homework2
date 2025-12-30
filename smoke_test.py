import time
import requests

time.sleep(5)  # wait for the service to be ready

r = requests.get("http://localhost:8000/predict?text=hello")

assert r.status_code == 200
print("Smoke test passed")
