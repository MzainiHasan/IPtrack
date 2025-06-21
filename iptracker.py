#!/usr/bin/env python3

# Author : M Zaini Hasan
# Site   : www.mzainihasan.com

import argparse
import requests

def track_ip(ip):
    url = f"http://free.ipwhois.io/json/{ip}?lang=en"
    try:
        response = requests.get(url)
        data = response.json()

        print(f"📍 IP yang dilacak : {data.get('ip', '-')}")
        print(f"🏙️ Kota            : {data.get('city', '-')}")
        print(f"🌍 Negara         : {data.get('country', '-')}")
        print(f"🏛️ Ibukota        : {data.get('country_capital', '-')}")
        print(f"🗺️ Benua          : {data.get('continent', '-')}")
        print(f"🔌 IP Type        : {data.get('type', '-')}")
        print(f"📍 Garis Lintang  : {data.get('latitude', '-')}")
        print(f"📍 Garis Bujur    : {data.get('longitude', '-')}")
        print(f"📞 Kode Telepon   : {data.get('country_phone', '-')}")
        print(f"🇨🇴 Kode Negara   : {data.get('country_code', '-')}")
    except Exception as e:
        print(f"❌ Gagal melacak IP. Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP Tracker CLI by M Zaini Hasan")
    parser.add_argument("ip", help="IP address yang ingin dilacak")
    args = parser.parse_args()
    track_ip(args.ip)
