import requests
def refresh():
    burp0_url = "https://issessionsctf-defusal.chals.io:443/"
    burp0_headers = {"Connection": "close", "sec-ch-ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"", "sec-ch-ua-mobile": "?0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
    requests.get(burp0_url, headers=burp0_headers)
    
def cutwire(colour):
    burp0_url = "https://issessionsctf-defusal.chals.io:443/cut-wire"
    burp0_headers = {
        "Connection": "close",
        "sec-ch-ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://issessionsctf-defusal.chals.io",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://issessionsctf-defusal.chals.io/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    burp0_json = {"wire": colour}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    print(response.text)

def defuse():
    burp0_url = "https://issessionsctf-defusal.chals.io:443/open-case"
    burp0_headers = {
        "Connection": "close",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"",
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://issessionsctf-defusal.chals.io",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://issessionsctf-defusal.chals.io/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.post(burp0_url, headers=burp0_headers)
    print(response.text)

refresh()

# Cut wires with color names as strings
cutwire("red")
cutwire("green")
cutwire("blue")
cutwire("yellow")
cutwire("orange")
cutwire("purple")
cutwire("cyan")
cutwire("lime")

# Attempt to defuse
defuse()
