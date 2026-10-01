# Import core types
from typing import Literal
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

from ucl_open_maze_runner import __semver__

# TODO - should inherit from some TaskParameters base class rather than BaseSchema
class UclOpenMazeRunnerTaskParameters(BaseSchema):
    ...


class UclOpenMazeRunnerTaskLogic(BaseSchema):
    version: Literal[__semver__] = __semver__
    name: Literal["UclOpenMazeRunner"] = Field(default="UclOpenMazeRunner", description="Name of the task logic", frozen=True)
    task_parameters: UclOpenMazeRunnerTaskParameters = Field(description="Parameters of the task logic")
    ...