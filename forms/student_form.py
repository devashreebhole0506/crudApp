class StudentForm:

    def __init__(self, form_data=None):
        self.form_data = form_data or {}
        self.errors = {}

    def is_valid(self):
        required_fields = [
            'name', 'address', 'mobile',
            'email', 'education', 'department', 'gender'
        ]

        for field in required_fields:
            if not self.form_data.get(field):
                self.errors[field] = f"{field} is required"

        if self.form_data.get('mobile') and not self.form_data['mobile'].isdigit():
            self.errors['mobile'] = "Mobile must be numeric"

        return len(self.errors) == 0

    def cleaned_data(self):
        return {
            "name": self.form_data.get('name'),
            "address": self.form_data.get('address'),
            "mobile": self.form_data.get('mobile'),
            "email_id": self.form_data.get('email'),  # ✅ FIXED
            "education": self.form_data.get('education'),
            "department": self.form_data.get('department'),
            "gender": self.form_data.get('gender')
        }