# Import core types
from typing import Literal
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

from ucl_open_maze_runner import __semver__

class BackgroundSubtractionParemeters(BaseSchema):
    threshold_value: float
    background_frames: int
    adaptation_rate: float

class UclOpenMazeRunnerTaskParameters(BaseSchema):
    initial_background_subtraction: BackgroundSubtractionParemeters
    online_background_subtraction: BackgroundSubtractionParemeters


class UclOpenMazeRunnerTaskLogic(BaseSchema):
    version: Literal[__semver__] = __semver__
    name: Literal["UclOpenMazeRunner"] = Field(default="UclOpenMazeRunner", description="Name of the task logic", frozen=True)
    task_parameters: UclOpenMazeRunnerTaskParameters = Field(description="Parameters of the task logic")