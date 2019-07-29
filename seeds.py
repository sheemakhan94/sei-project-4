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


    entry_one = Entry(
        date='2019-07-29',
        what='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        image='image-url',
        user=sheema
    )

    entry_two = Entry(
        date='2019-07-30',
        what='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        image='image-url',
        user=sheema
    )

    entry_three = Entry(
        date='2019-07-20',
        what='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        image='image-url',
        user=sheema
    )

    entry_four = Entry(
        date='2019-07-10',
        what='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        image='image-url',
        user=sheema
    )

    entry_five = Entry(
        date='2019-07-14',
        what='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        image='image-url',
        user=sheema
    )



    backend = Component(step='finish backend')
    frontend = Component(step='finish frontend')
    collect_clothes = Component(step='pick up dirty clothes')
    wash_clothes = Component(step='put clothes in washing machine')
    dry_clothes = Component(step='put clothes in tumble dryer')
    put_away = Component(step='fold clothes and put in wardrobe')

    project = Task(
        title='Complete Project',
        components=[backend, frontend],
        due='2019-07-31 14:00:00',
        user=sheema
    )

    laundry = Task(
    title='Do Laundry',
    components=[collect_clothes, wash_clothes, dry_clothes, put_away],
    due='2019-07-29 07:00:00',
    user=sheema
    )

    friday_drinks = Event(
        event_name='Friday Drinks',
        event_date='2019-08-02 17:00:00',
        event_location='The Culpeper, 40 Commercial St, Spitalfields, London E1 6LP',
        user=sheema
    )

    project_due = Event(
        event_name='Final Project Due',
        event_date='2019-07-30 14:00:00',
        event_location='General Assembly',
        user=sheema
    )

    dinner = Event(
        event_name='Dinner',
        event_date='2019-07-29 19:00:00',
        event_location='Pret',
        user=sheema
    )

    reunion = Event(
        event_name='RoHo Reunion',
        event_date='2019-08-03 21:00:00',
        event_location='Royal Holloway',
        user=sheema
    )



    db.session.add(sheema)
    db.session.add(entry_one)
    db.session.add(entry_two)
    db.session.add(entry_three)
    db.session.add(entry_four)
    db.session.add(entry_five)
    db.session.add(project)
    db.session.add(backend)
    db.session.add(frontend)
    db.session.add(laundry)
    db.session.add(collect_clothes)
    db.session.add(wash_clothes)
    db.session.add(dry_clothes)
    db.session.add(put_away)
    db.session.add(friday_drinks)
    db.session.add(reunion)
    db.session.add(project_due)
    db.session.add(dinner)

    db.session.commit()
