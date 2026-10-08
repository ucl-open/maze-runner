import os

from open_rigs_maze_runner.rig import (
    OpenRigsMazeRunnerRig,
    BackgroundSubtractionParemeters,
    FindContoursParameters
)
from open_rigs.video import SpinnakerCamera
from open_rigs.devices.harp import HarpBehavior
from open_rigs.devices.behavior_board import CameraTriggerController

rig = OpenRigsMazeRunnerRig(
    root_path="../temp_data",
    camera=SpinnakerCamera(serial_number="12345678"),
    behavior_board=HarpBehavior(port_name="COM3"),
    camera_trigger_controller=CameraTriggerController(trigger0_frequency=60, trigger1_frequency=60),
    initial_background_subtraction=BackgroundSubtractionParemeters(
        threshold_value=100,
        background_frames=100,
        adaptation_rate=0
    ),
    online_background_subtraction=BackgroundSubtractionParemeters(
        threshold_value=33,
        background_frames=1,
        adaptation_rate=1
    ),
    animal_contour_parameters=FindContoursParameters(
        min_area=300
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