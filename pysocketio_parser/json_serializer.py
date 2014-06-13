import json


def json_serializer(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()

    raise TypeError("Unserializable object %s of type %s" % (obj, type(obj)))


def dumps(*args, **kwargs):
    return json.dumps(default=json_serializer, *args, **kwargs)

loads = json.loads
