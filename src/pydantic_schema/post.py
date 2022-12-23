from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(le=3)
    title: str
# name: str=Field(alias="_name")
# id: int = Field(le="2")

    # @validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v>5:
    #         raise ValueError("Id is not less than two")
    #     else:
    #         return v


