#This  program will determines the award a person competing in a triathlon​ will receive

#Stores completion times of all competitions
swimming_completion_time=float(input("Enter the swimmers winners completion time: "))
cycling_completion_time=float(input("Enter the cycling winners completion time: "))
running_completion_time=float(input("Enterthe running winners completion time: "))

if swimming_completion_time<100.00:
    print("The swimmers winner finished the Trialthon in"+ " " + str(swimming_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial colours award" )

elif swimming_completion_time<105.00 and swimming_completion_time>100.01:
    print("The swimmers winner finished the Trialthon in"+ " " + str(swimming_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial half colours award" )
    
elif swimming_completion_time<110.00 and swimming_completion_time>105.01:
    print("The swimmers winner finished the Trialthon in"+ " " + str(swimming_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial scroll award" )
else:
    print("The swimmers winner finished the Trialthon in"+ " " + str(swimming_completion_time) + "minutes" + ", " + "Therefore the winner will recieve no award" )
    

if cycling_completion_time<100.00:
        print("The cycling winner finished the Trialthon in"+ " " + str(cycling_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial colours award" )
    
elif cycling_completion_time<105.00 and cycling_completion_time>100.01:
        print("The cycling winner finished the Trialthon in"+ " " + str(cycling_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial half colours award" )
        
elif cycling_completion_time<110.00 and cycling_completion_time>105.01:
        print("The cycling winner finished the Trialthon in"+ " " + str(cycling_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial scroll award" )
else:
        print("The cycling winner finished the Trialthon in"+ " " + str(cycling_completion_time) + "minutes" + ", " + "Therefore the winner will recieve no award" )
        
        
if running_completion_time<100.00:
                print("The running winner finished the Trialthon in"+ " " + str(running_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial colours award" )
            
elif running_completion_time<105.00 and running_completion_time>100.01:
                print("The running winner finished the Trialthon in"+ " " + str(running_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial half colours award" )
                
elif running_completion_time<110.00 and running_completion_time>105.01:
                print("The running winner finished the Trialthon in"+ " " + str(running_completion_time) + "minutes" + ", " + "Therefore the winner will recieve a Provincial scroll award" )
else:
                print("The running winner finished the Trialthon in"+ " " + str(running_completion_time) + "minutes" + ", " + "Therefore the winner will recieve no award" )