from . import reg_signal, ErrorVK


@reg_signal('group_unban')
def group_unban(**kwargs):
    event_obj = kwargs['event']['object']

    try:
        kwargs['vk'].method('groups.unban', {"group_id": event_obj['group_id'],
                                             'owner_id': event_obj['user_id']})
    except ErrorVK as ev:
        return '0'
    return '1'
