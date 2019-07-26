from app import app
from controllers import entries, tasks, events, auth

app.register_blueprint(entries.api, url_prefix='/api')
app.register_blueprint(tasks.api, url_prefix='/api')
app.register_blueprint(events.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
