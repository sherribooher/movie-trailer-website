# Import modules for the HTML file generation and the Movie class
import fresh_tomatoes
import media

# Create movie instances from the Movie class with specified attributes
wonder_woman = media.Movie(
    "Wonder Woman",
    "https://image.tmdb.org/t/p/w1280/imekS7f1OuHyUP2LAiTEM0zBzUz.jpg",
    "https://youtu.be/1Q8fG0TtVAY",
    "An Amazon princess comes to the world of Man to "
    "become the greatest of the female superheroes.",
    "2 hr 21 min")

star_wars = media.Movie(
    "Star Wars",
    "https://image.tmdb.org/t/p/w1280/tvSlBzAdRE29bZe5yYWrJ2ds137.jpg",
    "https://youtu.be/vZ734NWnAHA",
    "Luke Skywalker, Hans Solo, and Princess Leia save the "
    "Empire from the evil Imperial forces.",
    "2 hr 1 min")

the_help = media.Movie(
    "The Help",
    "https://image.tmdb.org/t/p/w1280/6u85CuvnbrzWMhKbGk4Bm5RnO3V.jpg",
    "https://youtu.be/l0dWCXCjX9o",
    "Three stories of three women combine to show how life in "
    "in Jackson, Mississippi revolved around 'the help'.",
    "2 hr 26 min")

schindlers_list = media.Movie(
    "Schindler's List",
    "https://image.tmdb.org/t/p/w1280/yPisjyLweCl1tbgwgtzBCNCBle.jpg",
    "https://youtu.be/bJcLRFWxRno",
    "The true story of Oskar Schindler, who saved over a "
    "thousand Jewish lives from the Nazis during World War II.",
    "3 hr 15 min")

scarface = media.Movie(
    "Scarface",
    "https://image.tmdb.org/t/p/w1280/zr2p353wrd6j3wjLgDT4TcaestB.jpg",
    "https://youtu.be/vREl66xmXsE",
    "The story of Tony Montana and how he became the biggest drug lord"
    "in Miami.",
    "2 hr 50 min")

gone_with_the_wind = media.Movie(
    "Gone with the Wind",
    "https://image.tmdb.org/t/p/w1280/4o1yeosjSFMaI9pe1rOkYcZ6hHO.jpg",
    "https://youtu.be/0dTsfsr6-X8",
    "A turbulent love story between a woman and man in the South during "
    "the Civil War and Reconstruction.",
    "3 hr 50 min")

goodfellas = media.Movie(
    "Goodfellas",
    "https://image.tmdb.org/t/p/w1280/hAPeXBdGDGmXRPj4OZZ0poH65Iu.jpg",
    "https://youtu.be/Zll4cjyk6sU",
    "The true story of Henry Hill who climbed the ranks of a Mafia "
    "family under the guidance of Jimmy Conway.",
    "2 hr 25 min")

the_wolf_of_wall_street = media.Movie(
    "The Wolf of Wall Street",
    "https://image.tmdb.org/t/p/w1280/vK1o5rZGqxyovfIhZyMELhk03wO.jpg",
    "https://youtu.be/iszwuX1AK6A",
    "A New York stockbroker refuses to cooperate in a large securities "
    "fraud case involving corruption on Wall Street.",
    "3 hr 15 min")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "https://image.tmdb.org/t/p/w1280/dM2w364MScsjFf8pfMbaWUcWrR.jpg",
    "https://youtu.be/s7EdQ4FqbhY",
    "A burger-loving hit man, his philosophical partner, a drug-addled "
    "gangster's moll and a washed-up boxer converge in this sprawling,"
    "comedic crime caper.",
    "2 hr 34 min")

# Assign the list of movies to a variable
movies = [wonder_woman, star_wars, the_help, schindlers_list,
          scarface, gone_with_the_wind, goodfellas,
          the_wolf_of_wall_street, pulp_fiction]

# Call the file to generate the website's html with the movie instances
fresh_tomatoes.open_movies_page(movies)
