import requests

r = requests.get("http://localhost:8000/predict?text=hello")
assert r.status_code == 200
