def fibonacci_sequence(n_terms):
    a,b = 0,1
    sequence =[]

    for _ in range(n_terms):
        sequence.append(a)
        a,b = b , a+b 
    return sequence

i = int(input("Enter the number of terms: "))
if i<=0:
    print("Please enter a positive number. ")
else: 
    result = fibonacci_sequence(i)
    print("Fibonacci Sequence is : ",result)