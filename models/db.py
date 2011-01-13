# -*- coding: utf-8 -*- 
# this file is released under public domain and you can use without limitations
if request.env.web2py_runtime_gae:
    db = DAL("gae")
    session.connect(request, response, db = db)
else:                                         
    db = DAL("sqlite://storage.sqlite")      

from gluon.tools import *
mail = Mail()
auth = Auth(globals(),db)
crud = Crud(globals(),db)
service = Service(globals())
plugins = PluginManager()

mail.settings.server = "logging" or "smtp.gmail.com:587"
mail.settings.sender = "aspersieman@gmail.com"
mail.settings.login = "aspersieman@gmail.com:"

auth.settings.hmac_key = "sha512:192f4beb-7cf8-4a6a-8233-d124cfde9ac8"

db.define_table("auth_user",
    Field("id","id",
          represent=lambda id:SPAN(id," ",A("view",_href=URL("auth_user_read",args=id)))),
    Field("username", type="string",
          label=T("Username")),
    Field("first_name", type="string",
          label=T("First Name")),
    Field("last_name", type="string",
          label=T("Last Name")),
    Field("email", type="string",
          label=T("Email")),
    Field("password", type="password",
          readable=False,
          label=T("Password")),
    Field("created_on","datetime",default=request.now,
          label=T("Created On"),writable=False,readable=False),
    Field("modified_on","datetime",default=request.now,
          label=T("Modified On"),writable=False,readable=False,
          update=request.now),
    Field("registration_key",default="",
          writable=False,readable=False),
    Field("reset_password_key",default="",
          writable=False,readable=False),
    Field("registration_id",default="",
          writable=False,readable=False),
    format="%(username)s",
    migrate=settings.migrate)


db.auth_user.first_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.last_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.password.requires = CRYPT(key=auth.settings.hmac_key)
db.auth_user.username.requires = IS_NOT_IN_DB(db, db.auth_user.username)
db.auth_user.registration_id.requires = IS_NOT_IN_DB(db, db.auth_user.registration_id)
db.auth_user.email.requires = (IS_EMAIL(error_message=auth.messages.invalid_email),
                               IS_NOT_IN_DB(db, db.auth_user.email))
auth.define_tables(migrate=settings.migrate)
auth.settings.mailer = mail
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.messages.verify_email = "Click on the link http://"+request.env.http_host+URL(r=request,c="default",f="user",args=["verify_email"])+"/%(key)s to verify your email"
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = "Click on the link http://"+request.env.http_host+URL(r=request,c="default",f="user",args=["reset_password"])+"/%(key)s to reset your password"

#crud.settings.auth = auth

mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login

# Initial setup
admin = db(db.auth_user.email == settings.administrator or none).select()
if admin:
    admingroup = db(db.auth_group.role == "Admin").select()
    if not admingroup:
        admingroup_id = auth.add_group(role = "Admin", description = "Administrator group.")
    else:
        admingroup_id = admingroup[0].id

    admingroup_membership = db((db.auth_membership.user_id == admin[0].id)&(db.auth_membership.group_id == admingroup_id)).select()
    if not admingroup_membership:
        auth.add_membership(admingroup_id, admin[0].id)
    adminpermission_categories = db((db.auth_permission.group_id == admingroup_id)&(db.auth_permission.table_name == "categories")).select(db.auth_permission.id)
    if not adminpermission_categories:
        auth.add_permission(admingroup_id, "create", "categories")
    adminpermission_images = db((db.auth_permission.group_id == admingroup_id)&(db.auth_permission.table_name == "images")).select(db.auth_permission.id)
    if not adminpermission_images:
        auth.add_permission(admingroup_id, "create", "images")
