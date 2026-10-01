import datetime
import os

from ucl_open.core.experiment import ExperimentSession

# TODO - autofill experiment fields
session = ExperimentSession(
    repository_url="https://github.com/ucl-open/maze-runner",
    commit="",
    workflow="main.bonsai",
    session_id="0_0_Track1RUN1",
    subject_id="M26021"
)

def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [session]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()