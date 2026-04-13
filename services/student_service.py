from models.student_model import StudentModel

class StudentService:

    @staticmethod
    def register_student(data):
        StudentModel.save_student(data)

    @staticmethod
    def get_students():
        return StudentModel.get_all_students()

    @staticmethod
    def get_student_by_id(student_id):
        return StudentModel.get_student_by_id(student_id)

    @staticmethod
    def delete_student_by_id(student_id):
        StudentModel.delete_student_by_id(student_id)

    @staticmethod
    def update_student(student_id, data):
        updated_data = {
            "name": data.get('name'),
            "address": data.get('address'),
            "mobile": data.get('mobile'),
            "email_id": data.get('email'),  # ✅ FIXED
            "education": data.get('education'),
            "department": data.get('department'),
            "gender": data.get('gender')
        }

        StudentModel.update_student(student_id, updated_data)