from . import reg_signal, ErrorVK


@reg_signal('invite_user')
def invite_user(**kwargs):
    db = kwargs['db']
    event_obj = kwargs['event']['object']
    try:
        kwargs['vk'].method("messages.addChatUser", {'chat_id': db.get_chat_uid(event_obj['chat_id']),
                                                     'user_id': event_obj['user_id'],
                                                     'visible_messages_count': event_obj['visible_messages_count'] if 'visible_messages_count' in event_obj else None})
    except ErrorVK as ev:
        return '-1'
    return '1'
