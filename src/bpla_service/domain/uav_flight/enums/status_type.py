from enum import StrEnum


class UavFlightStatusType(StrEnum):
    ACCEPTED = "accepted"
    FINISHED = "finished"
    REJECTED = "rejected"
    UNDER_REVIEW = "under_review"
