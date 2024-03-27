import json, random


def dt_string(string) -> str:
    return string[::-1]


def dt_bool(boolean) -> bool:
    return boolean


def dt_cluster() -> (bool, int, str):
    lv_error = (True, 5001, "LV error from python")
    return lv_error


def dt_array(listinput) -> list:
    return listinput


class CalibReport:
    def __init__(self, user="Pythoneer", temperature=12.3,
                 verification=[{"Reference [kg]": 4, "DUT value [kg]": 4.02}]):
        self.User = user
        self.Temperature = temperature
        self.Verification = verification

    def load_from_dict(self, **kwargs):
        self.__dict__.update(kwargs)

    def setDummyValues(self):
        self.User = "Pythonuser"
        self.Temperature = 28.32
        self.Verification = [{"Reference [kg]": 4, "DUT value [kg]": 4},
                             {"Reference [kg]": 5, "DUT value [kg]": 5 + random.uniform(-0.5, 0.5)},
                             {"Reference [kg]": 6, "DUT value [kg]": 6 + random.uniform(-0.5, 0.5)},
                             {"Reference [kg]": 7, "DUT value [kg]": 7 + random.uniform(-0.5, 0.5)},
                             {"Reference [kg]": 8, "DUT value [kg]": 8 + random.uniform(-0.5, 0.5)},
                             {"Reference [kg]": 9, "DUT value [kg]": 9 + random.uniform(-0.5, 0.5)},
                             {"Reference [kg]": 10, "DUT value [kg]": 10}]

        return self


def dt_getobject() -> str:
    calib_report = CalibReport()
    calib_report.setDummyValues()
    return json.dumps(calib_report.__dict__)


def dt_setobject(jsonstring):
    # Load the object as a dictionary from json string
    dict_object = json.loads(jsonstring)

    # Create a new CalibReport Object
    report = CalibReport()

    # Update the values of report object with the dictionary object
    report.load_from_dict(**dict_object)

    return report.__str__()
