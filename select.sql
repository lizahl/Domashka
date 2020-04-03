SELECT title, genre FROM films INNER JOIN genres ON (genres.id = films.genre_id);
===========================================================================
select title, name from films inner join films_directors on (films.id = films_directors.film_id) inner join directors on (directors.id = films_directors.director_id);
===========================================================================
SELECT title, genre FROM films LEFT JOIN genres ON (genres.id = films.genre_id) UNION SELECT title, genre FROM films RIGHT JOIN genres ON (genres.id = films.genre_id);
===========================================================================
select title, name, genre from films inner join films_directors on (films.id = films_directors.film_id) inner join directors on (directors.id = films_directors.director_id) inner join genres on (films.genre_id = genres.genre_id);
