import json
from pathlib import Path


def save_json(
    path: str | Path,
    data: dict,
):

    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


def load_json(
    path: str | Path,
):

    path = Path(path)

    if not path.exists():

        raise FileNotFoundError(
            f"{path} not found."
        )

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def save_model(
    path: str | Path,
    model,
):

    save_json(
        path,
        model.model_dump(),
    )


def load_model(
    path: str | Path,
    model_class,
):

    data = load_json(path)

    return model_class(
        **data,
    )