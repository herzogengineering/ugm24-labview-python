def dt_string(string) -> str:
    return string[::-1]


def dt_bool(boolean) -> bool:
    return boolean


def dt_cluster() -> (bool, int, str):
    lv_error = (True, 5001, "LV error from python")
    return lv_error


def dt_array(listinput) -> list:
    return listinput