import requests
import json
import sys

def fetch_json(url: str):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise

    try:
        return resp.json()
    except json.JSONDecodeError as e:
        print(f"[ERROR] Impossible de parser le JSON : {e}", file=sys.stderr)
        sys.exit(1)

def main():
    pages_url = (
        "https://m4tth1euna0p1c.github.io/"
        "Ecosystem-Digital-ilac/"
        "custom_data.json"
    )
    raw_url = (
        "https://raw.githubusercontent.com/"
        "m4tth1euna0p1c/Ecosystem-Digital-ilac/"
        "main/custom_data.json"
    )

    data = None
    for url in (pages_url, raw_url):
        try:
            data = fetch_json(url)
            print(f"✅ Chargé depuis : {url}")
            break
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                print(f"⚠️ 404 pour {url}, passage à la source suivante...", file=sys.stderr)
            else:
                print(f"[ERROR] Erreur HTTP pour {url} : {e}", file=sys.stderr)
        except Exception as e:
            print(f"[ERROR] Erreur lors de la récupération : {e}", file=sys.stderr)
            sys.exit(1)

    if data is None:
        print("[ERROR] Impossible de récupérer le JSON depuis aucune des sources.", file=sys.stderr)
        sys.exit(1)

    if not isinstance(data, list):
        print("[ERROR] Le JSON n’est pas une liste d’objets.", file=sys.stderr)
        sys.exit(1)

    for idx, item in enumerate(data, start=1):
        if idx > 1:
            print()
        print(f"=== Objet #{idx} ===")
        print(f"Nom         : {item.get('name')}")
        print(f"Description : {item.get('description')}")
        print("Spécifications :")
        specs = item.get('specifications', {})
        for key, val in specs.items():
            print(f"  - {key} : {val}")
        tags = item.get('tags', [])
        print(f"Tags        : {', '.join(tags) if tags else 'aucun'}")

if __name__ == "__main__":
    main()
