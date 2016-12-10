from pyramid.view import view_config

from ..models import Contact, ContactInfoItem


@view_config(route_name='contact', renderer='json')
def contact_set(request):
    if request.method == 'POST':
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

            request.dbsession \
                .query(Contact) \
                .filter(Contact.id == contact_data['id']) \
                .update({Contact.name: contact_data['name']})
        else:
            contact = Contact()
            contact.name = contact_data['name']
            request.dbsession.add(contact)
            request.dbsession.flush()
            request.dbsession.refresh(contact)

        for i, item_data in enumerate(contact_data['items']):
            item = ContactInfoItem()
            item.contact_id = contact_data['id']
            item.key = item_data['key']
            item.value = item_data['value']
            item.index = i
            request.dbsession.add(item)

        return {'result': 'ok', 'id': contact.id}
    elif request.method == 'GET':
        contact_id = request.params['id']
        contact = request.dbsession \
            .query(Contact) \
            .filter(Contact.id == contact_id) \
            .first()

        if contact is None:
            return {'result': 'failed', 'reason': 'object not found'}

        items = request.dbsession \
            .query(ContactInfoItem) \
            .filter(ContactInfoItem.contact_id == contact_id) \
            .all()

        return {
            'id': contact.id,
            'name': contact.name,
            'items': [{
                          'key': item.key,
                          'value': item.value,
                      } for item in items]
        }
    else:
        return {'result': 'failed'}

