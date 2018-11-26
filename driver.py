import MySQLdb


def start(cursor):
    prompt = "Welcome to database. Choose table to work with by inputting a number.\n"
    prompt += "1: Car Models\n"
    prompt += "2: Cars\n"
    prompt += "3: Customers\n"
    prompt += "4: Charging Stations\n"
    prompt += "5: Workshops\n"
    prompt += "6: Car Parts\n"
    prompt += "7: Car Parts Providers\n"
    prompt += "8: Logs\n"
    prompt += "9: View test queries\n"
    prompt += "0: Exit\n"
    input_string = int(input(prompt))
    if input_string == 1:
        car_models(cursor)
    elif input_string == 2:
        cars(cursor)
    elif input_string == 3:
        customers(cursor)
    elif input_string == 4:
        charging_stations(cursor)
    elif input_string == 5:
        workshops(cursor)
    elif input_string == 6:
        car_parts(cursor)
    elif input_string == 7:
        print("Looking at Car Parts Providers")
    elif input_string == 8:
        print("Looking at Logs")
    elif input_string == 9:
        tests(cursor)
    elif input_string == 0:
        return 0


def tests(cursor):
    input_string = int(input("\nEnter test case number\nEnter 0 to go back to title screen\n"))
    if input_string == 1:
        cursor.execute("SELECT car_id FROM car WHERE color = 'Red' AND plate_number LIKE 'AN%';")
        for row in cursor.fetchall():
            print("Car ID", row[0])
        tests(cursor)
    elif input_string == 2:
        cursor.execute("SELECT hour(charging_date) as hour, COUNT(*) AS num_car FROM charging_station_history WHERE DATE(charging_date) = '2018-01-14' GROUP BY hour ORDER BY hour")
        array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for row in cursor.fetchall():
            array[row[0]] = row[1]
        for i in range(len(array)):
            print(i, "-", i+1, ": ", array[i])
    elif input_string == 3:
        cursor.execute("SELECT COUNT(*) FROM car")
        for row in cursor.fetchall():
            percent = row[0]
        cursor.execute("SELECT COUNT(*) FROM (SELECT COUNT(*) FROM order_history WHERE TIME(date_accept) <= '10:00:00' AND TIME(date_accept) >= '07:00:00' AND DATE(date_accept) <= '2018-11-23' AND DATE(date_accept) >= ADDDATE('2018-11-23', -7) GROUP BY car_id) as A UNION SELECT COUNT(*) FROM (SELECT COUNT(*) FROM order_history WHERE TIME(date_accept) <= '14:00:00' AND TIME(date_accept) >= '12:00:00' AND DATE(date_accept) <= '2018-11-23' AND DATE(date_accept) >= ADDDATE('2018-11-23', -7) GROUP BY car_id) as B UNION SELECT COUNT(*) FROM (SELECT COUNT(*) FROM order_history WHERE TIME(date_accept) <= '19:00:00' AND TIME(date_accept) >= '17:00:00' AND DATE(date_accept) <= '2018-11-23' AND DATE(date_accept) >= ADDDATE('2018-11-23', -7) GROUP BY car_id) as C;")
        morning, afternoon, evening = cursor.fetchall()
        print("Morning:", int(morning[0]*100/percent))
        print("Afternoon:", int(afternoon[0]*100/percent))
        print("Evening:", int(evening[0]*100/percent))
    elif input_string == 4:
        cursor.execute("SELECT customer_id, date_accept FROM order_history WHERE customer_id = 4 group by customer_id, date_accept having count(*) >1;")
        for row in cursor.fetchall():
            print("Customer ID:", row[0])
            print("Date of trip:", row[1])
    elif input_string == 5:
        cursor.execute("SELECT AVG(pickup_location_distance) as average_distance, AVG(travel_destination_distance) as average_trip_duration FROM order_history")
        for row in cursor.fetchall():
            print("Average distance to client:", int(row[0]))
            print("Average distance to destination:", int(row[1]))
    elif input_string == 6:
        print("sorry")
        start(cursor)
    elif input_string == 7:
        cursor.execute("SELECT COUNT(*) FROM car")
        percent = 0
        for row in cursor.fetchall():
            percent = round(row[0]*0.1)
        foo = cursor.execute("SELECT car.car_id, COUNT(*) as num FROM car LEFT JOIN order_history ON order_history.car_id = car.car_id WHERE date_accept <= '2018-12-23' AND date_accept >= ADDDATE('2018-12-23', INTERVAL -3 MONTH) group by car.car_id order by num LIMIT %s;", (percent,))
        print(foo);
        print("Worst performing 10%:")
        for row in cursor.fetchall():
            print("Car ID", row[0])
    elif input_string == 8:
        print("sorry")
        start(cursor);
    elif input_string == 9:
        print("sorry")
        start(cursor)
    elif input_string == 10:
        print("sorry")
        start(cursor)
    elif input_string == 0:
        start(cursor)


def car_models(cursor):
    prompt = "\nBrowsing Car Models table. Choose your action.\n"
    prompt += "1: View entire table\n"
    prompt += "2: Perform a SELECT query\n"
    prompt += "0: Go back to title screen\n"
    input_string = int(input(prompt))
    if input_string == 1:
        cursor.execute("SELECT * FROM model")
        print("Name", "Charge cap.", "Class", "Seats", "Plug size", "Plug shape")
        for row in cursor.fetchall():
            print(" | ".join(str(elem) for elem in row))
        car_models(cursor)
    elif input_string == 2:
        prompt = "Choose attribute to SELECT\n"
        prompt += "1: Name\n"
        prompt += "2: Charge capacity\n"
        prompt += "3: Class\n"
        prompt += "4: Seats\n"
        prompt += "5: Plug size\n"
        prompt += "6: Plug shape\n"
        prompt += "0: Go back\n"
        input_string = int(input(prompt))
        if input_string == 1:
            input_string = str(input("Enter the name\n"))
            rows = cursor.execute("SELECT * FROM model WHERE model_name = %s", (input_string, ))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_models(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_models(cursor)
        elif input_string == 2:
            input_string = int(input("Enter charge capacity\n"))
            rows = cursor.execute("SELECT * FROM model WHERE capacity_of_charge = %s", (input_string, ))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_models(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_models(cursor)
        elif input_string == 3:
            input_string = str(input("Enter car class\n"))
            rows = cursor.execute("SELECT * FROM model WHERE model_type = %s", (input_string, ))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_models(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_models(cursor)
        elif input_string == 4:
            input_string = str(input("Enter number of seats\n"))
            rows = cursor.execute("SELECT * FROM model WHERE capacity_of_people = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_models(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_models(cursor)
        elif input_string == 5:
            input_string = str(input("Enter size of plug\n"))
            rows = cursor.execute("SELECT * FROM model WHERE plugs_size = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_models(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_models(cursor)
        elif input_string == 6:
            input_string = str(input("Enter shape of plug\n"))
            rows = cursor.execute("SELECT * FROM model WHERE plugs_shape = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_models(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_models(cursor)
        elif input_string == 0:
            car_models(cursor)
    elif input_string == 0:
        start(cursor)


def cars(cursor):
    prompt = "\nBrowsing Cars table. Choose your action.\n"
    prompt += "1. View entire table\n"
    prompt += "2. Perform a SELECT query\n"
    prompt += "0: Go back to title screen\n"
    input_string = int(input(prompt))
    if input_string == 1:
        cursor.execute("SELECT * FROM car")
        print("ID", "Color", "Plates", "Model")
        for row in cursor.fetchall():
            print(" | ".join(str(elem) for elem in row))
        cars(cursor)
    elif input_string == 2:
        prompt = "\nChoose attribute to SELECT\n"
        prompt += "1: ID\n"
        prompt += "2: Color\n"
        prompt += "3: Plates\n"
        prompt += "4: Model\n"
        prompt += "0: Go back\n"
        input_string = int(input(prompt))
        if input_string == 1:
            input_string = int(input("Enter car ID\n"))
            rows = cursor.execute("SELECT * FROM car WHERE car_id = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                cars(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                cars(cursor)
        elif input_string == 2:
            input_string = str(input("Enter car color\n"))
            rows = cursor.execute("SELECT * FROM car WHERE color = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                cars(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                cars(cursor)
        elif input_string == 3:
            input_string = str(input("Enter plates number (may be incomplete)\n"))
            rows = cursor.execute("SELECT * FROM car WHERE INSTR(plate_number, %s) > 0", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                cars(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                cars(cursor)
        elif input_string == 4:
            input_string = str(input("Enter car model\n"))
            rows = cursor.execute("SELECT * FROM car WHERE model_name = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                cars(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                cars(cursor)
        elif input_string == 0:
            cars(cursor)
    elif input_string == 0:
        start(cursor)


def customers(cursor):
    prompt = "\nBrowsing Customers table. Choose your action\n"
    prompt += "1: View entire table\n"
    prompt += "2: Perform a SELECT query\n"
    prompt += "0: Go back to title screen\n"
    input_string = int(input(prompt))
    if input_string == 1:
        cursor.execute("SELECT * FROM customer")
        print("ID", "Username", "e-Mail", "Full name", "Address", "Phone number")
        for row in cursor.fetchall():
            print(" | ".join(str(elem) for elem in row))
        customers(cursor)
    elif input_string == 2:
        prompt = "\nChoose attribute to SELECT\n"
        prompt += "1: ID\n"
        prompt += "2: Username\n"
        prompt += "3: e-Mail\n"
        prompt += "4: Name\n"
        prompt += "5: Address\n"
        prompt += "6: Phone Number\n"
        prompt += "0: Go back\n"
        input_string = int(input(prompt))
        if input_string == 1:
            input_string = int(input("Enter customer ID\n"))
            rows = cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                customers(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                customers(cursor)
        elif input_string == 2:
            input_string = str(input("Enter customer username\n"))
            rows = cursor.execute("SELECT * FROM customer WHERE username = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                customers(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                customers(cursor)
        elif input_string == 3:
            input_string = str(input("Enter customer e-Mail (may be incomplete)\n"))
            rows = cursor.execute("SELECT * FROM customer WHERE INSTR(email, %s) > 0", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                customers(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                customers(cursor)
        elif input_string == 4:
            input_string = str(input("Enter customer name (may be incomplete)\n"))
            rows = cursor.execute("SELECT * FROM customer WHERE INSTR(fullname, %s) > 0", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                customers(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                customers(cursor)
        elif input_string == 5:
            input_string = str(input("Enter customer address (may be incomplete)\n"))
            rows = cursor.execute("SELECT * FROM customer WHERE INSTR(address, %s) > 0", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                customers(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                customers(cursor)
        elif input_string == 6:
            input_string = str(input("Enter customer phone number (may be incomplete)\n"))
            rows = cursor.execute("SELECT * FROM customer WHERE INSTR(phone_number, %s) > 0", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                customers(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                customers(cursor)
        elif input_string == 0:
            customers(cursor)
    elif input_string == 0:
        start(cursor)


def charging_stations(cursor):
    prompt = "\nBrowsing Charging Stations table. Choose your action\n"
    prompt += "1: View entire table\n"
    prompt += "2: Perform a SELECT query\n"
    prompt += "0: Go back to title screen\n"
    input_string = int(input(prompt))
    if input_string == 1:
        cursor.execute("SELECT * FROM charging_station")
        print("ID", "Address", "Available sockets", "Plug shape", "Plug size", "Charging time", "Charging price")
        for row in cursor.fetchall():
            print(" | ".join(str(elem) for elem in row))
        charging_stations(cursor)
    elif input_string == 2:
        prompt = "\nChoose attribute to SELECT\n"
        prompt += "1: ID\n"
        prompt += "2: Address\n"
        prompt += "3: Available sockets\n"
        prompt += "4: Plug size\n"
        prompt += "5: Plug shape\n"
        prompt += "6: Charging time\n"
        prompt += "7: Charging price\n"
        prompt += "0: Go back\n"
        input_string = int(input(prompt))
        if input_string == 1:
            input_string = int(input("Enter charging station ID\n"))
            rows = cursor.execute("SELECT * FROM charging_station WHERE charging_station_id = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                charging_stations(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                charging_stations(cursor)
        if input_string == 2:
            input_string = str(input("Enter charging station address (may be incomplete)\n"))
            rows = cursor.execute("SELECT * FROM charging_station WHERE INSTR(address, %s) > 0", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                charging_stations(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                charging_stations(cursor)
        if input_string == 3:
            input_string = int(input("Enter number of available sockets\n"))
            rows = cursor.execute("SELECT * FROM charging_station WHERE amount_of_available_sockets = %s",
                                  (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                charging_stations(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                charging_stations(cursor)
        if input_string == 4:
            input_string = int(input("Enter size of plugs\n"))
            rows = cursor.execute("SELECT * FROM charging_station WHERE plugs_size = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                charging_stations(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                charging_stations(cursor)
        if input_string == 5:
            input_string = str(input("Enter shape of plugs\n"))
            rows = cursor.execute("SELECT * FROM charging_station WHERE plugs_shape = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                charging_stations(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                charging_stations(cursor)
        if input_string == 6:
            input_string = str(input("Enter shape of plugs\n"))
            rows = cursor.execute("SELECT * FROM charging_station WHERE plugs_shape = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                charging_stations(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                charging_stations(cursor)
        if input_string == 7:
            input_string = int(input("Enter charging price\n"))
            rows = cursor.execute("SELECT * FROM charging_station WHERE price = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                charging_stations(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                charging_stations(cursor)
        if input_string == 0:
            charging_stations(cursor)
    elif input_string == 0:
        start(cursor)


def workshops(cursor):
    prompt = "\nBrowsing Workshops table. Choose your action\n"
    prompt += "1: View entire table\n"
    prompt += "2: Perform a SELECT query\n"
    prompt += "0: Go back to title screen\n"
    input_string = int(input(prompt))
    if input_string == 1:
        cursor.execute("SELECT * FROM workshop")
        print("ID", "Address", "Available from", "Available to")
        for row in cursor.fetchall():
            print(" | ".join(str(elem) for elem in row))
        workshops(cursor)
    elif input_string == 2:
        prompt = "\nChoose attribute to SELECT\n"
        prompt += "1: ID\n"
        prompt += "2: Address\n"
        prompt += "0: Go back\n"
        input_string = int(input(prompt))
        if input_string == 1:
            input_string = int(input("Enter workshop ID\n"))
            rows = cursor.execute("SELECT * FROM workshop WHERE workshop_id = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                workshops(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                workshops(cursor)
        elif input_string == 2:
            input_string = str(input("Enter workshop address (may be incomplete)\n"))
            rows = cursor.execute("SELECT * FROM workshop WHERE INSTR(address, %s) > 0", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                workshops(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                workshops(cursor)
        elif input_string == 0:
            workshops(cursor)
    elif input_string == 0:
        start(cursor)


def car_parts(cursor):
    prompt = "\nBrowsing Car Parts table. Choose your action\n"
    prompt += "1: View entire table\n"
    prompt += "2: Perform SELECT query\n"
    prompt += "0: Go back to title screen\n"
    input_string = int(input(prompt))
    if input_string == 1:
        cursor.execute("SELECT * FROM part")
        print("ID", "Name", "Price")
        for row in cursor.fetchall():
            print(" | ".join(str(elem) for elem in row))
        car_parts(cursor)
    elif input_string == 2:
        prompt = "\nChoose attribute to SELECT\n"
        prompt += "1: ID\n"
        prompt += "2: Name\n"
        prompt += "0: Go back\n"
        input_string = int(input(prompt))
        if input_string == 1:
            input_string = int(input("Enter car part ID\n"))
            rows = cursor.execute("SELECT * FROM part WHERE part_id = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_parts(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_parts(cursor)
        elif input_string == 2:
            input_string = str(input("Enter car part name\n"))
            rows = cursor.execute("SELECT * FROM part WHERE part_name = %s", (input_string,))
            result = cursor.fetchall()
            if rows == 0:
                print("Nothing found")
                car_parts(cursor)
            else:
                for row in result:
                    print(" | ".join(str(elem) for elem in row))
                car_parts(cursor)
        elif input_string == 0:
            car_parts(cursor)
    elif input_string == 0:
        start(cursor)


db = MySQLdb.connect(host="localhost",  # your host все можно поменять ес чо
                     user="root",       # username
                     passwd="root",     # password
                     db="test")    # db name
cur = db.cursor()
start(cur)
