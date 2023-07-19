# This code snippet found at https://beepb00p.xyz/mypy-error-handling.html
from typing import Optional, TypeVar

from src.app import app

X = TypeVar("X")


def unwrap(x: Optional[X]) -> X:
    """Cast an Optional[X] to an X by asserting it's not None"""
    # similar to https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap
    assert x is not None
    return x


@app.template_filter()
def json(q, default=None):  # type: ignore
    import json

    return json.dumps(q)


@app.template_filter()
def pydantic_model_dump(model):  # type: ignore
    return model.model_dump_json()
