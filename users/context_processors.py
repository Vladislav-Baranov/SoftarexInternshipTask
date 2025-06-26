menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Model", 'url_name': 'model'},
        #{'title': "Требования к изображениям", 'url_name': 'contact'},
]


def get_main_context(request):
    return {'menu': menu}
