from fastapi import APIRouter, Depends
from app.auth.jwt import get_current_jwt_payload
from app.dto.common import JWTPayloadDto
from app.dto.users import UserAuthResultDto, UserRegisterDto, UserCredentialDto
from app.schemae.users import UserInfoModel
from app.services.users import UserService

router = APIRouter(
  prefix="/user",
  tags=["User Profiles"],
  dependencies=[],
  responses={404: {"description": "Not found"}},
)

user_svc = UserService()

@router.post("/register", response_model=UserInfoModel)
def register(dto: UserRegisterDto):
  return user_svc.register(dto)

@router.post("/login", response_model=UserAuthResultDto)
def login(dto: UserCredentialDto):
  return user_svc.login(dto)

@router.get("/me", response_model=JWTPayloadDto)
def me(user: JWTPayloadDto = Depends(get_current_jwt_payload)):
  return user
