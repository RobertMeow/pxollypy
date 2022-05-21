from . import reg_signal


@reg_signal('ping')
def ping(**kwargs):
    return '1'
