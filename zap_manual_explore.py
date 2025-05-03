import requests
import time

#we are defining the zap_url and api_key below
zap_url = 'http://localhost:8082/'
api_key = 'pnfcli12rkp7n28hffl1q0v75e'

alerts_url = f'{zap_url}JSON/spider/action/scan/?apikey={api_key}&url=https%3A%2F%2Fginandjuice.shop%2F'
response = requests.get(alerts_url)
data = response.json()
scanId = response.json().get('scan')

scan_progress = f'{zap_url}JSON/spider/view/status/?apikey={api_key}&scanId={scanId}'
response = requests.get(scan_progress)
status = response.json().get('status')

"""while status!=100:
   response = requests.get(scan_progress)
   status = response.json().get('status')
   time.sleep(10)"""


while True:
   response = requests.get(scan_progress)
   status = response.json().get('status')
   print(f"Scan status: {status}")
   if status == "100":
      break
print("Scan finished")


manual_explore_results = f'{zap_url}JSON/spider/view/results/?apikey={api_key}&scanId={scanId}'
response = requests.get(manual_explore_results)
data = response.json()


for url in data["results"]:
   print(url)
