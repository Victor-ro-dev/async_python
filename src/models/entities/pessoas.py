from sqlalchemy import Table, Column, Integer, String
from src.models.settings.db_metadata import metadata

PESSOA = Table(
    'person', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)