-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_show_genres.name AS genre_name, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.name
ORDER BY number_of_shows DESC;