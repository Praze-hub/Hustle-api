from customuser.utils import CustomEnum


class BookingStatus(CustomEnum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    DECLINED = 'declined'
    
    