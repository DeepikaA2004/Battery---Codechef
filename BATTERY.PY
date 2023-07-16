# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the battery health
    X = int(input())
    
    # Check if the battery is in optimal condition
    if X >= 80:
        print("YES")
    else:
        print("NO")