from typing import Literal, Dict
from pydantic import Field

from open_rigs.core.rig import Rig
from open_rigs.video import SpinnakerCamera
from open_rigs.devices.harp import HarpBehavior
from open_rigs.devices.behavior_board import CameraTriggerController
from open_rigs.core.base import BaseSchema

class BackgroundSubtractionParemeters(BaseSchema):
    threshold_value: float
    background_frames: int
    adaptation_rate: float

class FindContoursParameters(BaseSchema):
    min_area: float

class OpenRigsMazeRunnerRig(Rig):
    camera: SpinnakerCamera
    behavior_board: HarpBehavior
    camera_trigger_controller: CameraTriggerController
    initial_background_subtraction: BackgroundSubtractionParemeters
    online_background_subtraction: BackgroundSubtractionParemeters
    animal_contour_parameters: FindContoursParameters