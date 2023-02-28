from ninja import Schema, ModelSchema
from introapi.models import User


class Detail(Schema):
    message: str


class ModelGetOut(Schema):
    message: str
    model: ModelSchema


class UserGetOut(ModelSchema):
    class Config:
        model = User
        model_fields = '__all__'


class UserPostIn(ModelSchema):
    class Config:
        model = User
        model_fields = ['intra_id', 'favorite_language',
                        'favorite_food', 'favorite_color']


class UserDeleteIn(ModelSchema):
    class Config:
        model = User
        model_fields = ['id']
