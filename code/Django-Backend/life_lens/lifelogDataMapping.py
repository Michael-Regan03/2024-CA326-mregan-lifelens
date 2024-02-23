# actionOption Numbers in the csv and what they represent
actionOption = [
    (111 ,"Sleep" ),
    (112, "Sleepless"),
    (121, "Meal"),
    (122, "Snack"),
    (131, "Medical services"), # treatments, sick rest
    (132, "Personal hygiene"), # (bath)
    (133, "Appearance management"), # (makeup, change of clothes)
    (134, "Beauty-related services"),
    (211, "Main job"),
    (212, "Side job"),
    (213, "Rest during work"),
    (22, "Job search"),
    (311, "School class / seminar"), #(listening)
    (312, "Break between classes"),
    (313, "School homework, self-study"), #(individual)
    (314, "Team project"), #(in groups)
    (321, "Private tutoring"), # (offline)
    (322, "Online courses"),
    (41, "Preparing food and washing dishes"),
    (42, "Laundry and ironing"),
    (43, "Housing management and cleaning"),
    (44, "Vehicle management"),
    (45, "Pet and plant caring"),
    (46, "Purchasing goods and services"), #(grocery/take-out)
    (51, "Caring for children under 10 who live together"),
    (52, "Caring for elementary, middle, and high school students over 10 who live together"),
    (53, "Caring for a spouse"),
    (54, "Caring for parents and grandparents who live together"),
    (55, "Caring for other family members who live together"),
    (56, "Caring for parents and grandparents who do not live together"),
    (57, "Caring for other family members who do not live together"),
    (81, "Personal care-related travel"),
    (82, "Commuting and work-related travel"),
    (83, "Education-related travel"),
    (84, "Travel related to housing management"),
    (85, "Travel related to caring for family and household members"),
    (86, "Travel related to participation and volunteering"),
    (87, "Socializing and leisure-related travel"),
    (61, "Religious activities"),
    (62, "Political activity"),
    (63, "Ceremonial activities"),
    (64, "Volunteer"),
    (711, "Offline communication"),
    (712, "Video or voice call"),
    (713, "Text or email (Online)"),
    (721, "Reading books, newspapers, and magazines"),
    (722, "Watching TV or video"),
    (723, "Listening to audio"),
    (724, "Internet search or blogging"),
    (725, "Gaming (mobile, computer, video)"),
    (741, "Watching a sporting event"),
    (742, "Watching movie"),
    (743, "Concerts and plays"),
    
    #Duplicate
    (744, "Art galleries and museums,Amusement Park, zoo "),

    (745, "Festival, carnival"),
    (746, "Driving, sightseeing, excursion"),
    (751, "Walking"),
    (752, "Running, jogging"),
    (753, "Climbing, hiking"),
    (754, "Biking"),
    (755, "Ball games"), # (soccer, basketball, baseball, tennis, etc)
    
    #Duplicate
    (756, "Personal exercises"), #(yoga, pilates, etc.),Camping, fishing

    (761, "Group games"), #(board games, card games, puzzles, etc.)
    (762, "Personal hobbies"), #(woodworking, gardening, etc.)
    (763, "Group performances"), #(orchestra, choir, troupe, etc.)
    (764, "Liberal arts and learning"),#(languages, musical instruments, etc.)
    (791, "Nightlife"),
    (792, "Smoking"),
    (793, "Do nothing and rest"),
    (91, "Online shopping"),
    (92, "Offline shopping"),
]


#Not relevant to store
actionSub = [
    ('meal_amount','meal_amount'),
    ('move_method','move_method')
]


mealAmountMapping = {
    1: 'light',
    2: 'moderate',
    3: 'heavy'
}



transportMapping = {
    1: 'walk',
    2: 'driving',
    3: 'taxi',
    4: 'personal-mobility',
    5: 'bus',
    6: 'train/subway',
    7: 'other'
}

actionSubOption = (
    ('light', 'light'),
    ('moderate','moderate'),
    ('heavy','heavy'),
    ('walk', 'walk'),
    ('driving','driving'),
    ('taxi','taxi'),
    ('personal-mobility','personal-mobility'),
    ('bus','bus'),
    ('train/subway','train/subway'),
    ('other','other')
)

condition = [
    ('ALONE', 'ALONE'),
    ('WITH_ONE','WITH_ONE'),
    ('WITH_MANY','WITH_MANY')
]

conditionSub1Option = [
    (1, 'with-families'),
    (2, 'with-friends'),
    (3, 'with-colleagues'),
    (4, 'acquaintances'),
    (5, 'others')
]


conditionSub2Option = [
    (1, 'passive in conversation'),
    (2, 'moderate participation in conversation'),
    (3, 'active in conversation')
]

activity = [
    (0, 'IN_VEHICLE'),
    (1, 'ON_BICYCLE'),
    (2, 'ON_FOOT'),
    (3, 'STILL'),
    (4, 'UNKNOWN'),
    (6, 'UNKNOWN'),
    (5, 'TILTING'),
    (7, 'WALKING'),
    (8, 'RUNNING')
]





place = [
    ('home', 'home'),
    ('workplace','workplace'),
    ('restaurant','restaurant'),
    ('outdoor', 'outdoor'),
    ('other_indoor','other_indoor')
]





######## sleep 

sleep = {
    (1, 'Not at all'),
    (2, 'Not much'),
    (3, 'Moderately'),
    (4, 'Fairly'),
    (5, 'Fully'),
}

sleepProblem = {
    (1, 'It took more than 30 minutes to fall asleep.'),
    (2, 'I was awake during the night or prior to my scheduled wake time.'),
    (3, 'I was awake during the night to go to the bathroom.'),
    (4, 'I snored loudly during the sleep or woke up during the night choking.'),
    (5, 'I was disturbed by the low temperature during sleep.'),
    (6, 'I was disturbed by the high temperature during sleep.'),
    (7, 'I had nightmares.'),
    (8, 'I was disturbed by the pain.'),
    (9, 'I was disturbed by other reasons not listed above.'),
    (0, 'I did not have any problems.'),
}

dream = {
    (1, 'Nightmare'),
    (2, 'Neutral dream'),
    (3, 'Nice dream'),
    (4, 'None')
}

amCondition = {
    (1, 'Not at all') , 
    (2, 'Not much'), 
    (3, 'Moderately'),
    (4, 'Fairly'),
    (5, 'Fully')
}

amEmotion = {
    (1, 'Very unpleasant'),
    (2, 'Unpleasant'), 
    (3, 'Moderate'), 
    (4, 'Pleasant') , 
    (5, 'Very pleasant')
}


######## Evening

pmStress_Fatigue = {
    (1, 'Very much'), 
    (2, 'Fairly'), 
    (3, 'As usual'), 
    (4, 'Not much'), 
    (5, 'Not at all')
}


alcoholType = {
        (1, "Beer"),
        (2, "Wine"),
        (3, "Hard Cider"),
        (4, "Mead"),
        (5, "Sake"),
        (6, "Gin"),
        (7, "Brandy"),
        (8, "Whiskey"),
        (9, "Rum"),
        (10, "Tequilla"),
        (11, "Vodka"),   
   }


# https://www.alcoholrehabguide.org/alcohol/types/
alcoholPerecent = {
        1: 0.05, #Beer
        2: 0.11, #Wine
        3: 0.05, #Hard Cider
        4: 0.12, #Mead
        5 : 0.16, #Sake
        6: 0.45, #Gin
        7: 0.4, #Brandy
        8: 0.4, #Whiskey
        9: 0.4, #Rum
        10: 0.4, #Tequilla
        11 :0.4, #Vodka
}


