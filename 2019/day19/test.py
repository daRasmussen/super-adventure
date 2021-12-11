from itertools import permutations

items = [
    "mutex",
    "dark matter",
    "klein bottle",
    "tambourine",
    "fuel cell",
    "astrolabe",
    "monolith",
    "cake"
]

hist = [
[items[0] , items[1] , items[2] , items[3]],
[items[0] , items[1] , items[3] , items[4]],
[items[0] , items[1] , items[4] , items[5]],
[items[0] , items[1] , items[5] , items[6]],
[items[0] , items[1] , items[6] , items[7]],
[items[0] , items[1] , items[2] , items[4]],
[items[0] , items[1] , items[2] , items[5]],
[items[0] , items[1] , items[2] , items[6]],
[items[0] , items[1] , items[2] , items[7]],
[items[1] , items[2] , items[3] , items[4]],
[items[1] , items[2] , items[4] , items[5]],
[items[1] , items[2] , items[5] , items[6]],
[items[1] , items[2] , items[6] , items[7]], 
[items[2] , items[3] , items[4] , items[5]],
[items[2] , items[3] , items[5] , items[6]],
[items[2] , items[3] , items[6] , items[7]],
[items[2] , items[3] , items[4] , items[6]],
[items[2] , items[3] , items[4] , items[7]],
[items[2] , items[3] , items[5] , items[7]],
[items[3] , items[4] , items[5] , items[6]],
[items[3] , items[4] , items[6] , items[7]],
[items[4] , items[5] , items[6] , items[7]],
]

print("\n")

for item in hist:
    print(item)


test = [1,2,3,4]
"""
12          test[0] + test[1]
13          test[0] + test[2]
14          test[0] + test[3]
21 * 
23          test[1] + test[2]
24          test[1] + test[3]
31 *
32 *
34          test[2] + test[3]
41 *
42 * 
43 *
"""
#print("\n")
#for index, value in enumerate(test[:-1]):
    #print(f"index: {index}, value: {value}")
#    for index2, value2 in enumerate(test[index + 1:]):
        #print(f"index2: {index2}, value2: {value2}")
#        print(value, value2)

#test2 = [1,2,3,4,5,6,7,8]

"""
1234    test[0] + test[1] + test[2] + test[3]               1
1245    test[0] + test[1] + test[3] + test[4]               2
1256    test[0] + test[1] + test[4] + test[5]               3
1267    test[0] + test[1] + test[5] + test[6]               4
1278    test[0] + test[1] + test[6] + test[7]               5
1235    test[0] + test[1] + test[2] + test[4]               6
1236    test[0] + test[1] + test[2] + test[5]               7
1237    test[0] + test[1] + test[2] + test[6]               8
1238    test[0] + test[1] + test[2] + test[7]               9

2345    test[1] + test[2] + test[3] + test[4]               10
2356    test[1] + test[2] + test[4] + test[5]               11
2367    test[1] + test[2] + test[5] + test[6]               12
2378    test[1] + test[2] + test[6] + test[7]               13  

3456    test[2] + test[3] + test[4] + test[5]               14
3467    test[2] + test[3] + test[5] + test[6]               15
3478    test[2] + test[3] + test[6] + test[7]               16
3457    test[2] + test[3] + test[4] + test[6]               17
3458    test[2] + test[3] + test[4] + test[7]               18
3468    test[2] + test[3] + test[5] + test[7]               19

4567    test[3] + test[4] + test[5] + test[6]               20
4578    test[3] + test[4] + test[6] + test[7]               21

5678    test[4] + test[5] + test[6] + test[7]               22
"""


"""
Items:                              Status:
all                                 lighter
[]                                  heavier
mutex                               heavier
dark matter                         heavier
klein bottle                        heavier
tambourine                          heavier
fuel cell                           heavier
astrolabe                           heavier
monolith                            heavier
cake                                heavier
###########################################
mutex, dark matter                  heavier < > 
dark matter, klein bottle           heavier
klein bottle, tambourine            lighter <*>
tambourine, fuel cell               heavier
fuel cell, astrolabe                heavier
astrolabe, monolith                 heavier
monolith, cake                      heavier
###############################################
klein bottle, tambourine, mutex         lighter
klein bottle, tambourine, dark matter   lighter
klein bottle, tambourine, fuel cell     lighter 
klein bottle, tambourine, astrolabe     lighter
klein bottle, tambourine, monolith      lighter
klein bottle, tambourine, cake          lighter
############################################################
klein bottle, tambourine, dark matter, fuel cell    lighter
klein bottle, tambourine, dark matter, astrolobe    lighter
klein bottle, tambourine, dark matter, monolith     lighter
klein bottle, tambourine, dark matter, cake         lighter
###########################################################
klein bottle, tambourine, fuel cell, astrolobe      lighter
klein bottle, tambourine, fuel cell, monolith       lighter
klein bottle, tambourine, fuel cell, cake           lighter
###########################################################
klein bottle, tambourine, monolith, cake            lighter
#######################################################
klein bottle, tambourine, mutex, dark matter    lighter
klein bottle, tambourine, mutex, fuel cell      lighter
klein bottle, tambourine, mutex, astrolabe      lighter 
klein bottle, tambourine, mutex, monolith       lighter
klein bottle, tambourine, mutex, cake           lighter 
####################################################################
klein bottle, tambourine, mutex, dark matter, fuel cell      lighter
klein bottle, tambourine, mutex, dark matter, astrolabe      lighter
klein bottle, tambourine, mutex, dark matter, monolith       lighter
klein bottle, tambourine, mutex, dark matter, cake           lighter
###############################################################################
klein bottle, tambourine, mutex, dark matter, fuel cell, astrolabe      lighter
klein bottle, tambourine, mutex, dark matter, fuel cell, monolith       lighter
klein bottle, tambourine, mutex, dark matter, fuel cell, cake           lighter
###########################################################################################
klein bottle, tambourine, mutex, dark matter, fuel cell, astrolabe, monolith        lighter
klein bottle, tambourine, mutex, dark matter, fuel cell, astrolabe, cake            lighter
###########################################################################################
mutex, dark matter, klein bottle                  heavier
mutex, dark matter, tambourine                    heavier
mutex, dark matter, fuel cell                     heavier
mutex, dark matter, astrolabe                     heavier
mutex, dark matter, monolith                      heavier
mutex, dark matter, cake                          heavier
###########################################################################################
mutex, dark matter, klein bottle, fuel cell       heavier
mutex, dark matter, klein bottle, astrolabe       heavier
mutex, dark matter, klein bottle, monolith        heavier
mutex, dark matter, klein bottle, cake            heavier
###########################################################################################
"""





