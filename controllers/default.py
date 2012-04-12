# -*- coding: utf-8 -*- 
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call():
    session.forget()
    return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
@auth.requires_membership('Admin')
def news_create():
    form=crud.create(db.t_news,next='news_read/[id]')
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def news_read():
    record = db.t_news(request.args(0)) or redirect(URL('error'))
    form=crud.read(db.t_news,record)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def news_update():
    record = db.t_news(request.args(0),active=True) or redirect(URL('error'))
    form=crud.update(db.t_news,record,next='news_read/[id]',
                     ondelete=lambda form: redirect(URL('news_select')),
                     onaccept=crud.archive)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def news_select():
    f,v=request.args(0),request.args(1)
    try: query=f and db.t_news[f]==v or db.t_news
    except: redirect(URL('error'))
    rows=db(query)(db.t_news.active==True).select()
    return dict(rows=rows)

@auth.requires_login()
@auth.requires_membership('Admin')
def news_search():
    form, rows=crud.search(db.t_news,query=db.t_news.active==True)
    return dict(form=form, rows=rows)

@auth.requires_login()
@auth.requires_membership('Admin')
def projects_create():
    form=crud.create(db.t_projects,next='projects_read/[id]')
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def projects_read():
    record = db.t_projects(request.args(0)) or redirect(URL('error'))
    form=crud.read(db.t_projects,record)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def projects_update():
    record = db.t_projects(request.args(0),active=True) or redirect(URL('error'))
    form=crud.update(db.t_projects,record,next='projects_read/[id]',
                     ondelete=lambda form: redirect(URL('projects_select')),
                     onaccept=crud.archive)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def projects_select():
    f,v=request.args(0),request.args(1)
    try: query=f and db.t_projects[f]==v or db.t_projects
    except: redirect(URL('error'))
    rows=db(query)(db.t_projects.active==True).select()
    return dict(rows=rows)

@auth.requires_login()
@auth.requires_membership('Admin')
def projects_search():
    form, rows=crud.search(db.t_projects,query=db.t_projects.active==True)
    return dict(form=form, rows=rows)

@auth.requires_login()
@auth.requires_membership('Admin')
def blog_create():
    form=crud.create(db.t_blog,next='blog_read/[id]')
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def blog_read():
    record = db.t_blog(request.args(0)) or redirect(URL('error'))
    form=crud.read(db.t_blog,record)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def blog_update():
    record = db.t_blog(request.args(0),active=True) or redirect(URL('error'))
    form=crud.update(db.t_blog,record,next='blog_read/[id]',
                     ondelete=lambda form: redirect(URL('blog_select')),
                     onaccept=crud.archive)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def blog_select():
    f,v=request.args(0),request.args(1)
    try: query=f and db.t_blog[f]==v or db.t_blog
    except: redirect(URL('error'))
    rows=db(query)(db.t_blog.active==True).select()
    return dict(rows=rows)

@auth.requires_login()
@auth.requires_membership('Admin')
def blog_search():
    form, rows=crud.search(db.t_blog,query=db.t_blog.active==True)
    return dict(form=form, rows=rows)

@auth.requires_login()
@auth.requires_membership('Admin')
def resume_create():
    form=crud.create(db.t_resume,next='resume_read/[id]')
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def resume_read():
    record = db.t_resume(request.args(0)) or redirect(URL('error'))
    form=crud.read(db.t_resume,record)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def resume_update():
    record = db.t_resume(request.args(0),active=True) or redirect(URL('error'))
    form=crud.update(db.t_resume,record,next='resume_read/[id]',
                     ondelete=lambda form: redirect(URL('resume_select')),
                     onaccept=crud.archive)
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Admin')
def resume_select():
    f,v=request.args(0),request.args(1)
    try: query=f and db.t_resume[f]==v or db.t_resume
    except: redirect(URL('error'))
    rows=db(query)(db.t_resume.active==True).select()
    return dict(rows=rows)

@auth.requires_login()
@auth.requires_membership('Admin')
def resume_search():
    form, rows=crud.search(db.t_resume,query=db.t_resume.active==True)
    return dict(form=form, rows=rows)

