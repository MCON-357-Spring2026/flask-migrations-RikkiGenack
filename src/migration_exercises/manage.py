from .app import create_app
from .extensions import db
from .models import Student, Assignment, Grade
app = create_app()

# TODO 3:
# Import db and models here so Flask-Migrate can detect them.
#
# Example:
# from .extensions import db
# from .models import Student, Assignment, Grade
from flask_migrate import Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)