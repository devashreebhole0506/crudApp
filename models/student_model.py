from conf import get_db_connection

class StudentModel:

    @staticmethod
    def save_student(data):
        db = get_db_connection()
        cursor = db.cursor()

        query = """
        INSERT INTO students 
        (name, address, mobile, email_id, education, gender)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data['name'],
            data['address'],
            data['mobile'],
            data['email_id'],
            data['education'],
            data['gender']
        )

        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()

    @staticmethod
    def get_all_students():
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        cursor.close()
        db.close()

        return students
    @staticmethod
    def get_student_by_id(student_id):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()

        cursor.close()
        db.close()

        return student
    
    @staticmethod
    def delete_student_by_id(student_id):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        db.commit()

        cursor.close()
        db.close()

        return {"message": "Student Deleted Successfully"}
    
    @staticmethod
    def update_student(student_id, data):
        db = get_db_connection()
        cursor = db.cursor()

        query = "UPDATE students SET name = %s, address = %s, mobile = %s, email_id = %s, education = %s, gender = %s WHERE id = %s"
        values = (
            data['name'],
            data['address'],
            data['mobile'],
            data['email_id'],
            data['education'],
            data['gender'],
            student_id
        )
        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()

        return {"message": "Student Updated Successfully"}