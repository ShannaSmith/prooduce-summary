def create_delivery_report(day, um_deliveries):
    """print specified daily melon delivery report.
    
    Arguments:
    -specific Day: Day 1, Day 2
    - delivery document(txt file): um-deliveries-day-1.txt
    print report
    For example: 
    >>> create_delivery_report("Day 1", "um-deliveries-day-1.txt" )
     Delivered 6 Golden Midget Watermelons for total of $15.00
     Delivered 9 Hamis for total of $24.75
     Delivered 58 Honeydews for total of $57.42
     Delivered 6 Kleckley's Sweet Watermelons for total of $15.00
     Delivered 17 Long Milky Way - Moon and Stars Watermelons for total of $46.75
     Delivered 3 Melitopolski Watermelons for total of $9.00
      """

    print(day)  #Prints the day of the report
    the_file = open(um_deliveries) # Opens delivery file
    for line in the_file:   #interates through each line oof the file
        line = line.rstrip() #removes the space at the end of each line
        words = line.split('|') #separates the string and places each word in a list using the | as the delimiter

        melon = words[0] #assigns the first word of the list to the melon variable
        count = words[1] #assigns the second word of the list to the count variable
        amount = words[2] #assign the third woord of the list to the amount variable
        print(f"Delivered {count} {melon}s for total of ${amount}") #prints and concatenates a string for each line of the report
    the_file.close() #closes the file
create_delivery_report("Day 1", "um-deliveries-day-1.txt" ) #calls the function