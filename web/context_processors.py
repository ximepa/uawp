def enable_cabinet(request):
    try:
        from uawp.settings import ENABLE_CABINET
        return {'ENABLE_CABINET': ENABLE_CABINET,}
    except ImportError:
        return {'ENABLE_CABINET': 'True',}


def enable_feedback(request):
    try:
        from uawp.settings import ENABLE_FEEDBACK
        return {'ENABLE_FEEDBACK': ENABLE_FEEDBACK,}
    except ImportError:
        return {'ENABLE_FEEDBACK': 'True',}