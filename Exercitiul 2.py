import os, requests

url = 'http://localhost:5000/list'

# response = requests.get(url)
# print(response.text)

number = {'key': 6}

myobj = {
    'key': 7613,
    'name': 'Andreas',
    'pass': 'C6@2h'
    }

x = requests.post(url, data = number)

print(x.text)

# exercitiu = input('Ce exercitiu sa fie rezolvat? 1 sau 2 \n')
# os.system(f'curl http://127.0.0.1:5000/{exercitiu}')
