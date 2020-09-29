from common.constant import constant


def get_color(gender, complete=True):
    if gender in ['F', 'mother']:
        if complete:
            color = constant.FEMALE_COLOR

        else:
            color = constant.FEMALE_INCOMPLETE_COLOR

    elif gender in ['M', 'father']:
        if complete:
            color = constant.MALE_COLOR

        else:
            color = constant.MALE_INCOMPLETE_COLOR

    else:
        color = constant.UNDEFINED_COLOR

    return color


def get_style(type_):
    if type_ in ['F', 'mother', 'M', 'father']:
        style = constant.PARENT_LINK_STYLE

    else:
        style = constant.UNDEFINED_LINK_STYLE

    return style