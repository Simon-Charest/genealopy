from inspect import currentframe
from types import FrameType


def get_function_name(back: int = 1) -> str:
    current_frame: FrameType = currentframe()

    for _ in range(0, back):
        current_frame = current_frame.f_back

    return current_frame.f_code.co_name
