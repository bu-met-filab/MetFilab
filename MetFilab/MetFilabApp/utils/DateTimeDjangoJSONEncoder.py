import datetime
from django.core.serializers.json import DjangoJSONEncoder
import decimal
from django.utils.timezone import is_aware

class DateTimeDjangoJSONEncoder(DjangoJSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time and decimal types.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            # r = o.isoformat()
            r = o.strftime("%y-%m-%d %H:%M:%S")
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            # return o.isoformat()
            return o.strftime("%y-%m-%d")
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            # r = o.isoformat()
            r = o.strftime("%H:%M:%S")
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DateTimeDjangoJSONEncoder, self).default(o)