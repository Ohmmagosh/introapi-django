from ninja import Router, Form
from django.shortcuts import Http404, get_object_or_404
from introapi.schemas import (
    Detail,
    UserGetOut,
    UserPostIn,
    UserDeleteIn
)
from introapi.models import (
    User
)


router = Router(tags=["IntroAPI"])


@router.get("hello")
def hello(request):
    return {"message": "Hello World"}


@router.get("users/",
            response={200: dict, 400: Detail},
            tags=["GET"])
def get_users(request):
    try:
        users = User.objects.all()
        return 200, {
            'model': [UserGetOut.from_orm(user) for user in users]
            }
    except Http404:
        return 400, {
            "message": "Oops, no users found"
            }

@router.post('user/create/',
             tags=["POST"],
             response={200: dict})
def create_user(request, payload: UserPostIn=Form(...)):
    user = User.objects.create(
        intra_id=payload.intra_id,
        favorite_language=payload.favorite_language,
        favorite_food=payload.favorite_food,
        favorite_color=payload.favorite_color
    )
    return 200, {
        'message': 'User created',
        'model': UserGetOut.from_orm(user)
    }


@router.delete('user/delete/',
               tags=["DELETE"],
               response={200: Detail, 404: Detail})
def delete_user(request, payload: UserDeleteIn):
    try:
        user = get_object_or_404(User, id = payload.id)
        user.delete()
        return 200 , {
            'message': f'User {payload.id} Delete'
        }
    except Http404:
        return 404 , {
            'message': f'User {payload.id} not found'
        }


