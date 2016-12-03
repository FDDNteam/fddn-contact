from pyramid.view import view_config

from ..models import Contact, ContactInfoItem


@view_config(route_name='home', renderer='json')
def contact_update_view(request):
    one = request.json_body
    request.dbsession.query(ContactInfoItem).filter(ContactInfoItem.contact_id == one['id']).delete()
    request.dbsession.query(Contact).filter(Contact.id == one['id']).update({Contact.name: one['name']})
    return {"result":"OK"}
