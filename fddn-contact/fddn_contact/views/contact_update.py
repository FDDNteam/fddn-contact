from pyramid.view import view_config

from ..models import Contact, ContactInfoItem


@view_config(route_name='home', renderer='json')
def contact_update_view(request):
    query = request.dbsession.query(Contact)
    one = request.json_body
    query(ContactInfoItem).filter(ContactInfoItem.contact_id == one['id']).delete()
    query(Contact).filter(Contact.id == one['id']).update({Contact.name: one['name']})
    return {"result":"OK"}
