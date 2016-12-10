from pyramid.view import view_config

from ..models import Contact, ContactInfoItem


@view_config(route_name='update', renderer='json')
def contact_update_view(request):
    contact_data = request.json_body

    if 'id' in contact_data:
        contact = request.dbsession \
            .query(Contact) \
            .filter(Contact.id == contact_data['id']) \
            .first()

        if contact is None:
            return {'result': 'failed', 'reason': 'object not found'}

        request.dbsession\
            .query(ContactInfoItem)\
            .filter(ContactInfoItem.contact_id == contact_data['id'])\
            .delete()
    else:
        pass

    request.dbsession\
        .query(Contact)\
        .filter(Contact.id == contact_data['id'])\
        .update({Contact.name: contact_data['name']})

    for i, item_data in enumerate(contact_data['items']):
        item = ContactInfoItem()
        item.contact_id = contact_data['id']
        item.key = item_data['key']
        item.value = item_data['value']
        item.index = i
        request.dbsession.add(item)

    return {"result": "ok"}
