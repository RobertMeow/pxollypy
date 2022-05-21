from . import reg_signal, ErrorVK


@reg_signal('group_ban')
def group_ban(**kwargs):
    event_obj = kwargs['event']['object']

    try:
        kwargs['vk'].method('groups.ban', {"group_id": event_obj['group_id'],
                                           'owner_id': event_obj['user_id'],
                                           'end_date': event_obj['expired']})
    except ErrorVK as ev:
        return '0'
    return '1'
