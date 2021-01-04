import mysql.connector as sq


def connection():
    try:
        con = sq.connect(host="localhost", user="py", password="python123", database="hospital_management_system")
        if not con.is_connected():
            print("database not connected")
        else:
            return con
    except sq.Error as er:
        print(er)


def insertion():
    try:
        con = connection()
        cur = con.cursor()
        name = input("enter name of doctors")
        id = int(input("enter id of doctors"))
        age = int(input("enter age of doctors"))
        date_of_birth = input("enter date of birth of doctors")
        mobile_no = input("enter mobile no of doctors")
        specialization = input("enter specialization of doctors")
        fees = int(input("enter fees of doctors"))
        years_of_experience = int(input("enter years of experience"))
        cur.execute(
            "insert into doctors(name,id,age,date_of_birth,mobile_no,specialization,fees,years_of_experience)values('%s'"
            ",%d,%d,'%s','%s','%s',%d,%d)" % (name, id, age, date_of_birth, mobile_no, specialization,
                                              fees, years_of_experience))
        print()
        print("data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)


def display():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from doctors")
        for i in cur.fetchall():
            print(i)
    except sq.Error as er:
        print(er)


def updating():
    try:
        con = connection()
        cur = con.cursor()
        name = input("enter name of doctors")
        id = int(input("enter id of doctors"))
        age = int(input("enter age of doctors"))
        date_of_birth = input("enter date of birth of doctors")
        mobile_no = input("enter mobile no of doctors")
        specialization = input("enter specialization of doctors")
        fees = int(input("enter fees of doctors"))
        years_of_experience = int(input("enter years of experience"))
        cur.execute(
            "update doctors set name='%s',age=%d, date_of_birth='%s', mobile_no='%s', specialization='%s', "
            "fees=%d,years_of_experience=%d where id= %d" % (name, age, date_of_birth, mobile_no, specialization, fees,
                                                             years_of_experience, id))
        print()
        con.commit()
        print("data updated successfully")
    except sq.Error as er:
        print(er)


def deletion():
    try:
        con = connection()
        cur = con.cursor()
        id = int(input("enter id of doctors whose record you want to delete \nEnter id"))
        cur.execute("delete from doctors where id= %d" % id)
        print()
        con.commit()
        print("Data Deleted successfully")
    except sq.Error as er:
        print(er)


def insertion1():
    try:
        con = connection()
        cur = con.cursor()
        patient_ID = int(input("enter id of patients"))
        name = input("enter name of patients")
        age = int(input("enter age of patients"))
        gender = input("enter gender of patients")
        address = input("enter address of patients")
        contact_no = input("enter contact no of patients")
        date_of_birth = input("enter date of birth of patients")
        consultant_name = input("enter consultant name of patients")
        date_of_consultancy = input("enter date of consultancy of patients")
        department = input("enter department of patients")
        consultancy_fees = int(input("enter consultancy fees of patients"))
        cur.execute(
            "insert into patients( patient_ID,name,age,gender,address,contact_no,date_of_birth,consultant_name,"
            "date_of_consultancy,department,consultancy_fees)values(%d,'%s',%d,'%s','%s','%s','%s','%s','%s','%s',%d)"
            % (patient_ID, name, age, gender, address, contact_no, date_of_birth, consultant_name, date_of_consultancy,
                department, consultancy_fees))
        print()
        print("data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)


def display1():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from patients")
        for i in cur.fetchall():
            print(i)
    except sq.Error as er:
        print(er)


def updating1():
    try:
        con = connection()
        cur = con.cursor()

        patient_ID = int(input("enter id of patients"))
        name = input("enter name of patients")
        age = int(input("enter age of patients"))
        gender = input("enter gender of patients")
        address = input("enter address of patients")
        contact_no = input("enter contact no of patients")
        date_of_birth = input("enter date of birth of patients")
        consultant_name = input("enter consultant name of patients")
        date_of_consultancy = input("enter date of consultancy of patients")
        department = input("enter department of patients")
        consultancy_fees = int(input("enter consultancy fees of patients"))
        cur.execute(
            "update patients set name='%s',age=%d ,gender='%s',address='%s',contact_no='%s',date_of_birth='%s',"
            "consultant_name='%s',date_of_consultancy='%s',department='%s',consultancy_fees=%d where patient_ID= %d" % (
                name, age, gender, address, contact_no, date_of_birth, consultant_name, date_of_consultancy, department,
                consultancy_fees, patient_ID))
        print()
        con.commit()
        print("data updated successfully")
    except sq.Error as er:
        print(er)


def deletion1():
    try:
        con = connection()
        cur = con.cursor()
        patient_ID = int(input("enter id of patients whose record you want to delete \nEnter id"))
        cur.execute("delete from patients where patient_ID= %d" % patient_ID)
        print()
        con.commit()
        print("Data Deleted successfully")
    except sq.Error as er:
        print(er)


def insertion2():
    try:
        con = connection()
        cur = con.cursor()
        room_no = int(input("enter room no"))
        room_type = input("enter room type")
        room_charges_per_day = int(input("enter room charges per day"))
        room_status = input("enter room status")
        patient_name = input("enter patient name")
        cur.execute(
            "insert into room_info(room_no, room_type, room_charges_per_day, room_status, patient_name )values"
            "(%d,'%s',%d,'%s','%s')" % (room_no, room_type, room_charges_per_day, room_status, patient_name))
        print()
        print("data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)


def display2():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from room_info")
        for i in cur.fetchall():
            print(i)
    except sq.Error as er:
        print(er)


def updating2():
    try:
        con = connection()
        cur = con.cursor()
        room_no = int(input("enter room no"))
        room_type = input("enter room type")
        room_charges_per_day = int(input("enter room charges per day"))
        room_status = input("enter room status")
        patient_name = input("enter patient name of occupied room")
        cur.execute(
            "update Room_Info set room_type='%s',room_charges_per_day=%d,room_status='%s',patient_name='%s'where "
            "room_no= %d" % (room_type, room_charges_per_day, room_status, patient_name, room_no))
        print()
        con.commit()
        print("data updated successfully")
    except sq.Error as er:
        print(er)


def deletion2():
    try:
        con = connection()
        cur = con.cursor()
        room_no = int(input("enter room no from Room_Info whose record you want to delete \nEnter room no"))
        cur.execute("delete from Room_Info where room_no= %d" % room_no)
        print()
        con.commit()
        print("Data Deleted successfully")
    except sq.Error as er:
        print(er)


def insertion3():
    try:
        con = connection()
        cur = con.cursor()
        bill_no = int(input("enter bill no"))
        bill_date = input("enter bill date")
        name = input("enter name")
        room_type = input("enter room type")
        room_charges = int(input("enter room charges"))
        pathology_fees = int(input("enter pathology fees"))
        doctor_fees = int(input("enter doctor fees"))
        total_amount = int(input("enter total amount of bill"))
        cur.execute(
            "insert into bill_details( bill_no, bill_date, name ,room_type, room_charges, pathology_fees, doctor_fees, "
            "total_amount )values(%d,'%s','%s','%s',%d,%d,%d,%d)" % (bill_no, bill_date, name, room_type, room_charges,
                                                                     pathology_fees, doctor_fees, total_amount))
        print()
        print("data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)


def display3():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from bill_details")
        for i in cur.fetchall():
            print(i)
    except sq.Error as er:
        print(er)


def updating3():
    try:
        con = connection()
        cur = con.cursor()
        bill_no = int(input("enter bill no"))
        bill_date = input("enter bill date")
        name = input("enter name")
        room_type = input("enter room type")
        room_charges = int(input("enter room charges"))
        pathology_fees = int(input("enter pathology fees"))
        doctor_fees = int(input("enter doctor fees"))
        total_amount = int(input("enter total amount of bill"))
        cur.execute(
            "update bill_details set bill_date='%s', name='%s', room_type='%s', room_charges=%d, pathology_fees=%d, "
            "doctor_fees=%d, total_amount=%d where bill_no= %d" % (
                bill_date, name, room_type, room_charges, pathology_fees, doctor_fees, total_amount, bill_no))
        print()
        con.commit()
        print("data updated successfully")
    except sq.Error as er:
        print(er)


def deletion3():
    try:
        con = connection()
        cur = con.cursor()
        bill_no = int(input("enter bill no from bil_ details whose record you want to delete \nEnter bill no"))
        cur.execute("delete from bill_details where bill_no= %d" % bill_no)
        print()
        con.commit()
        print("Data Deleted successfully")
    except sq.Error as er:
        print(er)


def menu():
    try:
        print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
        print()
        print("Select Your Choice From The Given Alternatives")
        print()
        print(
            "1.Add Record Of Doctors\n2.Update Record Of Existing Doctors\n3.Delete Record Of Doctors\n4.Access All The "
            "Records Of Doctors\n5.Add Record Of patients\n6.Update Record Of Existing patients\n7.Delete Record Of "
            "patients\n8.Access All The Records Of patients\n9.Add Record Of room info\n10.Update Record Of Existing "
            "room info\n11.Delete Record Of room info\n12.Access All The Records Of room info\n13.Add Records Of bill "
            "details\n14.Update Record Of Existing bill details\n15.Delete Record Of bill details\n16.Access All The "
            "Records Of bill details")
        a = input("Enter Your Choice")
        if a == '1':
            insertion()
            print()
            print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
            a = input("Enter Your Choice")
            if a == 'Yes':
                insertion()
            else:
                print("Okay")
        elif a == '2':
            display()
            print()
            updating()
            print()
            print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
            b = input("Enter Your Choice")
            if b == 'Yes':
                updating()
            else:
                print("Okay")
        elif a == '3':
            display()
            print()
            deletion()
            print()
            print("Do You Want To Delete More Records")
            c = input("Enter Your Choice")
            if c == 'Yes':
                deletion()
            else:
                print("okay")
        elif a == '4':
            display()
        elif a == '5':
            insertion1()
            print()
            print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
            d = input("Enter Your Choice")
            if d == 'Yes':
                insertion1()
            else:
                print("Okay")
        elif a == '6':
            display1()
            print()
            updating1()
            print()
            print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
            e = input("Enter Your Choice")
            if e == 'Yes':
                updating1()
            else:
                print("Okay")
        elif a == '7':
            display1()
            print()
            deletion1()
            print()
            print("Do You Want To Delete More Records")
            f = input("Enter Your Choice")
            if f == 'Yes':
                deletion1()
            else:
                print("okay")
        elif a == '8':
            display1()
        elif a == '9':
            insertion2()
            print()
            print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
            g = input("Enter Your Choice")
            if g == 'Yes':
                insertion2()
            else:
                print("Okay")
        elif a == '10':
            display2()
            print()
            updating2()
            print()
            print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
            h = input("Enter Your Choice")
            if h == 'Yes':
                updating2()
            else:
                print("Okay")
        elif a == '11':
            display2()
            print()
            deletion2()
            print()
            print("Do You Want To Delete More Records")
            i = input("Enter Your Choice")
            if i == 'Yes':
                deletion2()
            else:
                print("okay")
        elif a == '12':
            display2()
        if a == '13':
            insertion3()
            print()
            print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
            j = input("Enter Your Choice")
            if j == 'Yes':
                insertion3()
            else:
                print("Okay")
        elif a == '14':
            display3()
            print()
            updating3()
            print()
            print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
            k = input("Enter Your Choice")
            if k == 'Yes':
                updating3()
            else:
                print("Okay")
        elif a == '15':
            display3()
            print()
            deletion3()
            print()
            print("Do You Want To Delete More Records")
            l = input("Enter Your Choice")
            if l == 'Yes':
                deletion3()
            else:
                print("okay")
        elif a == '16':
            display3()
    except sq.Error as er:
        print(er)


menu()
while input('Do You want to Continue(y for yes)') == 'y':
    menu()
