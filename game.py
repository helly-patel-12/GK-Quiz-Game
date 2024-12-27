def give_options(x,y,z,w):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    print("d):", w)

a ="Note: wrtie options in lower case only ! do not write whole answers." 
print("Hello! Welcome to my Quiz" "All Questions carries 10 marks each" "\n")
print(a) 
ans = input("\n" "Are you ready to play quiz (yes/no): ")

score = 0
total_questions = 20

correct_ans =["b", "c", "b", "d", "c", "b", "c", "b", "a", "b", "c", "a", "a", "c", "d", "b", "d", "b", "c", "c", "d", "c", "d", "d", "c"]

if ans.lower() == "yes":
    print("\n" "Question- What is the tallest mountain in the world? ")
    give_options("K2", "Mount Everest", "Mount Kilimanjaro", "Denali" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")
   
    print("\n" "Question- Who is the Founder of Apple Inc? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs", "Elon Musk")
    print(a)
    ans = input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")
    
    print("\n" "Question- Which planet is known as the 'Red Planet'? ")
    give_options("Venus", "Mars", "Jupiter", "Saturn")
    print(a)
    ans = input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")
    
    print("\n" "Question- Who discovered electricity? ")
    give_options("Isaac Newton", "Nikola Tesla", "Michael Faraday", "Benjamin Franklin")
    print(a)
    ans = input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")
    
    print("\n" "Question- What is the world's largest ocean? ")
    give_options("Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Southern Ocean" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[4]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")   

    print("\n" "Question- How many teeth does an adult human have? ")
    give_options("28", "32", "30", "26" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[5]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- Who invented the lightbulb? ")
    give_options("Albert Einstein", "Nikola Tesla", "Thomas Edison", "Alexander Graham Bell" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[6]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What does NASA stand for? ")
    give_options("North American Satellite Association", "National Aeronautics and Space Administration", "National Association of Space Astronauts", "National American Space Association" )    
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[7]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What is the fastest land animal? ")
    give_options("Cheetah ", "Ostrich", "Lion", "Elephant" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[8]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- How many bones are there in the adult human body? ")
    give_options("256", "206", "216", "232" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[9]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- Who was Shakespeare? ")
    give_options("A classical composer", "A British King", "An English playwright and poet ", "A scientist" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[10]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")  

    print("\n" "Question- What are the primary colors? ")
    give_options("Yellow, Blue, Red", "Yellow, Orange, Green", "Orange, Purple, Green", "Blue, Green, Yellow" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[11]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What does WWW stand for? ")
    give_options("World Wide Web", "World Web Warriors", "Wide World Web", "Web Wide World" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[12]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What is the square root of 121? ")
    give_options("10", "13", "11", "9" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[13]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- Who was the first man to walk on the moon? ")
    give_options("John Glenn", "Yuri Gagarin", "Buzz Aldrin", "Neil Armstrong" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[14]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What is the biggest animal in the world? ")
    give_options("African Elephant", "Blue Whale", "Saltwater Crocodile", "White Rhinoceros" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[15]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What is the primary gas found in the Earth's atmosphere? ")
    give_options("Oxygen", "Argon", "Carbon Dioxide", "Nitrogen" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[16]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What is the longest river in the world? ")
    give_options("Amazon River", "Nile River", "Yangtze River", "Mississippi River" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[17]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- Who are the two main characters in 'Romeo and Juliet'? ")
    give_options("Hamlet and Ophelia", "Macbeth and Lady Macbeth", "Romeo and Juliet", "Othello and Desdemona" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[18]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- In what country are the Pyramids of Giza located? ")
    give_options("Iran", "Iraq", "Egypt", "Saudi Arabia" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[19]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- Where do kangaroos originate from? ")
    give_options("Africa", "South America", "North America", "Australia" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[20]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What color are emeralds? ")
    give_options("Blue", "Red", "Green", "Purple" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[21]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- What country does sushi originate from? ")
    give_options("China", "Korea", "Thailand", "Japan" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[22]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")

    print("\n" "Question- Which planet has the most moons? ")
    give_options("Mars", "Venus", "Saturn", "Jupiter" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[23]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")
    
    print("\n" "Question- How many legs does a spider usually have? ")
    give_options("4", "6", "8", "10" )
    print(a)
    ans=input("&gt;&gt;&gt;&gt;")
    if ans.lower() == correct_ans[24]:
        score=score+1
        print("Correct")
    else:
        score=score-(0.5)
        print("Incorrect")


print("Now as we are done with the questions its time to show the scores to the user. I will multiply the score with 10 and then I will pass the if-else conditionals to print the status of the result of this Quiz game:")    
i = score*10
if i<70:
    print("Ouch!, your score is ",i,"/ 250 need to work hard")
elif 70<=i<=130:
    print("Discouraging! you scored ",i,"/ 250 better luck next time.")
elif 130<i<220:
    print("Congratulation! you scored ",i,"/ 250 you are a bit smart but could do better.")
elif 220<=i<235:
    print("Amazing! you scored ",i,"/ 250 you are quiet smart.")
else:
    print("Marvelous ! it's a perfect ",i,"/ 250 you are Intelligent. Keep it UP!")
