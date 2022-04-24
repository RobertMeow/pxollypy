from . import reg_signal, ErrorVK


@reg_signal('delete_for_all')
def add_chat(**kwargs):
    db = kwargs['db']
    event_obj = kwargs['event']['object']
    try:
        response = kwargs['vk'].method('messages.delete', {
            'cmids': str(event_obj['conversation_message_ids'])[1:-1].replace(' ', ''),
            'delete_for_all': True,
            'peer_id': db.get_chat_uid(event_obj['chat_id'])+2000000000
        })
        return str([cmi for cmi in response if response[cmi]])[1:-1].replace(' ', '')
    except ErrorVK:
        return '0'
