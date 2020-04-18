import requests
import zipfile


class Covid:

    def __init__(self):
        _URL = "http://187.191.75.115/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
        _PATH = "covid.zip"
        self.download_url(_URL, _PATH)
        self.from_zip(_PATH)

    def download_url(self, url, save_path, chunk_size=128):
        r = requests.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def from_zip(self, _PATH):
        with zipfile.ZipFile(_PATH, "r") as zip_ref:
            zip_ref.extractall("excel")
