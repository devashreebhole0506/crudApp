from config import get_db_connection

class StudentModel:

    @staticmethod
    def save_student(data):
        db = get_db_connection()
        cursor = db.cursor()

        query = """
        INSERT INTO students 
        (name, address, mobile, email, education, gender)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data['name'],
            data['address'],
            data['mobile'],
            data['email'],
            data['education'],
            data['gender']
        )

        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()