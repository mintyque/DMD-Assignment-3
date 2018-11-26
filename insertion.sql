SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE available_part;
TRUNCATE TABLE car;
TRUNCATE TABLE charging_station;
TRUNCATE TABLE charging_station_history;
TRUNCATE TABLE customer;
TRUNCATE TABLE model;
TRUNCATE TABLE order_history;
TRUNCATE TABLE part;
TRUNCATE TABLE provider;
TRUNCATE TABLE workshop;
TRUNCATE TABLE workshop_history;

# Models
INSERT INTO model(model_name, capacity_of_charge,model_type, capacity_of_people, plugs_size, plugs_shape)
VALUES("XIOMI", 100, "Business", 6, 25, "Triangle");

INSERT INTO model(model_name, capacity_of_charge,model_type, capacity_of_people, plugs_size, plugs_shape)
VALUES("HONDA_3", 100, "Econom", 3, 30, "Square");

INSERT INTO model(model_name, capacity_of_charge,model_type, capacity_of_people, plugs_size, plugs_shape)
VALUES("HONDA_6", 100, "Econom", 6, 30, "Square");

INSERT INTO model(model_name, capacity_of_charge,model_type, capacity_of_people, plugs_size, plugs_shape)
VALUES("Ferrari", 100, "Business", 1, 50, "Triangle");

INSERT INTO model(model_name, capacity_of_charge,model_type, capacity_of_people, plugs_size, plugs_shape)
VALUES("VOLGA", 100, "SuperEconom", 4, 30, "Square");

# Cars
INSERT INTO car(color, plate_number, model_name)
VALUES("Pink", "AN770E", "XIOMI");

INSERT INTO car(color, plate_number, model_name)
VALUES("Red", "AN771E", "VOLGA");

INSERT INTO car(color, plate_number, model_name)
VALUES("Black", "AB772E", "HONDA_3");

INSERT INTO car(color, plate_number, model_name)
VALUES("Yellow", "AB773E", "Ferrari");

INSERT INTO car(color, plate_number, model_name)
VALUES("Blue", "AB774E", "VOLGA");

INSERT INTO car(color, plate_number, model_name)
VALUES("Purple", "AN775E", "HONDA_3");

INSERT INTO car(color, plate_number, model_name)
VALUES("Indigo", "AB776E", "VOLGA");

INSERT INTO car(color, plate_number, model_name)
VALUES("Blue", "AB777E", "VOLGA");

INSERT INTO car(color, plate_number, model_name)
VALUES("Red", "AB778E", "HONDA_6");

INSERT INTO car(color, plate_number, model_name)
VALUES("Orange", "AB779E", "HONDA_6");


# Charging stations
INSERT INTO charging_station(address, amount_of_available_sockets, plugs_shape, plugs_size, time_of_charging, price)
VALUES("Universitetskya 1", 2, "Square", 30, 35, 250);

INSERT INTO charging_station(address, amount_of_available_sockets, plugs_shape, plugs_size,time_of_charging, price)
VALUES("Universitetskya 2", 4, "Triangle", 50, 25, 900); 

INSERT INTO charging_station(address, amount_of_available_sockets, plugs_shape, plugs_size,time_of_charging, price)
VALUES("Universitetskya 3", 6, "Square", 25, 30, 300); 


#Charging station history
INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(1, 1, "2018-01-14 12:06:23", 400);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(2, 2, "2018-03-04 09:36:43", 200);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(3, 1, "2018-05-24 07:52:30" , 100);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(7, 2, "2018-02-16 09:36:43", 600);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(5, 1, "2018-09-27 02:12:11", 600);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(1, 1, "2018-01-14 01:06:23", 400);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(3, 2, "2018-01-14 01:06:23", 400);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(3, 1, "2018-01-14 15:06:23", 400);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(3, 1, "2018-11-14 15:06:23", 400);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(3, 2, "2018-11-05 01:06:23", 400);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(3, 2, "2018-11-10 01:06:23", 400);

INSERT INTO charging_station_history(car_id, charging_station_id, charging_date, price)
VALUES(1, 1, "2018-10-30 12:06:23", 400);

# Customers
INSERT INTO customer(username, email, fullname, address, phone_number)
VALUES("worker1230","worker1230@gmail.com", "Florence Vidassi", "Universiteskaya 1", "+7(909)-204-333-44-10");

INSERT INTO customer(username, email, fullname, address, phone_number)
VALUES("worker1231","worker1231@gmail.com", "Evgeniy Zurich", "Universiteskaya 2", "+7(909)-214-333-46-92");

INSERT INTO customer(username, email, fullname, address, phone_number)
VALUES("worker1232","worker1232@gmail.com", "Albert Bovaria", "Universiteskaya 3", "+7(909)-204-333-45-12");

INSERT INTO customer(username, email, fullname, address, phone_number)
VALUES("worker1233","worker1233@gmail.com", "Giancarllo Osi", "Universiteskaya 4", "+7(909)-224-343-44-12");

INSERT INTO customer(username, email, fullname, address, phone_number)
VALUES("worker1234","worker1234@gmail.com", "Mazzara Assignment", "Universiteskaya 5", "+7(909)-224-334-47-11");

INSERT INTO customer(username, email, fullname, address, phone_number)
VALUES("worker1235","worker1235@gmail.com", "Shilov LetMeTellYouStory", "Universiteskaya 6", "+7(909)-224-333-40-15");


# order_history
INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(1, 2, "2018-11-23 08:32:23", "2018-11-23 19:32:43", "2018-11-23 20:32:23", 100, "Levobulachnaya 1", "Pravobulachnaya 1", 128);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(1, 2, "2018-11-23 09:32:23", "2018-11-23 20:32:43", "2018-11-23 23:32:23", 100, "Levobulachnaya 1", "Pravobulachnaya 1", 128);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(2, 3, "2018-11-23 09:33:23", "2018-11-23 19:37:23", "2018-11-23 20:32:23", 250, "Levobulachnaya 2", "Pravobulachnaya 2", 428);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(3, 1, "2018-11-23 18:34:23", "2018-11-23 19:35:23", "2018-11-23 20:32:23", 55, "Levobulachnaya 3", "Pravobulachnaya 3", 278);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(3, 3, "2018-11-23 15:35:23", "2018-11-23 19:33:23", "2018-11-23 12:32:23", 75, "Levobulachnaya 4", "Pravobulachnaya 4", 238);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(5, 4, "2018-11-23 17:32:23", "2018-11-23 19:42:23", "2018-11-24 09:32:23", 225, "Levobulachnaya 5", "Pravobulachnaya 5", 2018);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(3, 3, "2018-11-23 18:32:23", "2018-11-23 19:22:23", "2018-11-23 22:32:23", 285, "Levobulachnaya 6", "Pravobulachnaya 6", 1228);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(4, 3, "2018-11-23 19:32:23", "2018-11-23 19:12:23", "2018-11-23 23:32:23", 394, "Levobulachnaya 7", "Pravobulachnaya 7", 542);

INSERT INTO order_history(customer_id, car_id, date_accept, date_pickup_customer, date_finished, travel_destination_distance, pickup_location, travel_destination, pickup_location_distance)
VALUES(4, 3, "2018-11-23 19:32:23", "2018-11-23 19:12:23", "2018-11-23 23:32:23", 394, "Levobulachnaya 7", "Pravobulachnaya 7", 542);


# Workshop
INSERT INTO workshop(address, available_time_start,available_time_end)
VALUES("Street 1", 9, 18);

INSERT INTO workshop(address, available_time_start,available_time_end)
VALUES("Street 2", 7, 15);

INSERT INTO workshop(address, available_time_start,available_time_end)
VALUES("Street 3", 0, 24);

# Workshop history
INSERT INTO workshop_history(part_id, reparing_date, workshop_id)
VALUES("1", "2018-11-23 00:15:15", "1");

INSERT INTO workshop_history(part_id, reparing_date, workshop_id)
VALUES("1", "2018-11-10 05:30:00", "3");

INSERT INTO workshop_history(part_id, reparing_date, workshop_id)
VALUES("2", "2018-01-20 14:00:00", "2");

INSERT INTO workshop_history(part_id, reparing_date, workshop_id)
VALUES("3", "2018-11-20 18:00:01", "2");

INSERT INTO workshop_history(part_id, reparing_date, workshop_id)
VALUES("3", "2018-11-20 18:00:01", "2");

# Provider
INSERT INTO provider(address,phone_number)
VALUES("Street 15", "89090937432");

INSERT INTO provider(address,phone_number)
VALUES("Street 16", "89090947639");


# Part
INSERT INTO part(part_name,price)
VALUES("Front", 13000);

INSERT INTO part(part_name,price)
VALUES("Side", 11000);

INSERT INTO part(part_name,price)
VALUES("Back", 9000);


# Available part
INSERT INTO available_part(workshop_id, provider_id, amount, part_id)
VALUES(null, 1, 50, 1);

INSERT INTO available_part(workshop_id, provider_id,amount,part_id)
VALUES(1, null, 20, 2);

SET FOREIGN_KEY_CHECKS = 1;