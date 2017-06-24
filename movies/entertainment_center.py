# import libraries
import fresh_tomatoes
import media

# assign movie list
wonder_woman = media.Movie("Wonder Woman","A woman superhero","https://upload.wikimedia.org/wikipedia/en/e/e1/Gal_Gadot_as_Wonder_Woman.jpg","https://www.youtube.com/watch?v=1Q8fG0TtVAY")
#print(wonder_woman.storyline)
#wonder_woman.show_trailer()
batman_superman = media.Movie("Batman VS Superman", "DC movie", "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg", "https://www.youtube.com/watch?v=NhWg7AQLI_8")
arrival = media.Movie("Arrival", "When gigantic spaceships touch down in 12 locations", "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg", "https://www.youtube.com/watch?v=aTNJtEXYsyw")
deadpool = media.Movie("Deadpool", "Fox ent movie", "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg", "https://www.youtube.com/watch?v=gtTfd6tISfw")

# objects stored in a list data structure
movies = [wonder_woman,batman_superman, arrival, deadpool]
fresh_tomatoes.open_movies_page(movies)

