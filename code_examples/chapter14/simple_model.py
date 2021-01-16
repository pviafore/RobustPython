from pydantic.dataclasses import dataclass
from pydantic import StrictInt
@dataclass
class Model:
    value: int

Model(value="123")
Model(value=5.5)

from pydantic import StrictInt
@dataclass
class Model2:
    value: StrictInt

from pydantic import ValidationError

try:
    Model2(value="0023")
    assert False, "Model should have failed to parse"
except ValidationError:
    pass
