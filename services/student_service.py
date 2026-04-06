from models.student_model import StudentModel

class StudentService:

    @staticmethod
    def register_student(data):
        if not data['name']:
            return {"error": "Name is required"}

        StudentModel.save_student(data)

        return {"message": "Student Registered Successfully"}

    @staticmethod
    def get_students():
        return StudentModel.get_all_students()