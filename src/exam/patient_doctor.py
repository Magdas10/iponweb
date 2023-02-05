import date_and_time
from copy import deepcopy


class PatientError(Exception):
    pass


class Patient:
    def __init__(self, name, surname, age, gender):
        if isinstance(name, str):
            self.__name = name
        else:
            raise PatientError("wrong input for name")
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise PatientError("wrong input for surname")
        if isinstance(age, int) and 18 <= age <= 100:
            self.__age = age
        else:
            raise PatientError("wrong input for age")
        if gender == 'M' or gender == 'F':
            self.__gender = gender
        else:
            raise PatientError("wrong input for gender")

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    def __repr__(self):
        return f"{self.__name} {self.__surname} - {self.__gender}, {self.__age} years old"

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname and self.age == other.age and self.gender == other.gender

    def __ne__(self, other):
        return not self == other


# print(patient1)
# print(patient1 == patient2)
# print(patient1 != patient2)
# print(patient1 == patient1)

class DoctorError(Exception):
    pass


class Doctor:
    start = date_and_time.Time(9, 0, 0)
    end = date_and_time.Time(17, 0, 0)

    def __init__(self, name, surname):
        if isinstance(name, str):
            self.__name = name
        else:
            raise DoctorError("wrong input for name")
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise DoctorError("wrong input for surname")
        self.__schedule = {}

    def __repr__(self):
        sch = ""
        for d in self.__schedule:
            sch += d.__repr__() + " " + self.__schedule[d].__repr__() + '\n'

        return f"Doctor {self.__name} {self.__surname} schedule {sch}"

    @property
    def schedule(self):
        return self.__schedule

    def is_free(self, time):
        if isinstance(time, date_and_time.DateTime):
            for d in self.__schedule:
                if time >= d:
                    p = deepcopy(d)
                    p.add_minute(30)
                    if p >= time:
                        return False
            else:
                return True
        else:
            raise DoctorError("wrong input for time")

    def is_registered(self, patient):
        for d in self.__schedule:
            if self.__schedule[d] == patient:
                return True
            else:
                return False

    def register_patient(self, patient, time):
        if isinstance(time, date_and_time.DateTime) and isinstance(patient, Patient):
            if self.is_free(time) and not self.is_registered(patient):
                if Doctor.start <= time.time <= Doctor.end:
                    self.__schedule[time] = patient
                    print(f"Patient {patient} successfully registered at {time}")
                else:
                    print("work hours- 09:00-17:00")
            elif self.is_registered(patient):
                print(f"Patient {patient} already registered")
            else:
                print(f"Datetime {time} already taken from another patient")
        else:
            raise DoctorError("wrong input for patient or datetime")


doctor1 = Doctor("David", "Davidyan")
patient1 = Patient("Magda", "Gyurjyan", 21, 'F')
patient2 = Patient("Agnes", "Muradyan", 20, 'F')
patient3 = Patient("Ani", "Arzumanyan", 19, 'F')
doctor1.register_patient(patient1,
                         date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(10, 30, 30)))
doctor1.register_patient(patient2,
                         date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(11, 20, 30)))
print(doctor1)
print(doctor1.is_free(date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(11, 45, 30))))
print(doctor1.is_free(date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(10, 35, 30))))
print(doctor1.is_free(date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(11, 55, 30))))
print("-----------------------------")
print(doctor1.is_registered(patient1))
print(doctor1.is_registered(patient3))
print("-----------------------------")

doctor1.register_patient(patient1,
                         date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(10, 30, 30)))
doctor1.register_patient(patient3,
                         date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(10, 30, 30)))
doctor1.register_patient(patient3,
                         date_and_time.DateTime(date_and_time.Date(2022, 12, 24), date_and_time.Time(19, 30, 30)))
