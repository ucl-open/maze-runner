# Import core types
from typing import Literal
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

class BackgroundSubtractionParemeters(BaseSchema):
    threshold_value: float
    background_frames: int
    adaptation_rate: float

class OpenRigsMazeRunnerTaskParameters(BaseSchema):
    initial_background_subtraction: BackgroundSubtractionParemeters
    online_background_subtraction: BackgroundSubtractionParemeters


class OpenRigsMazeRunnerTaskLogic(BaseSchema):
    name: Literal["OpenRigsMazeRunner"] = Field(default="OpenRigsMazeRunner", description="Name of the task logic", frozen=True)
    task_parameters: OpenRigsMazeRunnerTaskParameters = Field(description="Parameters of the task logic")