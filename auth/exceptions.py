from fastapi import HTTPException, status


UserExist = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="User with this email already exists",
)

InvalidCredentials = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Email or password is incorrect. Incorrect login credentials",
)

TokenExpired = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired",
    headers={"WWW-Authenticate": "Bearer"},
)

UnvalidatedCredentials = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

UserDoesNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Could not find user",
)