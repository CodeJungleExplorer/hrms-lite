from fastapi import HTTPException, status

def not_found(message: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    )

def conflict(message: str):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=message
    )
