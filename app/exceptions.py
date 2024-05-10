from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    detail: str = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'This user already exists.'


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect email or password.'


class ExpiredTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Your token has expired.'


class AbsentTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Can't find your token."


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect token format.'


# Explicitly vague error message due to security reasons.
class UserIsNotPresentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED


class RoomFullyBookedException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'There are no vacant rooms left.'


class RoomCannotBeBookedException(BookingException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'Unable to book a room due to an unknown reason.'


class DateFromCannotBeAfterDateToException(BookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Logical error: date_from can not be later then date_to.'


class CannotBookHotelForLongerException(BookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "You can't book a hotel for more than 1 months"


class CannotAddToDatabaseException(BookingException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'Unnable to add data to database'


class CannotProcesCSVException(BookingException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'Unable to process given csv file'


class HotelsNotFoundException(BookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Hotels not found'


class RoomsNotFoundException(BookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Rooms not found'


class BookingsNotFoundException(BookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Bookings not found'
