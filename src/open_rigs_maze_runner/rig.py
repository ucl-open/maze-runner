from typing import Literal, Dict
from pydantic import Field

from open_rigs.core.rig import Rig
from open_rigs.video import SpinnakerCamera
from open_rigs.devices.harp import HarpBehavior
from open_rigs.devices.behavior_board import CameraTriggerController

class OpenRigsMazeRunnerRig(Rig):
    camera: SpinnakerCamera
    behavior_board: HarpBehavior
    camera_trigger_controller: CameraTriggerController