def abs_path_from_project(relative_path: str):
    import model
    from pathlib import Path

    return (
        Path(model.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
