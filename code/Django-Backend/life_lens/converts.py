def ageConverter(age):
    if age < 30:
       return [1,0,0,0,0,0,0]
    elif age < 40:
        return [0,1,0,0,0,0,0]
    elif age < 50:
        return [0,0,1,0,0,0,0]
    elif age < 60:
        return [0,0,0,1,0,0,0]
    elif age < 70:
        return [0,0,0,0,1,0,0]
    elif age < 80:
        return [0,0,0,0,0,1,0]
    else:
        return [0,0,0,0,0,0,1]
    
def sleepConverter(sleep):
    if sleep < 4:
       return [0,0,0]
    elif sleep < 8:
        return [1,0,0]
    elif sleep < 12:
        return [0,1,0]
    else:
        return [0,0,1]
    
def smokeConverter(smoke):
    if smoke ==  "Everyday Smoker":
       return [1,0,0,0]
    elif smoke ==  "Sometimes Smoker":
        return [0,1,0,0]
    elif smoke ==  "Former Smoker":
        return [0,0,1,0]
    else:
        return [0,0,0,1]

    
def activeConverter(time):
    #https://www.cdc.gov/physicalactivity/basics/age-chart.html
    if time*7 > 150:
       return [1]
    else:
        return [0]
    
def alcoholConverter(amount, gender):
    #https://www.cdc.gov/alcohol/onlinemedia/infographics/excessive-alcohol-use.html
    #https://en.wikipedia.org/wiki/Standard_drink#:~:text=Each%20contains%20about%2014%20grams,or%2017.7%20ml%20of%20ethanol.
    standardDrink = 17.7 #(ml) the us measurement as model is trained on cdc data
    heavyDrinkerWomen = 8*standardDrink
    heavyDrinkerMan = 15*standardDrink
    if gender == 0:
        #If the user is a man
        if amount*7 > heavyDrinkerMan:
            return [1]
        else:
            return [0]
    elif gender == 1:
        #If the user is a women
        if amount*7 > heavyDrinkerWomen:
            return [1]
        else:
            return [0]