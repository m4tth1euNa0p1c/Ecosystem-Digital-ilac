import requests
import sys

def fetch_json(url: str):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"[ERROR] Impossible de récupérer les données : {e}", file=sys.stderr)
        sys.exit(1)

def parse_and_display(data):

    for idx, item in enumerate(data, 1):
        print(f"\n=== Objet #{idx} ===")
        print(f"Nom         : {item.get('name')}")
        print(f"Description : {item.get('description')}")
        specs = item.get('specifications', {})
        print("Spécifications :")
        for key, val in specs.items():
            print(f"  - {key} : {val}")
        tags = item.get('tags', [])
        print(f"Tags        : {', '.join(tags)}")

def main():
    url = "https://github.com/m4tth1euNa0p1c/Ecosystem-Digital-ilac/custom_data.json"
    data = fetch_json(url)
    parse_and_display(data)

if __name__ == "__main__":
    main()
