from genealopy.constant import (
    FEMALE_COLOR, FEMALE_INCOMPLETE_COLOR, MALE_COLOR, MALE_INCOMPLETE_COLOR,
    PARENT_LINK_STYLE, UNDEFINED_COLOR, UNDEFINED_LINK_STYLE
)


def get_color(gender: str, complete: bool = True) -> str:
    color: str

    if gender in ["F", "mother", "grandmother"]:
        if complete:
            color = FEMALE_COLOR

        else:
            color = FEMALE_INCOMPLETE_COLOR

    elif gender in ["M", "father", "grandfather"]:
        if complete:
            color = MALE_COLOR

        else:
            color = MALE_INCOMPLETE_COLOR

    else:
        color = UNDEFINED_COLOR

    return color


def get_style(type: str) -> str:
    if type in ["F", "mother", "grandmother", "M", "father", "grandfather"]:
        return PARENT_LINK_STYLE

    else:
        return UNDEFINED_LINK_STYLE
