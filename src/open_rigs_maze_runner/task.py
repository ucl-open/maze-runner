# Import core types
from typing import Literal
from pydantic import Field

from open_rigs.core.task import Task, TaskParameters

class OpenRigsMazeRunnerTaskParameters(TaskParameters):
    ...


class OpenRigsMazeRunnerTaskLogic(Task):
    ...