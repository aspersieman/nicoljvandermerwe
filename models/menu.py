
response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%s <%s>' % (settings.author, settings.author_email)
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = []

if 'auth' in globals():
    if auth.has_membership(auth.id_group("Admin")):
        response.menu = [
            (T('Index'),URL('index').xml()==URL().xml(),URL('index'),[]),
            (T('News Create'),URL('news_create').xml()==URL().xml(),URL('news_create'),[]),
            (T('News Select'),URL('news_select').xml()==URL().xml(),URL('news_select'),[]),
            (T('Projects Create'),URL('projects_create').xml()==URL().xml(),URL('projects_create'),[]),
            (T('Projects Select'),URL('projects_select').xml()==URL().xml(),URL('projects_select'),[]),
            (T('Blog Create'),URL('blog_create').xml()==URL().xml(),URL('blog_create'),[]),
            (T('Blog Select'),URL('blog_select').xml()==URL().xml(),URL('blog_select'),[]),
            (T('Cv Create'),URL('cv_create').xml()==URL().xml(),URL('cv_create'),[]),
            (T('Cv Select'),URL('cv_select').xml()==URL().xml(),URL('cv_select'),[]),
        ]

if not response.menu:
    response.menu = [
        (T('My Curriculum Vitae'),URL('cv/view').xml()==URL().xml(),URL('cv/view'),[]),
        (T('About'),URL('about/view').xml()==URL().xml(),URL('about/view'),[]),
        (T('News'),URL('news/view').xml()==URL().xml(),URL('news/view'),[]),
        (T('Projects'),URL('projects/view').xml()==URL().xml(),URL('projects_select'),[]),
        (T('Blog'),URL('pleph.appspot.com').xml()==URL().xml(),URL('pleph.appspot.com'),[]),
    ]
