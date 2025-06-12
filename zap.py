import requests

#we are defining the zap_url and api_key below
zap_url = 'http://localhost:8082/'
api_key = ''

#scan_url = f'{zap_url}/JSON/ascan/action/scan/?apikey={api_key}&url=https://ginandjuice.shop/'
#response = requests.get(scan_url)
#print(response.text)

#alerts_url = f'{zap_url}JSON/core/view/alerts/?apikey={api_key}&baseurl=https://ginandjuice.shop/'
alerts_url = f'{zap_url}JSON/core/view/alerts/?apikey={api_key}&baseurl=https%3A%2F%2Fginandjuice.shop%2F'
response = requests.get(alerts_url)
alerts = response.json().get('alerts')
#print(alerts)
for alert in alerts:
    print(f"Alert: {alert.get('alert')}")
    print(f"Risk: {alert.get('risk')}")
    print(f"Description: {alert.get('description')}")
    print(f"Solution: {alert.get('solution')}")
    print('-' * 40)

#http://localhost:8082/JSON/core/view/alerts/?apikey=pnfcli12rkp7n28hffl1q0v75e&baseurl=https%3A%2F%2Fginandjuice.shop%2F

#alerts_url = 'http://localhost:8082/JSON/core/view/alert/?apikey=pnfcli12rkp7n28hffl1q0v75e&id=1'
#response = requests.get(alerts_url)
#alerts = response.json().get('alert')
#print(alerts)
#print(f"Alert: {alerts.get('alert')}")
#print(f"Risk: {alerts.get('risk')}")
#print(f"Description: {alerts.get('description')}")
#print(f"Solution: {alerts.get('solution')}")
#print('-' * 40)


"""import requests


import time

#we are defining the zap_url and api_key below
zap_url = 'http://localhost:8082/'
api_key = 'pnfcli12rkp7n28hffl1q0v75e'

scan_url = f'{zap_url}/JSON/ascan/action/scan/?apikey={api_key}&url=https://ginandjuice.shop/'
response = requests.get(scan_url)


alerts_url = f'{zap_url}/JSON/core/view/alerts/?apikey={api_key}&baseurl=https://ginandjuice.shop/'
response = requests.get(alerts_url)
alerts = response.json().get('alerts')


for alert in alerts:
    print(f"Alert: {alert.get('alert')}")
    print(f"Risk: {alert.get('risk')}")
    print(f"Description: {alert.get('description')}")
    print(f"Solution: {alert.get('solution')}")
    print('-' * 40)
"""
