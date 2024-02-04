def find_number_with_max_delit():
    colvo_delit = 0
    number_with_max_delit = None

    for number in range(84052, 84131):
        deliteli = []
        for i in range(1, number + 1):
            if number % i == 0:
                deliteli.append(i)
                 
        if len(deliteli) > colvo_delit:
            colvo_delit = len(deliteli)
            number_with_max_delit = number
            
    return colvo_delit, number_with_max_delit

colvo_delit, number_with_max_delit = find_number_with_max_delit()
print(colvo_delit, number_with_max_delit)


