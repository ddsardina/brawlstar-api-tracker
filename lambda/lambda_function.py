import urllib3
privateIP = "192.168.1.1"

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    r = http.request('POST', f'http://{privateIP}:5000/api/battles/PCURU80V')
    print(r.status)
    return r.status
