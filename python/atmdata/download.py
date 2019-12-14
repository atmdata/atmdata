import io

import pandas as pd
import requests
from tqdm import tqdm

_session = requests.Session()


def get_data(file_url: str) -> io.BytesIO:
    f = _session.get(file_url, stream=True)
    total = int(f.headers["Content-Length"])
    print(total)
    buffer = io.BytesIO()
    for chunk in tqdm(
        f.iter_content(1024),
        total=total // 1024 + 1 if total % 1024 > 0 else 0,
        desc="download",
    ):
        buffer.write(chunk)

    buffer.seek(0)
    return buffer


if __name__ == "__main__":
    b = get_data(
        "https://opensky-network.org/datasets/publication-data/climbing-aircraft-dataset/anonym/B737/test_fromICAO.csv")
    print(pd.read_csv(b))
