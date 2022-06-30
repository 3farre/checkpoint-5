import requests

r = requests.get('http://127.0.0.1:5000/api')

def get_phone(name):
  name = requests.get('http://127.0.0.1:5000/api?action=phone&name=Urban')
  return name.text

def get_name(phone):
  phone = requests.get('http://127.0.0.1:5000/api?action=name&phone=0435-4355438')
  return phone.text


   