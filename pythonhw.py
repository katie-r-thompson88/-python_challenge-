import csv

with open("election_data.csv") as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)  
    data = list(csv_reader)
    
    print("Election Results:")
    
    row_count = len(data)
    print("Total votes: ", row_count)
   
    candidates = []
    for row in data:
       candidates.append(row[2])

    count = candidates.count('Khan')
    percent = int(count / row_count * 100) 
    print("Khan:", count, + percent, "%") 
    
    count = candidates.count('Correy')
    percent = int(count / row_count * 100) 
    print("Correy:", count, + percent, "%")
    
    count = candidates.count('Li')
    percent = int(count / row_count * 100) 
    print("Li:", count, + percent, "%")
    
    count = candidates.count("O'Tooley")
    percent = int(count / row_count * 100) 
    print("O'Tooley:", count, + percent, "%")

    li = data[2]
    max(l for l in li)
    print("Winner is:", li[2])
    