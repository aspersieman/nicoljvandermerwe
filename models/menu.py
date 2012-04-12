
response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = "%s <%s>" % (settings.author, settings.author_email)
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = []

if "auth" in globals():
    if auth.has_membership(auth.id_group("Admin")):
        response.menu = [
            (T("Index"),URL("index")==URL(),URL("index"),[]),
            (T("News Create"),URL("news_create")==URL(),URL("news_create"),[]),
            (T("News Select"),URL("news_select")==URL(),URL("news_select"),[]),
            (T("Projects Create"),URL("projects_create")==URL(),URL("projects_create"),[]),
            (T("Projects Select"),URL("projects_select")==URL(),URL("projects_select"),[]),
            (T("Blog Create"),URL("blog_create")==URL(),URL("blog_create"),[]),
            (T("Blog Select"),URL("blog_select")==URL(),URL("blog_select"),[]),
            (T("Resume Create"),URL("resume_create")==URL(),URL("resume_create"),[]),
            (T("Resume Select"),URL("resume_select")==URL(),URL("resume_select"),[]),
        ]

if not response.menu:
    response.menu = [
        (T("Resume"),URL("resume/view")==URL(),URL("resume/view"),[]),
        (T("Projects"),URL("projects/view")==URL(),URL("projects_select"),[]),
        (T("About"),URL("about/view")==URL(),URL("about/view"),[]),
        (T("News"),URL("news/view")==URL(),URL("news/view"),[]),
        (T("Blog"),URL("", scheme = True, host =
                       "pleph.appspot.com") == URL(),URL("", scheme =
                                                                True, host =
                       "pleph.appspot.com"),[]),
    ]
