import os

from ucl_open_maze_runner.rig import (
    UclOpenMazeRunnerRig
)
from ucl_open.video import SpinnakerCamera
from ucl_open.devices.harp import HarpBehavior
from ucl_open.devices.behavior_board import CameraTriggerController

rig = UclOpenMazeRunnerRig(
    root_path="C:/temp_data",
    camera=SpinnakerCamera(
        serial_number="18474551",# Track 1 24166055, Track 2 17458434, SleepPot 18474551
        exposure_time=15000,
        gain=10
    ),
    behavior_board=HarpBehavior(port_name="COM9"),
    camera_trigger_controller=CameraTriggerController(
        trigger0_frequency=60,
        trigger1_frequency=60
    )
)

def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [rig]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()