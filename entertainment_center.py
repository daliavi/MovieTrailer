import media
import fresh_tomatoes


def show_movies():
    # creating movie instances

    jungle_book = media.Movie("Jungle Book",
                              "http://cdn.collider.com/wp-content/uploads/2015/08/jungle-book-poster-hi-res.jpeg",  # NOQA
                              "https://youtu.be/5mkm22yO-bs")  # NOQA
    storks = media.Movie("Storks",
                         "http://www.getmovieposter.com/wp-content/uploads/getmovieposter_storks_1.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=B1UE7hMblmQ")  # NOQA

    zootopia = media.Movie("Zootopia",
                           "http://cdn.collider.com/wp-content/uploads/2015/12/zootopia-movie-poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=WWFB-zrxn7o")  # NOQA

    finding_dory = media.Movie("Finding Dory",
                               "http://www.everythingpixar.com/uploads/3/8/2/4/38249737/9213755_orig.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=NQu-153MnGQ")  # NOQA

    lion_king = media.Movie("The Lion King",
                            "http://mpspg.com/images/lion-king-movie-cover-i11.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=GaJWzJfoXlE")  # NOQA

    frozen = media.Movie("Frozen",
                         "https://walter.trakt.us/images/movies/000/077/349/posters/original/9d1a3cdcf2.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=R-cdIvgBCWY")  # NOQA

    movies = [jungle_book, storks, zootopia, finding_dory, lion_king, frozen]
    fresh_tomatoes.open_movies_page(movies)
    return

show_movies()
