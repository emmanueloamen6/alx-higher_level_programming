-- script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id FROM hbtn_0d_tvshows
LEFT JOIN tv_show_genres.genre_id ON tv_shows.title=tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
