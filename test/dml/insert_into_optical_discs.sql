USE verwaltung;
INSERT INTO optical_discs (
    type,
    title,
    published_date,
    genre,
    price,
    description,
    fsk,
    ean,
    item_created
)
VALUES
(
'DVD',
'Star Wars Episode VII',
'2015-09-01',
'Science-Fiction',
19.99,
'Star Wars: Die letzten Jedi/Zusammenfassung
'Luke Skywalker hat sich im Alter auf eine einsame Insel zurückgezogen.',
12,
'8717418565114',
current_timestamp()
);