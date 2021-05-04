from copyreg import pickle
from mimetypes import init
import pandas as pd
import requests
from datetime import datetime
import pytz
from pathlib import Path
import pickle


class Action:
    def __init__(self, url: str) -> None:
        r = requests.get(url)
        action = r.json()

        df = pd.DataFrame(action["traces"], columns=["millis", "measure", "value"])
        df = df.drop_duplicates(subset=["millis", "measure"], keep="last")
        self.dataframe = df.pivot(index="millis", columns="measure", values="value")

        self.id = action["id"]
        self.name = action["name"]
        self.meta = action["meta"]
        self.description = action["meta"]["description"]
        self.version = action["meta"]["version"]
        self.created_at = datetime.strptime(
            action["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z"
        ).astimezone(pytz.timezone("US/Eastern"))

    def created_at_str(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M")

    def dump(self):
        basename = self.created_at.strftime("%Y-%m-%d-%H-%M")
        file = f"{basename}.pickle"
        path = Path("data") / file
        with path.open("wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
