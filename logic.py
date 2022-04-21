"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    days = (mon, tue, wed, thu, fri) = (1, 2, 3, 4, 5)
    possible_days = list(itertools.permutations(days))
    # (1, 2, 3, 5, 4), (1, 2, 4, 3, 5),
    # print(possible_days) 

    # 2 + 3 = Hamming is the programmer
    # Wilkes brought the droid, and 9 he is not the designer
    # 11 Writer brought the laptop and 4 he is not Minsky
    # Wilkes or laptop arrive on monday and 1 laptop on wednesday, Wilkes = monday
    # print(possible_days)
    # 1, 4, 5, 3, 2
    """
    days_by_name = [(Wilkes, Hamming, Minsky, Knuth, Simon) 
    	for (Wilkes, Hamming, Minsky, Knuth, Simon) in possible_days 
    	if Wilkes == mon and Knuth == Simon+1]
    # print(days_by_name)
    """
    days_by_job = [(designer, manager, writer, programmer, _) 
    	for (designer, manager, writer, programmer, _) in possible_days
    	if writer == 3 and
    	manager != fri and 
    	designer != thu] #
    #print(days_by_job)
    days_by_object = [(droid, tablet, laptop, iphone, _) 
    	for (droid, tablet, laptop, iphone, _) in possible_days
    	if laptop == 3 and 
    	tablet != 5 and
    	(iphone == tue or tablet == tue)]
    
    ranks = set([(Wilkes, Hamming, Minsky, Knuth, Simon) 
    	for (Wilkes, Hamming, Minsky, Knuth, Simon) in possible_days 
    	if Wilkes == mon and Knuth == Simon + 1
    	for (designer, manager, writer, programmer, _) in days_by_job
    	if Hamming == programmer and # 2 + 3 = Hamming is the programmer
    	Minsky != writer and # 4
    	Wilkes != designer and # 9
    	Simon == manager # or Knuth == manager + 1 # 10 and 6
    	for (droid, tablet, laptop, iphone, _) in days_by_object
    	if designer != droid and
    	laptop == writer
    	])
    #print(ranks.pop())
    name_list = ["Wilkes", "Hamming", "Minsky", "Knuth", "Simon"]
    day_list = list(ranks.pop())
    result_dict = {name_list[i]: day_list[i] for i in range(0,len(day_list))}
    print(result_dict)

    return sorted(result_dict, key=lambda name: result_dict[name])
    # print(days_by_object)
    # 10 and 6: Simon is the manager
    	#if writer == 3:
    		#print((designer, manager, writer, programmer, _))
    	# designer != thursday and != droid
    	# manager = 1 to 4
    	# 6 eliminate all the days Knuth does not follow Simon
    	# Wilkes or laptop arrive on monday and 1 laptop on wednesday, Wilkes must monday
    #print((Wilkes, Hamming, Minsky, Knuth, Simon))
    #(_, _, writer, _, _) = (Wilkes, Hamming, Minsky, Knuth, Simon)
    #(droid, _, laptop, ) = (Wilkes, Hamming, Minsky, Knuth, Simon)
    # 12 tuesday == iphone or tablet

def answer(**names):
    "Given a dict of {name:day}, return a list of names sorted by day."
    print(names)
    return sorted(names, key=lambda name: names[name])

assert logic_puzzle() == ['Wilkes', 'Simon', 'Knuth', 'Hamming', 'Minsky'] # 1, 4, 5, 3, 2


"""
return next(answer(Wilkes=Wilkes, Hamming=Hamming, Minsky=Minsky,
                       Knuth=Knuth, Simon=Simon)
                for (Wilkes, Hamming, Minsky, Knuth, Simon) in possible_days
                if Knuth == Simon + 1 # 6
                for (programmer,writer,manager,designer,_) in possible_days
                if Knuth == manager + 1 # 10
                and thu != designer # 7
                and programmer != Wilkes and writer != Minsky # 2, 4
                for (laptop, droid, tablet, iphone, _) in possible_days
                if set([laptop, Wilkes]) == set([mon, writer]) # 11
                and set([programmer, droid]) == set([Wilkes, Hamming]) # 3
                and (iphone == tue or tablet == tue) # 12
                and designer != droid # 9
                and Knuth != manager and tablet != manager # 5
                and wed == laptop # 1
                and fri != tablet # 8
                )

"""