from pydantic import BaseModel,ValidationError


class Model(BaseModel):
      v:str

      class Config:
            fields={}
