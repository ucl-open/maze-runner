# Import core types
from typing import Literal, List
from pydantic import Field

from open_rigs.core.task import Task, TaskParameters
from open_rigs.core import Vector2
from open_rigs.core.base import BaseSchema

class RewardZone(BaseSchema):
    region: List[Vector2]
    reward_command: str


class OpenRigsMazeRunnerTaskParameters(TaskParameters):
    reward_sequence: List[RewardZone]


class OpenRigsMazeRunnerTaskLogic(Task):
    task_parameters: OpenRigsMazeRunnerTaskParameters