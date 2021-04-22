CREATE PROCEDURE InsertAllDiscs
AS
INSERT INTO optical_discs
    (
    [type],
    [title],
    [published_date],
    [genre],
    [price],
    [description],
    [fsk],
    [ean],
    [item_created]
    )
VALUES
    (
    @type,
    @title,
    @published_date,
    @genre,
    @price,
    @description,
    @fsk,
    @ean,
    @item_created
    )