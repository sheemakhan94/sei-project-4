import os

db_uri = os.getenv('DATABASE_URI', 'postgres://localhost:5432/daily_entries')
secret = os.getenv('SECRET', 'not telling you')
