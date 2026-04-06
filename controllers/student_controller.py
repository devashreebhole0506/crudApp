from flask import Blueprint, request, jsonify, render_template
from services.student_service import StudentService

student_bp = Blueprint('student', __name__)

@student_bp.route('/')
def form():
    return render_template('form.html')


@student_bp.route('/api/students', methods=['POST'])
def create_student():

    data = {
        "name": request.form['name'],
        "address": request.form['address'],
        "mobile": request.form['mobile'],
        "email": request.form['email'],
        "education": request.form['education'],
        "gender": request.form['gender']
    }

    result = StudentService.register_student(data)

    return jsonify(result)


@student_bp.route('/api/getstudents', methods=['GET'])
def get_students():   # ✅ renamed function

    students_list = StudentService.get_students()

    return jsonify(students_list)