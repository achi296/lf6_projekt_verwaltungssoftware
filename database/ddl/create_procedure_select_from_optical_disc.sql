CREATE PROCEDURE SelectAllDiscs
AS
SELECT
    type,
    title,
    published_date,
    genre,
    price,
    description,
    fsk,
    ean,
    item_created
FROM optical_discs ;

