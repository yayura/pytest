from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status_code is not equal to expected."
    WRONG_ELEMENTS_COUNT = "Number of element is not equal to exp"
