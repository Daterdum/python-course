# Match case code examples
# More examples https://habr.com/ru/company/yandex_praktikum/blog/547902/

import random


def literal_pattern_match():  # Also shows wildcard_pattern '_'
    num = random.choice(range(5))

    match num:
        case 0:  # if num == 0
            print("Zero")

        case 1:  # elif num == 1
            print("One")

        case _:  # else
            print("Not zero or one")


def capture_pattern_match(name):
    match name:
        case "":
            print("Hello unknown person")

        case name:
            print(f"Dobriy den {name}")


class Statuses:
    OK = 200
    AUTH_ERROR = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    ERROR = 500


def _constant_pattern_match(status, message):
    print(f"{status=}, {message=}")
    match status, message:
        case Statuses.OK, ok_msg:
            print(f'Handler successful {status}, {ok_msg}')

        case Statuses.FORBIDDEN, err_msg:
            print(f'Handler forbidden {status}, {err_msg}')

        case Statuses.ERROR, err_msg if err_msg:  # guard
            print(f'Handler failed with error: {err_msg}')

        case _:
            print('idk this status or err_msg was not provided')


def constant_pattern_match():
    _constant_pattern_match(
        status=random.choice((
            Statuses.OK,
            Statuses.AUTH_ERROR,
            Statuses.FORBIDDEN,
            Statuses.NOT_FOUND,
            Statuses.ERROR,
        )),
        message="Status message"
    )

    _constant_pattern_match(Statuses.ERROR, "Error explanation")  # >>> Handler failed with error: Error explanation
    _constant_pattern_match(Statuses.ERROR, "")  # >>> idk this status or err_msg was not provided


# Unquote pattern to try
if __name__ == '__main__':
    # literal_pattern_match()
    # capture_pattern_match(name=input("Enter name for capture pattern or press enter to stay unknown: "))
    # constant_pattern_match()
    pass
