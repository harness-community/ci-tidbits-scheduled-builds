"""Entrypoint for the scheduled-build demo.

The pipeline clones this file and runs its tests. A cron trigger starts
that pipeline when the clock matches, with no one clicking Run.
"""

APP_NAME = "tidbits-scheduled-builds"
VERSION = "1.0.0"


def greeting() -> str:
    return f"{APP_NAME} {VERSION} — built on a schedule"


if __name__ == "__main__":
    print(greeting())
