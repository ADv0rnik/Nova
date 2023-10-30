def merge_dict(destination: dict, source: dict):
    """
    source: https://stackoverflow.com/a/20666342
    """

    for key, value in source.items():
        if isinstance(value, dict) and isinstance(destination.get(key), dict):
            destination[key] = merge(destination[key], value)
        else:
            destination[key] = value

    return destination
