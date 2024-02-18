menu = [{'title': 'О сайте', 'url': 'about'},
        {'title': 'Добавить статью', 'url': 'add_page'},
        {'title': 'Обратная связь', 'url': 'contact'},
        {'title': 'Загрузить файл', 'url': 'loadfile'},
        # {'title': 'Войти', 'url': 'login'},
        ]


class DataMixin:
    paginate_by = 5
    title_page = None
    extra_context = {}
    cat_selected = None

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
        # if 'menu' not in self.extra_context:
        #     self.extra_context['menu'] = menu
        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        # context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context
