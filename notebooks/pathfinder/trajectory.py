import subprocess
import json
import os

# this runs Pathfinder 1 from https://github.com/jhh/motion

def build(toml_str, trajectory_name):
    process = subprocess.run(
    "MOTION_OPTS=-Djava.library.path={0}/lib {0}/bin/motion '{1}'".format(
        "../../pathfinder/build/install/motion",
        json.dumps({"pathfinder": {"toml": toml_str}})),
    shell=True)
    os.rename("data/trajectory.csv", "data/%s.csv" % trajectory_name)

