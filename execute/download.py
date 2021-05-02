import urllib.request
from csv import DictReader

# constants
CSV_NAME = "urls.csv"
DOWNLOAD_PATH = "./downloaded_files/file"
FORMAT_FILE = ".jpg"

with open(CSV_NAME, "r") as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row_index, row in enumerate(csv_dict_reader):
        urllib.request.urlretrieve(
            row.get("URLS"), f"{DOWNLOAD_PATH}{row_index}{FORMAT_FILE}"
        )
