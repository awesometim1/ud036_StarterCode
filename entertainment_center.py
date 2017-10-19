import media, fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                       "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar", "A marine on an alien planet", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")



ai = media.Movie("AI", "A robotic boy embarks on a journey to find his true self", "http://www.gstatic.com/tv/thumb/movieposters/27945/p27945_p_v8_ai.jpg",
                 "https://www.youtube.com/watch?v=oBUAQGwzGk0")

rat = media.Movie("Ratatouille" , "A rat who loves tasting food and befriends a cook" , "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",
                  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

indiana = media.Movie("Indiana Jones: The Last Crusade", "Indiana Jones goes on a quest to find the magical goblet", "http://t1.gstatic.com/images?q=tbn:ANd9GcTvapMUYGkuF5IrOsugBN3-kAIMHEhGu2exzQErGjVMiXCHtCmA",
                      "https://www.youtube.com/watch?v=a6JB2suJYHM")

wonder = media.Movie("Wonder Woman", "She fights a war to end all wars and discovers her true destiny", "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",
	"https://www.youtube.com/watch?v=VSB4wGIdDwo")

movies = [toy_story, avatar, ai, rat, indiana, wonder]
fresh_tomatoes.open_movies_page(movies)


