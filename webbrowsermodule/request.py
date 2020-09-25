import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code
len(res.text)
print (res.text)
res.raise_for_status()
playfile = open('romeoandjuliet.txt', 'wb')
for chunk in res.iter_content():
    playfile.write(chunk)
playfile.close()