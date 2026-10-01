from typing import Literal, Dict
from pydantic import Field

from ucl_open.core.rig import Rig
from ucl_open.video import SpinnakerCamera
from ucl_open.devices.harp import HarpBehavior
from ucl_open.devices.behavior_board import CameraTriggerController
from ucl_open.devices import SerialDevice

from ucl_open_maze_runner import __semver__


class UclOpenMazeRunnerRig(Rig):
    version: Literal[__semver__] = __semver__
    camera: SpinnakerCamera
    behavior_board: HarpBehavior
    camera_trigger_controller: CameraTriggerController
    # arduino: SerialDevice