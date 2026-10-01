from typing import Literal, Dict
from pydantic import Field

from ucl_open.core.rig import Rig

from ucl_open_maze_runner import __semver__


class UclOpenMazeRunnerRig(Rig):
    version: Literal[__semver__] = __semver__
    ...