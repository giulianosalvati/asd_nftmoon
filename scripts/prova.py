import urllib.request 
import json

# content ID
cid = "bafkreiak2t5rgyeqmjytkuhfipwrm32qnjmorps52o6vlsd3rs5oci67pa"

# read .json
with urllib.request.urlopen(f"https://dweb.link/ipfs/{cid}") as url:
    data = json.loads(url.read())
    print(data['value'])
