import arrow
from school.models import (
    ClassAttendance,
    ClassRoom,
    Department,
    Employees,
    StaffAttendance,
    StudentFee,
    Students,
    Subject,
    Tutor,
)
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


class Admitter:
    def add_department(self, name, role, head_name):
        try:
            dep = Department.objects.create(
                department_name=name, role=role, head_name=head_name
            )
            if dep:
                return JsonResponse(
                    {"success": True, "info": "Department added successfully"}
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "Unable to add department"}
                )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def get_departments(self):
        try:
            departments = Department.objects.all()
            if departments:
                return JsonResponse(
                    {"success": True, "data": list(departments.values())}
                )
            else:
                return JsonResponse({"success": False, "info": "No departments found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def update_department(self, department_id, name=None, role=None, head_name=None):
        try:
            dep = Department.objects.get(department_id=department_id)
            if not dep:
                return JsonResponse(
                    {"success": False, "info": "Department does not exist"}
                )

            if name is not None:
                dep.department_name = name
            if role is not None:
                dep.role = role
            if head_name is not None:
                dep.head_name = head_name

            dep.save()
            return JsonResponse(
                {"success": True, "info": "Department updated successfully"}
            )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def add_employee(self, fullname, department):
        try:
            emp = Employees.objects.create(full_name=fullname, department=department)
            if emp:
                return JsonResponse(
                    {"success": True, "info": "Employee added successfully"}
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "Unable to add employee"}
                )

        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def get_employees(self):
        try:
            employees = Employees.objects.all()
            if employees:
                return JsonResponse({"success": True, "data": list(employees.values())})
            else:
                return JsonResponse({"success": False, "info": "No employees found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def update_employee(self, employee_id, fullname=None, department=None, status=None):
        try:
            emp = Employees.objects.get(employee_id=employee_id)
            if not emp:
                return JsonResponse(
                    {"success": False, "info": "Employee does not exist"}
                )

            if fullname is not None:
                emp.full_name = fullname
            if department is not None:
                emp.department = department
            if status is not None:
                emp.status = status

            emp.save()
            return JsonResponse(
                {"success": True, "info": "Employee updated successfully"}
            )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def add_subjects(self, name, description):
        try:
            sub = Subject.objects.create(
                subject_name=name, subject_description=description
            )
            if sub:
                return JsonResponse(
                    {"success": True, "info": "Subject added successfully"}
                )
            else:
                return JsonResponse({"success": False, "info": "Unable to add subject"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def get_subjects(self):
        try:
            subjects = Subject.objects.all()
            if subjects:
                return JsonResponse({"success": True, "data": list(subjects.values())})
            else:
                return JsonResponse({"success": False, "info": "No subjects found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def update_subject(self, subject_id, name=None, description=None):
        try:
            sub = Subject.objects.get(id=subject_id)
            if not sub:
                return JsonResponse(
                    {"success": False, "info": "Subject does not exist"}
                )

            if name is not None:
                sub.subject_name = name
            if description is not None:
                sub.subject_description = description

            sub.save()
            return JsonResponse(
                {"success": True, "info": "Subject updated successfully"}
            )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def add_teacher(self, full_name, subjects, department_id):
        try:
            dep = Department.objects.get(department_id=department_id)
            if not dep:
                return JsonResponse(
                    {"success": False, "info": "Department does not exist"}
                )

            tutor = Tutor.objects.create(full_name=full_name, department=dep)

            # Add subjects to the tutor
            if isinstance(subjects, list):
                for subject_id in subjects:
                    subject = Subject.objects.get(id=subject_id)
                    tutor.subjects.add(subject)
            if isinstance(subjects, str):
                subject = Subject.objects.get(name=subjects)
                tutor.subjects.add(subject)

            return JsonResponse({"success": True, "info": "Tutor created successfully"})

        except Exception as e:
            logger.warning(str(e))
            return JsonResponse({"success": False, "info": "Kindly try again"})

    def get_tutors(self):
        try:
            tutors = Tutor.objects.all()
            if tutors:
                return JsonResponse({"success": True, "data": list(tutors.values())})
            else:
                return JsonResponse({"success": False, "info": "No tutors found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def update_tutor(self, tutor_id, full_name=None, subjects=None):
        try:
            tut = Tutor.objects.get(tutor_id=tutor_id)
            if not tut:
                return JsonResponse({"success": False, "info": "Tutor does not exist"})

            if full_name is not None:
                tut.full_name = full_name
            if subjects is not None:
                if isinstance(subjects, list):
                    tut.subjects.add(*subjects)
                else:
                    tut.subjects.add(subjects)

            tut.save()
            return JsonResponse({"success": True, "info": "Tutor updated successfully"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def add_classroom(self, teacher_id, grade, capacity):
        try:
            teach = Tutor.objects.get(tutor_id=teacher_id)
            if not teach:
                return JsonResponse({"success": False, "info": "Tutor does not exist"})

            classroom = ClassRoom.objects.create(
                teacher=teach, grade=grade, capacity=capacity
            )
            if classroom:
                return JsonResponse(
                    {"success": True, "info": "Classroom created successfully"}
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "Unable to create classroom"}
                )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def get_classrooms(self):
        try:
            classrooms = ClassRoom.objects.all()
            if classrooms:
                return JsonResponse(
                    {"success": True, "data": list(classrooms.values())}
                )
            else:
                return JsonResponse({"success": False, "info": "No classrooms found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def update_classroom(
        self, classroom_id, teacher_id=None, grade=None, capacity=None
    ):
        try:
            classroom = ClassRoom.objects.get(classroom_id=classroom_id)
            if not classroom:
                return JsonResponse(
                    {"success": False, "info": "Classroom does not exist"}
                )

            if teacher_id is not None:
                classroom.teacher = teacher_id
            if grade is not None:
                classroom.grade = grade
            if capacity is not None:
                classroom.capacity = capacity

            classroom.save()
            return JsonResponse(
                {"success": True, "info": "Classroom updated successfully"}
            )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def add_student(
        self, name, age, gender, address, classroom_id, parent_name, p_phone, p_email
    ):
        try:
            classroom = ClassRoom.objects.get(classroom_id=classroom_id)
            if not classroom:
                return JsonResponse(
                    {"success": False, "info": "Classroom does not exist"}
                )

            student = Students.objects.create(
                name=name,
                age=age,
                gender=gender,
                address=address,
                classroom=classroom,
                parent_name=parent_name,
                p_phone=p_phone,
                p_email=p_email,
            )
            if student:
                return JsonResponse(
                    {"success": True, "info": "Student created successfully"}
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "Unable to create student"}
                )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def get_students(self):
        try:
            students = Students.objects.all()
            if students:
                return JsonResponse({"success": True, "data": list(students.values())})
            else:
                return JsonResponse({"success": False, "info": "No students found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def update_student(
        self,
        student_id,
        name=None,
        age=None,
        gender=None,
        address=None,
        classroom_id=None,
        parent_name=None,
        p_phone=None,
        p_email=None,
        status=None,
    ):
        try:
            student = Students.objects.get(student_id=student_id)
            if not student:
                return JsonResponse(
                    {"success": False, "info": "Student does not exist"}
                )

            if name is not None:
                student.name = name
            if age is not None:
                student.age = age
            if gender is not None:
                student.gender = gender
            if address is not None:
                student.address = address
            if classroom_id is not None:
                student.classroom = classroom_id
            if parent_name is not None:
                student.parent_name = parent_name
            if p_phone is not None:
                student.parent_phone = p_phone
            if p_email is not None:
                student.parent_email = p_email
            if status is not None:
                student.status = status

            student.save()
            return JsonResponse(
                {"success": True, "info": "Student updated successfully"}
            )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def mark_class_attendance(self, student_id, class_room, status):
        try:
            student = Students.objects.get(student_id=student_id)
            if not student:
                return JsonResponse(
                    {"success": False, "info": "Student does not exist"}
                )

            class_room = ClassRoom.objects.get(classroom_id=class_room)
            if not class_room:
                return JsonResponse(
                    {"success": False, "info": "Classroom does not exist"}
                )

            now = arrow.now().datetime
            attendance = ClassAttendance.objects.create(
                student=student, class_room=class_room, date=now, status=status
            )
            if attendance:
                return JsonResponse(
                    {"success": True, "info": "Attendance marked successfully"}
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "Unable to mark attendance"}
                )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    # TODO:add an endpoint foe getting class attendance by the date

    def mark_staff_attendance(self, employee, department):
        try:
            employee = Employees.objects.get(employee_id=employee)
            if not employee:
                return JsonResponse(
                    {"success": False, "info": "Employee does not exist"}
                )

            department = Department.objects.get(department_id=department)
            if not department:
                return JsonResponse(
                    {"success": False, "info": "Department does not exist"}
                )

            now = arrow.now().datetime
            attendance = StaffAttendance.objects.create(
                employee=employee, department=department, date=now
            )
            if attendance:
                return JsonResponse(
                    {"success": True, "info": "Attendance marked successfully"}
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "Unable to mark attendance"}
                )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    # TODO:add the endpoints for the curriculum and timetable and also add the class for fee payments and stuff
