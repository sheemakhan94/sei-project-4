import os

db_uri = os.getenv('DATABASE_URI', 'postgres://localhost:5432/journals')
secret = os.getenv('SECRET', 'not telling you')
