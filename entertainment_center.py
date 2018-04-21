import fresh_tomatoes
import media

#Defining Global Variables
wreck_it_ralph = media.Movie("Wreck it Ralph",
                         "The story of a video game bad guy, who wants to be a hero.",
                         "https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg",
                         "https://www.youtube.com/watch?v=87E6N7ToCxs",
                         "$49.1 Million"   )

incredibles = media.Movie("The Incredibles",
                    "A family with incredible abilities battles for their place in a world that doesn't want them.",
                    "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                    "https://www.youtube.com/watch?v=eZbzbC9285I",
                          "$70.4 Million")

count_of_monte_cristo = media.Movie("The Count of Monte Cristo",
                          "Seeking a simple life, a french sailor must become something else when he's falsely imprisoned.",
                          "https://upload.wikimedia.org/wikipedia/en/b/bb/The_Count_of_Monte_Cristo_film.jpg",
                          "https://www.youtube.com/watch?v=gzRSVl8UewM",
                                    "$11.4 Million")

case_for_christ = media.Movie("The Case for Christ",
                          "A reporter seeks to disprove the claims of the Bible.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cc/The_Case_for_Christ_poster.jpg",
                          "https://www.youtube.com/watch?v=On6RM27qSFc",
                              "$4 Million")

war_room = media.Movie("War Room",
                      "A young woman struggles in her marriage.",
                      "https://upload.wikimedia.org/wikipedia/en/a/a7/WarRoomMoviePoster.jpg",
                      "https://www.youtube.com/watch?v=mIl-XY9t_Lw",
                       "$11.4 Million")

risen = media.Movie("Risen",
                     "A Roman soldier investigates the disappearance of a Jew.",
                     "https://upload.wikimedia.org/wikipedia/en/3/3c/Risen_2016_poster.jpg",
                     "https://www.youtube.com/watch?v=OcTVLfn5i8g",
                    "$11.4 Million")

courageous = media.Movie("Courageous",
                     "An officer struggles with responsibilities in his job and at home.",
                     "https://upload.wikimedia.org/wikipedia/en/3/3b/Courageous_Cover.JPG",
                     "https://www.youtube.com/watch?v=i9VT_NBIVfs",
                         "$9.1 Million")

fireproof = media.Movie("Fireproof",
                     "In a failing marriage, the husband takes drastic measures to keep his wife.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b7/Fireproof_poster.jpg",
                     "https://www.youtube.com/watch?v=84q0SXW781c",
                        "$6.8 Million")

gods_not_dead = media.Movie("God's Not Dead",
                     "A student investigates and upholds the reliability of the Bible.",
                     "https://upload.wikimedia.org/wikipedia/en/c/cf/God%27s_Not_Dead.jpg",
                     "https://www.youtube.com/watch?v=bMjo5f9eiX8",
                            "$9.2 Million")

gods_not_dead_2 = media.Movie("God's Not Dead 2",
                     "A Teacher goes on trial for talking to a student about Jesus.",
                     "https://upload.wikimedia.org/wikipedia/en/4/42/God%27s_Not_Dead_2_poster.jpg",
                     "https://www.youtube.com/watch?v=Sxz-Y-c2UUc",
                              "$7.6 Million")

the_song = media.Movie("The Song",
                      "A man struggles between music and family and finds wisdom instead.",
                      "https://upload.wikimedia.org/wikipedia/en/c/ca/The_Song_%282014%29_Official_Poster.jpg",
                      "https://www.youtube.com/watch?v=rDK7EodvRd0",
                       "$568K")

passion = media.Movie("The Passion of the Christ",
                      "The story of an unpopular man who died to save everyone.",
                      "https://upload.wikimedia.org/wikipedia/en/6/61/Thepassionposterface-1-.jpg",
                      "https://www.youtube.com/watch?v=4Aif1qEB_JU",
                      "$83.8 Million")

#Array list containing all movies
movies = [wreck_it_ralph, incredibles, count_of_monte_cristo, risen, courageous, case_for_christ, fireproof,war_room, gods_not_dead, gods_not_dead_2, the_song, passion]
fresh_tomatoes.open_movies_page(movies)