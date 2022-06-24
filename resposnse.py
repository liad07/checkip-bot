import urllib.request, json

def sample_res(ip):
    f = open("iplist.txt", "a")
    f.write(ip + "\n")
    f.close()
    url1 = "https://geolocation-db.com/json/" + ip
    with urllib.request.urlopen(url1) as url:
        data = json.loads(url.read().decode())
    x = str(data)
    x = x.replace("{", "")
    x = x.replace("}", "")
    x = x.replace("'", "")
    x = x.split(",")
    d = ""
    latitude = x[4]
    longitude = x[5]
    latitude = latitude.replace("latitude:", "")
    longitude = longitude.replace("longitude:", "")
    latitude = latitude.lstrip()
    longitude = longitude.lstrip()
    maplink = "https://www.google.com/maps/search/" + latitude + "," + longitude + "/"
    for i in range(len(x)):
        d += x[i] + "\n"
    d += maplink
    f = open("iplist.json", "a")
    f.write(str(data) + "\n")
    f.close()
    return d