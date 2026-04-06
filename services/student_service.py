from models.student_model import StudentModel

class StudentService:

    @staticmethod
    def register_student(data):
        # You can add validation or business logic here
        if not data['name']:
            return {"error": "Name is required"}

        StudentModel.save_student(data)

        return {"message": "Student Registered Successfully"}
    
    @staticmethod
    def get_students():
        students = StudentModel.get_all_students()
        return students 