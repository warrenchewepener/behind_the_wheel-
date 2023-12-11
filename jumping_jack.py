Songs = ["Just Cant Get Enough","Enjoy The Silence","Black Celebration","Everything Counts"] 

for album in Songs: 
    print(album)  

playback = input("What song from Depeche Mode do you like the best?")

if playback == "Just Cant Get Enough": 
    
    def alternative(hits,records,albums): 
        print(f"The {hits} album was {records} and it had a picture of a {albums} on the cover")

    alternative("First","Speak and Spell","Bird Hatching") 

elif playback == "Enjoy The Silence": 

    def alternative_two(hits_two,records_two): 
        print(f"That song was on the album {hits_two} and it was a pictute of a {records_two}")

    alternative_two("Violator","Rose")


elif playback == "Black Celebration": 

    def alternative_three(hits_three,records_three): 
        print(f"That song was on the album {hits_three} and it was a picture of a {records_three}") 

    alternative_three("Black Celebration","Building") 


elif playback == "Everything Counts": 

    def alternative_four(hits_four,records_four): 
        print(f"That song was on the album {hits_four} and it had a picture of a {records_four}") 

    alternative_four("Construction Time Again","Man with a hammer") 


else:
    print("Nevermind")                 