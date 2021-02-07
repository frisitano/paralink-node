from jsonschema import Draft7Validator
from sanic.exceptions import InvalidUsage
from sanic_jwt.exceptions import AuthenticationFailed

from src.models import User


def validate_request(request: dict, schema: dict) -> None:
    errors = [error for error in Draft7Validator(schema).iter_errors(request)]
    if errors:
        message = "\n".join(
            [
                (".".join(error.path) + " - " if error.path else "") + error.message
                for error in errors
            ]
        )
        raise InvalidUsage(f"Request does not adhere to schema \n{message}")


async def authenticate(request) -> dict:
    data = request.json
    user = await User.query.where(User.email == data["email"]).gino.all()
    if not user:
        raise AuthenticationFailed("Email not found.")

    if user[0].check_password(data["password"].encode()):
        return {"email": user[0].email}

    raise AuthenticationFailed("Password is incorrect.")
