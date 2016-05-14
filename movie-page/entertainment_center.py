import fresh_tomatoes  # this file will actually create the web page
import media  # this file contains the class to set the movie variables


# Below is a list of movies that I enjoy all details have been pulled
# from IMDB and are assumed to be accurate
star_wars1 = media.Movie("Star Wars Episode I: The Phantom Menace",
    "1999",
    "Ewan McGregor, Liam Neeson, Natalie Portman",
    """Two Jedi Knights escape a hostile blockade to
    find allies and come across a young boy who may bring balance to the Force,
    but the long dormant Sith resurface to reclaim their old glory.
    """,
    "/images/episode1.jpg",  # posters found and downloaded through google images
    "https://www.youtube.com/watch?v=I6hOlI9cg4o")

star_wars2 = media.Movie("Star Wars Episode II: Attack of the Clones",
    "2002",
    "Hayden Christensen, Natalie Portman, Ewan McGregor",
    """Ten years after initially meeting, Anakin
    Skywalker shares a forbidden romance with Padme,
    while Obi - Wan investigates an assassination attempt on the Senator
    and discovers a secret clone army crafted
    for the Jedi.
    """,
    "/images/episode2.jpg",  # posters found and downloaded through google images
    "https://www.youtube.com/watch?v=9C-fZCLsISA")

star_wars3 = media.Movie("Star Wars Episode III: Revenge of the Sith",
    "2005",
    "Hayden Christensen, Natalie Portman, Ewan McGregor",
    """During the near end of the clone wars,
    Darth Sidious has revealed himself and is ready to execute the last
    part of his plan to rule the Galaxy.
    """,
    "/images/episode3.jpg",  # posters found and downloaded through google images
    "https://www.youtube.com/watch?v=a3Cdj3GpobM")

star_wars4 = media.Movie("Star Wars Episode IV: A New Hope",
    "1977",
    " Mark Hamill, Harrison Ford, Carrie Fisher",
    """Luke Skywalker joins forces with a Jedi Knight,
    a cocky pilot, a wookiee and two droids to save the universe from the
    Empire's world-destroying battle - station, while also attempting to
    rescue Princess Leia from the evil Darth Vader.
    """,
    "/images/episode4.jpg",  # Posters found and downloaded through google images
    "https://www.youtube.com/watch?v=1g3_CFmnU7k")

star_wars5 = media.Movie("Star Wars Episode V: The Empire Strikes Back",
    "1980",
    " Mark Hamill, Harrison Ford, Carrie Fisher",
    """After the rebels have been brutally overpowered
    by the Empire on their newly established base,
    Luke Skywalker takes advanced Jedi training with Master Yoda,
    while his friends are pursued by Darth Vader as part of his plan to
    capture Luke.
    """,
    "/images/episode5.jpg",  # posters found and downloaded through google images
    "https://www.youtube.com/watch?v=96v4XraJEPI")

star_wars6 = media.Movie("Star Wars Episode 6: The Return of the Jedi",
    "1983",
    " Mark Hamill, Harrison Ford, Carrie Fisher",
    """After rescuing Han Solo from the palace of
    Jabba the Hutt, the rebels attempt to destroy the second Death Star,
    while Luke struggles to make Vader
    return from the dark side of the Force.
    """,
    "/images/episode6.jpg",  # posters found and downloaded through google images
    "https://www.youtube.com/watch?v=5UfA_aKBGMc")

# make an array of the movies above
movies = [star_wars1,
          star_wars2,
          star_wars3,
          star_wars4,
          star_wars5,
          star_wars6]

# call function to display web page
fresh_tomatoes.open_movies_page(movies)
