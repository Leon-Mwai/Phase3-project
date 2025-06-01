from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///meditrack.db')
Session = sessionmaker(bind=engine)
session = Session()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    medications = relationship('Medication', back_populates='patient', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Patient {self.name}, Age {self.age}>"

class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    time_to_take = Column(String, nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'))

    patient = relationship('Patient', back_populates='medications')

    def __repr__(self):
        return f"<Medication {self.name} - {self.dosage} @ {self.time_to_take}>"

