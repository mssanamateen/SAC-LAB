def student_info(**kwargs):
    print("Student Information:")
    for label in kwargs:          
        print(label, "=", kwargs[label])


student_info(name="Alamdar", rollno=92, course="SAC")
student_info(name="Vedanth", rollno=97)
student_info(name="zaid", course="SAC")
