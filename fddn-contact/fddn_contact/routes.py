def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('set-contact','/set_contact')
    config.add_route('get-contact','/get_contact')
