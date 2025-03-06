from MySQL import DB, app
with app.app_context():
    # DB.drop_all()
    DB.create_all()