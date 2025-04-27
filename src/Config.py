from pathlib import Path

# Base path = lokasi file Python ini
BASE_DIR = Path(__file__).resolve().parent

# Gabungkan path
pathDataUser = BASE_DIR / "../data/PersonDB.json"
pathDataItem = BASE_DIR / "../data/items.json"

# Resolve supaya path ../ nya dibereskan
pathDataUser = pathDataUser.resolve()
pathDataItem = pathDataItem.resolve()

