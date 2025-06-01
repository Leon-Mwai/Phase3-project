from .models import session, Patient, Medication, Base, engine

def seed():
    Base.metadata.create_all(engine)
    session.query(Medication).delete()
    session.query(Patient).delete()

    p1 = Patient(name="Alex Kim", age=30)
    p2 = Patient(name="Jamie Smith", age=25)

    m1 = Medication(name="Ibuprofen", dosage="200mg", time_to_take="8AM", patient=p1)
    m2 = Medication(name="Amoxicillin", dosage="500mg", time_to_take="2PM", patient=p2)

    session.add_all([p1, p2, m1, m2])
    session.commit()
    print("DB seeded ")
