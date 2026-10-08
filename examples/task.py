import os

from open_rigs_maze_runner.task import (
    OpenRigsMazeRunnerTaskLogic,
    OpenRigsMazeRunnerTaskParameters,
    RewardZone
)
from open_rigs.core import Vector2

task_logic = OpenRigsMazeRunnerTaskLogic(
    task_parameters=OpenRigsMazeRunnerTaskParameters(
        reward_sequence=[
            RewardZone(
                region=[Vector2(x=44, y=193), Vector2(x=129, y=193), Vector2(x=129, y=279), Vector2(x=44, y=279)],
                reward_command="l100"
            ),
            RewardZone(
                region=[Vector2(x=541, y=201), Vector2(x=608, y=201), Vector2(x=608, y=287), Vector2(x=541, y=287)],
                reward_command="r100"
            )
        ]
    ),
)

def main(path_seed: str = "./local/{schema}.json"):
    example_task_logic = task_logic
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [example_task_logic]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()