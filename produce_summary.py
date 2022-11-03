def create_delivery_report(day, um_deliveries):
    print(day)
    the_file = open(um_deliveries)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()
create_delivery_report("Day 1", "um-deliveries-day-1.txt" )