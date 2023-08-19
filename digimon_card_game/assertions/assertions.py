def assert_is_positive(number: int, reason: str) -> None:
    if number <= 0:
        raise ValueError(reason)
