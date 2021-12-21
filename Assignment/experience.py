
print('***** Welcome to Ginika\'s ground shiping *****')
print('') 

shippingPrice = 0.0
premiumGroundShipping = 45000.0
amount = []
       

def groundShipping(weight):
    if(weight<= 2):
        shippingPrice = (weight * 540) + 7200
        return shippingPrice
    elif(weight>= 2 and weight <= 6):
        shippingPrice = (weight * 1080) + 7200
        return shippingPrice
    elif(weight>= 6 and weight <= 10):
        shippingPrice = (weight * 1440) + 7200
        return shippingPrice        
    else:
        shippingPrice = (weight * 1710) + 7200
        return shippingPrice        
 
def droneShipping(weight):
    if(weight<= 2):
        shippingPrice = (weight * 1620) + 0.0
        return shippingPrice
    elif(weight>= 2 and weight <= 6):
        shippingPrice = (weight * 3240) + 0.0
        return shippingPrice
    elif(weight>= 6 and weight <= 10):
        shippingPrice = (weight * 4320) + 0.0
        return shippingPrice        
    else:
        shippingPrice = (weight * 5130) + 0.0
        return shippingPrice   

def checkForCheapShipping(value):
    print('')
    amount.append(groundShipping(value))
    amount.append(droneShipping(value))
    amount.append(premiumGroundShipping)
    if(amount[0] == min(amount)):
        print('---Ground Shipping Method is the Cheapest---')
        return min(amount)
    elif(amount[1] == min(amount)):
        print('^^^ Drone Shipping Method is the Cheapest^^^')
        return min(amount)    
    elif(amount[2] == min(amount)):
        print('~~~ Premium Ground Shipping Method is the Cheapest~~~')
        return min(amount)
    else: 
        print('An error occur')


packageWeight = float(input('Please kindly enter the weight of your package: '))
while(packageWeight <= 0):
    print('Invalide package weight. Please enter a valid package weight')
    packageWeight = float(input('Please kindly enter the weight of your package: '))
    
print('Your Shipping price is: #' + str(checkForCheapShipping(packageWeight)))