from mimetypes import init
import pandas as pd
import requests
from datetime import datetime
import pytz


class Action:
    def __init__(self, url: str) -> None:
        r = requests.get(url)
        action = r.json()

        df = pd.DataFrame(action["traces"], columns=["millis", "measure", "value"])
        df = df.drop_duplicates(subset=["millis", "measure"], keep="last")
        self.dataframe = df.pivot(index="millis", columns="measure", values="value")

        self.name = action["name"]
        self.description = action["meta"]["description"]
        self.created_at = (
            datetime.strptime(action["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
            .astimezone(pytz.timezone("US/Eastern"))
            .strftime("%Y-%m-%d %H:%M")
        )
