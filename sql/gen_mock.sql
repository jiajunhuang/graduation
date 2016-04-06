use graduation;

load data local infile 'sql/mock_grade.csv' into table grade fields terminated by ',' enclosed by '"' lines terminated by '\n' (id, fid, uid, score, score_at, comment);

load data local infile 'sql/mock_food.csv' into table food fields terminated by ',' enclosed by '"' lines terminated by '\n' (id, image, name, seller, create_at, price);

load data local infile 'sql/mock_deal.csv' into table deal fields terminated by ',' enclosed by '"' lines terminated by '\n' (id, seller, buyer, food, address, phone, sell_at);
