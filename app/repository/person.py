from sqlalchemy import update, delete
from sqlalchemy import select

from app.config import db, commit_rollback
from app.schemas import PersonCreate
from app.models import Person


class PersonRepository:

    @staticmethod
    async def create(person: PersonCreate):
        """Create a new person."""
        db.add(Person(**person.dict()))
        await commit_rollback()

    """Get a person by id."""
    @staticmethod
    async def get_by_id(person_id: int):
        """ retrieve person data by id """
        query = select(Person).where(Person.id == person_id)
        return (await db.execute(query)).scalar_one_or_none()
        
    @staticmethod
    async def update(person_id: int, form_person: PersonCreate) -> Person:
        """Update person data"""
        query = update(Person)\
        .where(Person.id == person_id)\
        .values(**form_person.dict())\
        .execution_options(synchronize_session="fetch")

        await db.execute(query)
        await commit_rollback()

    @staticmethod
    async def delete(person_id: int) -> None:
        """Delete a person by id."""
        query = delete(Person).where(Person.id == person_id)
        await db.execute(query)
        await commit_rollback()