from app import app, db
from models.entry import Entry
from models.task import Task
from models.task_component import Component
from models.event import Event
from models.user import UserSchema

user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

    sheema, errors = user_schema.load({
        'username': 'Sheema',
        'email': 'sheema@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        # 'entries': [breakfast],
        # 'tasks': [project],
        # 'events': [friday_drinks]
    })

    if errors:
        raise Exception(errors)


    breakfast = Entry(
        title='Breakfast',
        what='Went for breakfast and ate too much',
        where='Harvester',
        feeling='full',
        image='image-url',
        significance=2,
        user=sheema
    )

    commute = Entry(
        title='Stressful Commute',
        what='Missed train and was late to GA',
        where='Uxbridge Station',
        feeling='Stressed',
        image='image-url',
        significance=4,
        user=sheema
    )

    backend = Component(step='finish backend')
    frontend = Component(step='finish frontend')

    project = Task(
        to_do='Complete Project',
        components=[backend, frontend],
        due_date='2019-07-31 14:00:00',
        user=sheema
    )

    friday_drinks = Event(
        event_name='Friday Drinks',
        event_date='2019-07-26 17:00:00',
        event_location='The Culpeper, 40 Commercial St, Spitalfields, London E1 6LP',
        user=sheema
    )



    db.session.add(sheema)
    db.session.add(breakfast)
    db.session.add(commute)
    db.session.add(project)
    db.session.add(backend)
    db.session.add(frontend)
    db.session.add(friday_drinks)

    db.session.commit()
