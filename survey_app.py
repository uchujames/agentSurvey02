import streamlit as st
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup (integrated into survey_app.py)
DATABASE_URL = "sqlite:///survey.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class SurveyResponse(Base):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    opinion = Column(String)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Streamlit app logic
def main():
    st.title("Survey Form")

    name = st.text_input("Name")
    email = st.text_input("Email")
    opinion = st.text_area("Your Opinion")

    if st.button("Submit"):
        if name and email and opinion:
            db = next(get_db())
            response = SurveyResponse(name=name, email=email, opinion=opinion)
            db.add(response)
            db.commit()
            st.success("Thank you for your submission!")
        else:
            st.error("Please fill in all fields.")

if __name__ == "__main__":
    main()




# Key Points:
# - For this small project, keeping the database setup and Streamlit app logic in a single file (survey_app.py) is the easiest approach.
# - The survey.db file will be created automatically in the same directory as your survey_app.py file when you run the application for the first time.
# - No Separate Database File: You don't need to manually create the survey.db file. SQLite will handle that.