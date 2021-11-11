from . import reg_signal, ErrorVK


@reg_signal('set_theme')
def set_theme(**kwargs):
    db = kwargs['db']
    event_obj = kwargs['event']['object']
    try:
        kwargs['vk'].method("messages.setConversationStyle", {
                                                     'peer_id': db.get_chat_uid(event_obj['chat_id'])+2000000000,
                                                     'style': event_obj['style']})
    except ErrorVK as ev:
        return '-1'
    return '1'
