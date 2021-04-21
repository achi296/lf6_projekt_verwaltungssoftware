USE verwaltung;
CREATE TABLE optical_discs (
    id int not null auto_increment primary key,
    type char(3),
    title varchar(50),
    published_date date,
    genre varchar(50),
    price float(5),
    description varchar(500),
    fsk int,
    ean varchar(50),
    item_created timestamp
)
;