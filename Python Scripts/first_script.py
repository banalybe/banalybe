
largest = None
smallest = None
while True:
    set = input ("Enter a Number: ")
    if set == "done":
        break
    try:
        x = int(set)

    except:
            print('Invalid input')
            continue
    for the_lrg in [x]:
            if largest is None:
                largest = the_lrg
            elif the_lrg > largest:
                largest = the_lrg

    for the_sml in [x]:
            if smallest is None:
                smallest = the_sml
            elif the_sml < smallest:
                smallest = the_sml
print("Maximum is", largest)
print("Minimum is", smallest)
