from rest_framework.views import exception_handler
import traceback
from django.conf import settings

def custom_exception_handler(exc, context):
    # Call DRF's default handler first to get the standard error response
    response = exception_handler(exc, context)

    # Only add debug info if we actually got a response *and* we're in DEBUG mode
    if response is not None and settings.DEBUG:
        # Some DRF errors give you `response.data` as a list, some as a dict
        # so we must check the type first:
        if isinstance(response.data, dict):
            response.data["exception"] = str(exc)
            response.data["trace"] = traceback.format_exc()
        else:
            # It's probably a list, e.g. ["This field is required", "Another error..."]
            # You can decide how you want to handle it. For example:
            # Turn it into a dict:
            response.data = {
                "errors": response.data,
                "exception": str(exc),
                "trace": traceback.format_exc()
            }

    return response