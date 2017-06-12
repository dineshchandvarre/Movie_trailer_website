import fresh_tomatoes
import media

Baahubali= media.Movie("Baahubali-2","Two brothers clash for control of a kingdom.","https://trendaa.in/wp-content/uploads/2017/02/Mighty-Prabhas-in-this-new-Bahubali-2-poster.jpg","https://youtu.be/qD-6d8Wo3do")
The_fate_and_furious=media.Movie("The Fate of the Furious","With Dom and Letty married, Brian and Mia retired and the rest of the crew exonerated, the globe-trotting team has found some semblance of a normal life. They soon face an unexpected challenge when a mysterious woman named Cipher forces Dom to betray them all. Now, they must unite to bring home the man who made them a family and stop Cipher from unleashing chaos.","http://t1.gstatic.com/images?q=tbn:ANd9GcQh2MCGCzxmCq4ei68-i6ELtRB18nFS4iHKBnHxffrLHkouoN-4","https://www.youtube.com/watch?v=hLL7DVLTAmo")

Zootopia=media.Movie("Zootopia","From the largest elephant to the smallest shrew, the city of Zootopia is a mammal metropolis where various animals live and thrive. When Judy Hopps (Ginnifer Goodwin) becomes the first rabbit to join the police force, she quickly learns how tough it is to enforce the law. Determined to prove herself, Judy jumps at the opportunity to solve a mysterious case. Unfortunately, that means working with Nick Wilde (Jason Bateman), a wily fox who makes her job even harder.","http://t2.gstatic.com/images?q=tbn:ANd9GcQj1fU0-Idujcrs_MB2xEWbVEygeCkcjYUp4Z-hSIPqgu0vFbQi","https://www.youtube.com/watch?v=jWM0ct-OLsM&t=68s")

Baywatch=media.Movie("Baywatch","Lifeguard Mitch Buchannon (Dwayne Johnson) and a brash new recruit (Zac Efron) uncover a criminal plot that threatens the future of the bay.","http://t1.gstatic.com/images?q=tbn:ANd9GcSGPyPu97eBhAFqNMLrNp10yB7noudkBKYYbB5ilZVSjH9ybUn5","https://www.youtube.com/watch?v=oPu1Ejq__N0")
SPIDER_MAN_HOMECOMING=media.Movie("SPIDER-MAN: HOMECOMING","Thrilled by his experience with the Avengers, young Peter Parker (Tom Holland) returns home to live with his Aunt May. Under the watchful eye of mentor Tony Stark, Parker starts to embrace his newfound identity as Spider-Man. He also tries to return to his normal daily routine -- distracted by thoughts of proving himself to be more than just a friendly neighborhood superhero. Peter must soon put his powers to the test when the evil Vulture emerges to threaten everything that he holds dear.","http://t0.gstatic.com/images?q=tbn:ANd9GcT8W3Fe7DD101g0M7OCalJN9u675sQAJFslGCjvs74PTOfEKt_t","https://www.youtube.com/watch?v=DiTECkLZ8HM")

Guardians_of_the_Galaxy_Vol_2=media.Movie("Guardians of the Galaxy Vol. 2","Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect their precious batteries from invaders. When it is discovered that Rocket has stolen the items they were sent to guard, the Sovereign dispatch their armada to search for vengeance. As the Guardians try to escape, the mystery of Peter's parentage is revealed.","http://t2.gstatic.com/images?q=tbn:ANd9GcSzRHzPW9j56dGLliOdUV0lzjeUwfALe9Zn2Ys7Kkwj4YsvDpsh","https://www.youtube.com/watch?v=duGqrYw4usE")

# Baahubali.show_trailer()
# Baahubali.show_poster()
movies=[Baahubali,The_fate_and_furious,Zootopia,Guardians_of_the_Galaxy_Vol_2,Baywatch,SPIDER_MAN_HOMECOMING]
fresh_tomatoes.open_movies_page(movies)