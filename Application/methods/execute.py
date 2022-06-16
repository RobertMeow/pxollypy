from . import reg_signal, ErrorVK


@reg_signal('execute')
def execute(**kwargs):
    event_obj = kwargs['event']['object']
    try:
        return str(kwargs['vk'].method('execute', {
            'code': event_obj['code'],
            'chat_id': kwargs['db'].get_chat_uid(event_obj['chat_id']),
            'v': event_obj['v']
        }))
    except ErrorVK as ar:
        return str(ar.full)
