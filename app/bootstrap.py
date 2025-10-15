# app/bootstrap.py
import logging
from app.core.database import Base, engine, SessionLocal
from app.models import user, project, department  # import all models so Base.metadata sees them

logger = logging.getLogger("bootstrap")

def init_db():
    """
    Create all database tables and seed initial data if necessary.
    """
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Tables created successfully.")

    # Optionally seed data
    seed_initial_data()


def seed_initial_data():
    """
    Add default entries like admin user or default department.
    """
    db = SessionLocal()
    try:
        from app.models.user import User  # adjust for your actual model
        admin = db.query(User).filter_by(username="admin").first()

        if not admin:
            logger.info("👤 Creating default admin user...")
            admin = User(username="admin", email="admin@againbuilders.com", hashed_password="changeme")
            db.add(admin)
            db.commit()
            logger.info("Admin user created.")
        else:
            logger.info("Admin user already exists.")
    except Exception as e:
        logger.error(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
