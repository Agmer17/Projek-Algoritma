from pathlib import Path

# Base path = lokasi file Python ini
BASE_DIR = Path(__file__).resolve().parent

# Gabungkan path
dataUser = BASE_DIR / "../data/PersonDB.json"
dataItem = BASE_DIR / "../data/items.json"

# Resolve supaya path ../ nya dibereskan
dataUser = dataUser.resolve()
dataItem = dataItem.resolve()

