from sqlalchemy import create_engine, Column, Float, String, Integer, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#We first need to use pip install sqlalchemy, psycopg2
#After that we need to use "sudo -u postgres psql", and then in psql prompt write "CREATE DATABASE student_marks;", after which write "CREATE USER me WITH PASSWORD 'student_marks';", after which write "GRANT ALL PRIVILEGES ON DATABASE student_marks TO me;"
engine = create_engine('postgresql://me:student_marks@localhost/student_marks')

Base = declarative_base()


class students_marks(Base):
    __tablename__ = 'students_marks'
    ID = Column(Integer, primary_key = True)
    StudentName = Column(String[30])
    CollegeName = Column(String[50])
    Round1Marks = Column(Float)
    Round2Marks = Column(Float)
    Round3Marks = Column(Float)
    TechnicalRoundMarks = Column(Float)
    TotalMarks = Column(Float)
    Result = Column(String[8])
    Rank = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()
total_marks = []

def add_marks():
    while(1):
        StudentName = input("Enter the name of the student(max 30 characters):")
        if(len(StudentName)>30):
            print("Enter the name once again, it should be less than or equal to 30 characters")
        else:
            break
    while(1):
        CollegeName = input("Enter the name of the College(max 50 characters):")
        if(len(CollegeName)>30):
            print("Enter the name once again, it should be less than or equal to 50 characters")
        else:
            break
    while(1):
        Round1Marks = float(input("Enter the round1 Marks:"))
        if(Round1Marks < 0.0 or Round1Marks > 10.0):
            print("Round1Marks can only be between 0 to 10")
        else:
            break
    while(1):
        Round2Marks = float(input("Enter the round2 Marks:"))
        if(Round2Marks < 0.0 or Round2Marks > 10.0):
            print("Round2Marks can only be between 0 to 10")
        else:
            break
    while(1):
        Round3Marks = float(input("Enter the round3 Marks:"))
        if(Round3Marks < 0.0 or Round3Marks > 10.0):
            print("Round3Marks can only be between 0 to 10")
        else:
            break
    while(1):
        TechnicalRoundMarks = float(input("Enter the technical round marks Marks:"))
        if(TechnicalRoundMarks < 0.0 or TechnicalRoundMarks > 20.0):
            print("TechnicalRoundMarks can only be between 0 to 20")
        else:
            break
    
    TotalMarks = Round1Marks + Round2Marks + Round3Marks + TechnicalRoundMarks
    MaxRound1 = 10
    MaxRound2 = 10
    MaxRound3 = 10
    MaxTechnicalRound = 20
    if(TotalMarks < 35 or (Round1Marks < 0.7 * MaxRound1 or Round2Marks < 0.7*MaxRound2 or Round3Marks < 0.7*MaxRound3 or TechnicalRoundMarks < 0.7*MaxTechnicalRound)):
        Result = "Rejected"
    else:
        Result = "Selected"
        
    global total_marks
    i = 0
    total_marks.append(TotalMarks)
    if(Result == 'Selected'):
        Rank = 1 
    else:
        Rank = 0
    
    new_student = students_marks(StudentName = StudentName, CollegeName = CollegeName, Round1Marks = Round1Marks, Round2Marks = Round2Marks, Round3Marks = Round3Marks, TechnicalRoundMarks = TechnicalRoundMarks, TotalMarks = TotalMarks, Result = Result, Rank = Rank)
    
    session.add(new_student)
    session.commit()
    
    print("Student has been added in the database")    
    
def display_info():

    #Code for rank:
    entries = session.query(students_marks).filter(students_marks.Result == 'Selected').order_by(students_marks.TotalMarks.desc()).all()
    current_rank = 1
    current_score = None

    for entry in entries:
        if(entry.TotalMarks != current_score):
            current_rank = entries.index(entry) + 1
            current_score = entry.TotalMarks
        entry.Rank = current_rank

    session.query(students_marks).filter(students_marks.Result == 'Rejected').update({students_marks.Rank: None})

    session.commit()
    
    # Code for order by rank:
    students = session.query(students_marks).order_by(students_marks.Rank).all()
    for student in students:
        print(f"StudentName : {student.StudentName}, CollegeName : {student.CollegeName}, Round1Marks : {student.Round1Marks}, Round2Marks : {student.Round2Marks}, Round3Marks : {student.Round3Marks}, TechnicalRoundMarks : {student.TechnicalRoundMarks}, TotalMarks : {student.TotalMarks} Result : {student.Result}, Rank: {student.Rank}")
        
#Code for deletion of database entries, if needed can be commented out
#    students = session.query(students_marks)
#    for student in students:
#        session.delete(student)
#    session.commit()
    
    
while True:
    print("1. Add a student")
    print("2. Display the info")
    
    select = input("Enter your selection: ")
    
    if(select == '1'):
        add_marks()
    elif(select == '2'):
        display_info()
    else:
        print("Not a valid selection")
        break
        

        
session.close()
