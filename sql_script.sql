SET FOREIGN_KEY_CHECKS = 0;

create table if not exists model (
	model_name varchar(30) unique primary key,
    capacity_of_charge int not null,
    model_type varchar(30) not null,
    capacity_of_people int not null,
    plugs_size int not null,
    plugs_shape varchar(30) not null
);

create table if not exists car (
	car_id int auto_increment primary key,
	color varchar(30) not null,
	plate_number varchar(30) not null unique,
	model_name varchar(30) not null,
 
	foreign key(model_name) references model(model_name)
);

create table if not exists customer(
	customer_id int auto_increment primary key,
	username varchar(30) not null unique,
    email varchar(30) not null unique,
    fullname varchar(30) not null,
    address  varchar(30),
    phone_number varchar(30) not null
); 

create table if not exists charging_station(
	charging_station_id int auto_increment primary key,
	address varchar(30) not null unique,
    amount_of_available_sockets int not null,
	plugs_shape varchar(30) not null,
    plugs_size varchar(30) not null,
    time_of_charging int not null,
    price int not null
);

create table if not exists charging_station_history(
	car_id int not null,
    charging_station_id int not null,
    charging_date datetime not null,
    price int not null,
    
    foreign key(car_id) references car(car_id),
    foreign key(charging_station_id) references charging_station(charging_station_id)
);

create table if not exists order_history(
    customer_id int not null,
    car_id int not null,
    date_accept datetime not null,
    date_pickup_customer datetime not null,
    date_finished datetime not null,
    travel_destination_distance int not null,
    travel_destination varchar(30) not null,
    pickup_location_distance int not null,
    pickup_location varchar(30) not null,
    
    foreign key(customer_id) references customer(customer_id),
    foreign key(car_id) references car(car_id) 
);

create table if not exists part(
	part_id int auto_increment unique primary key,
    part_name varchar(30) not null unique,
    price int not null
);

SELECT pickup_location, COUNT(*) as num FROM order_history WHERE DATE(date_accept)='2018-11-23' AND TIME(date_accept) <= '10:00:00' AND TIME(date_accept) >= '07:00:00'  GROUP BY pickup_location ORDER BY num LIMIT 3;
SELECT travel_destination, COUNT(*) as num FROM order_history WHERE DATE(date_accept)='2018-11-23' AND TIME(date_accept) <= '10:00:00' AND TIME(date_accept) >= '07:00:00' GROUP BY travel_destination ORDER BY num LIMIT 3;

create table if not exists workshop(
	workshop_id int auto_increment primary key,
	address  varchar(30) not null unique,
    available_time_start int not null,
	available_time_end int not null
);

create table if not exists workshop_history(
	part_id int not null,
    reparing_date datetime not null,
    workshop_id int not null,

    foreign key(workshop_id) references workshop(workshop_id),
    foreign key(part_id) references part(part_id)
);

create table if not exists provider(
	provider_id int auto_increment primary key,
    address varchar(30) not null unique,
    phone_number varchar(30) not null unique
);

create table if not exists available_part(
	workshop_id int,
    provider_id int,
    amount int,
	part_id int not null unique,
    
    foreign key(part_id) references part(part_id),
    foreign key(workshop_id) references workshop(workshop_id),
    foreign key(provider_id) references provider(provider_id)
);
