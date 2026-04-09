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

    @staticmethod
    def get_student_by_id(student_id):
        return StudentModel.get_student_by_id(student_id)

    @staticmethod
    def delete_student_by_id(student_id):
        StudentModel.delete_student_by_id(student_id)
        return {"message": "Student Deleted Successfully"}

    @staticmethod
    def update_student(student_id, data):
        student = StudentModel.get_student_by_id(student_id)

        if not student:
            return {"error": "Student not found"}

        updated_data = {
            "name": data.get('name', student['name']),
            "address": data.get('address', student['address']),
            "mobile": data.get('mobile', student['mobile']),
            "email_id": data.get('email_id', student['email_id']),
            "education": data.get('education', student['education']),
            "gender": data.get('gender', student['gender'])
        }

        # ✅ IMPORTANT FIX
        StudentModel.update_student(student_id, updated_data)

        return {"message": "Student Updated Successfully"}