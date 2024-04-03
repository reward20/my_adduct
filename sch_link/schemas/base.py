from pydantic import BaseModel, ConfigDict

__all__ = [
    "Schema"
]


class Schema(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        ser_json_timedelta="float",
        allow_inf_nan=False,
    )
