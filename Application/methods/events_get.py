from . import reg_signal, Signals


@reg_signal('events_get')
def events_get(**kwargs):
    return str(list(Signals.methods))
