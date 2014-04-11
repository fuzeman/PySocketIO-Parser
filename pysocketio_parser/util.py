def try_convert(value, to_type, default=None):
    try:
        return to_type(value)
    except:
        return default
