#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


import requests

if __name__ == "__main__":
   p = requests.get("https://alx-intranet.hbtn.io/status")
   print("Body response:")
   print("\t- type: {}".format(type(p.text)))
   print("\t- content: {}".format(p.text))
