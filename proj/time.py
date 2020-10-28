#    Copyright 2020 June Hanabi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import datetime


def get_time() -> datetime:
    """
    Returns the current time
    Thank you kite
    https://www.kite.com/python/answers/how-to-calculate-a-time-difference-in-minutes-in-python#:~:text=Subtract%20one%20datetime%20object%20from,the%20time%20difference%20in%20minutes.

    :return: A datetime object containing the current time
    """
    return datetime.datetime.today()


def get_minutes(time_end: datetime, time_start: datetime) -> int:
    """
    Converts 2 dates to minutes
    Thank you kite
    https://www.kite.com/python/answers/how-to-calculate-a-time-difference-in-minutes-in-python#:~:text=Subtract%20one%20datetime%20object%20from,the%20time%20difference%20in%20minutes.

    :param time_end: End timestamp
    :param time_start: Start timestamp
    :return: Minutes between them
    """
    time_delta = (time_end - time_start)
    total_seconds = time_delta.total_seconds()
    return int(total_seconds / 60)


def get_minutes_remain(minutes: int) -> int:
    """
    Returns minutes remaining after converting to hours

    :param minutes: Total minutes before converting to hours
    :return: minutes after converting to hours
    """
    return minutes % 60


def get_hours(minutes: int) -> int:
    """
    Converts minutes to hours

    :param minutes: Minutes before conversion
    :return: Hours
    """
    return int(minutes / 60)


def get_time_str(minutes: int) -> str:
    """
    Returns a printable timestamp of the difference in hours and minutes from an unconverted minutes

    :param minutes: Unconverted minutes
    :return: Printable string
    """

    hours = get_hours(minutes)
    minutes_remain = get_minutes_remain(minutes)
    minutes_str = ""

    if minutes_remain < 10:
        minutes_str = "0" + str(minutes_remain)
    else:
        minutes_str = str(minutes_remain)

    return str(hours) + ":" + minutes_str
