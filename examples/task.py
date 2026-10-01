import os

from ucl_open_maze_runner.task import (
    UclOpenMazeRunnerTaskLogic,
    UclOpenMazeRunnerTaskParameters,
    BackgroundSubtractionParemeters
)

task_logic = UclOpenMazeRunnerTaskLogic(
    task_parameters=UclOpenMazeRunnerTaskParameters(
        initial_background_subtraction=BackgroundSubtractionParemeters(
            threshold_value=50,
            background_frames=100,
            adaptation_rate=0
        ),
        online_background_subtraction=BackgroundSubtractionParemeters(
            threshold_value=33,
            background_frames=1,
            adaptation_rate=1
        )
    )
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