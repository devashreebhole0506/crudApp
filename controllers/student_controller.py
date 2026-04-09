from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from services.student_service import StudentService

student_bp = Blueprint('student', __name__)

# Form
@student_bp.route('/')
def form():
    return render_template('form.html')


# Create Student
@student_bp.route('/api/students', methods=['POST'])
def create_student():

    data = {
        "name": request.form['name'],
        "address": request.form['address'],
        "mobile": request.form['mobile'],
        "email_id": request.form['email_id'],
        "education": request.form['education'],
        "gender": request.form['gender']
    }

    StudentService.register_student(data)
    return redirect(url_for('student.show_students'))


# Show Students
@student_bp.route('/students')
def show_students():
    students = StudentService.get_students()
    return render_template('students.html', students=students)


# DELETE (FIXED)
@student_bp.route('/students/<int:student_id>/delete')
def delete_student(student_id):
    StudentService.delete_student_by_id(student_id)
    return redirect(url_for('student.show_students'))


# EDIT PAGE (FIXED)
@student_bp.route('/students/<int:student_id>/edit')
def edit_student(student_id):
    student = StudentService.get_student_by_id(student_id)
    return render_template('edit.html', student=student)


# UPDATE (NEW)
@student_bp.route('/students/<int:student_id>/update', methods=['POST'])
def update_student(student_id):
    data = request.form
    StudentService.update_student(student_id, data)
    return redirect(url_for('student.show_students'))