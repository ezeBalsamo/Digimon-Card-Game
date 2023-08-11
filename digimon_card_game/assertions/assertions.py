def assert_is_positive(number: int, reason: str):
    if number <= 0:
        raise ValueError(reason)
