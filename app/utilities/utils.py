from bson import ObjectId
from datetime import datetime, timezone

def jsonDecoder(obj):
    if isinstance(obj, ObjectId):
        return int(str(obj), 16)
    
    elif isinstance(obj, datetime):
        if obj.tzinfo is None:
            obj = obj.replace(tzinfo = timezone.utc)
        return obj.isoformat()

    else:
        return obj