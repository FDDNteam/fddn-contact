from pyramid.view import view_config

from ..models import Contact, ContactInfoItem


@view_config(route_name='home', renderer='json')
def contact_update_view(request):
    contact_data = request.json_body

    request.dbsession\
        .query(ContactInfoItem)\
        .filter(ContactInfoItem.contact_id == contact_data['id'])\
        .delete()

    request.dbsession\
        .query(Contact)\
        .filter(Contact.id == contact_data['id'])\
        .update({Contact.name: contact_data['name']})

    for item in contact_data['items']:
        pass

    return {"result":"OK"}
