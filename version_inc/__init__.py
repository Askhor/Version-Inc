import argparse
import re


def kw_transformation(kw):
    return f"<{kw}>"


YEAR = kw_transformation("YEAR")
MONTH = kw_transformation("MONTH")
DAY = kw_transformation("DAY")
WEEK = kw_transformation("WEEK")
WEEK_DAY = kw_transformation("WDAY")
COUNTER = kw_transformation("COUNTER")
MAJOR = kw_transformation("MAJOR")
MINOR = kw_transformation("MINOR")
VARIABLES = {"COUNTER": COUNTER, "MAJOR": MAJOR, "MINOR": MINOR}


def command_entry_point():
    try:
        run_version_inc()
    except KeyboardInterrupt:
        pass


def reading_re(template: str):
    template = template.replace(".", "\\.")
    template = re.compile(kw_transformation("(YEAR|MONTH|DAY|WEEK|WDAY)")).sub("[0-9]+", template)
    template = template.replace(COUNTER, "(?P<COUNTER>[0-9]+)")
    template = template.replace(MAJOR, "(?P<MAJOR>[0-9]+)")
    template = template.replace(MINOR, "(?P<MINOR>[0-9]+)")

    return re.compile(template)


def new_version(template: str, variables):
    for var in VARIABLES:
        if var in variables:
            template = template.replace(VARIABLES[var], variables[var])

    print(template)
    return template


def run_version_inc():
    parser = argparse.ArgumentParser(
        prog="Version-Inc",
        description="A lightweight tool for incrementing version numbers in files"
    )
    parser.add_argument("VERSION_TEMPLATE")
    args = parser.parse_args()