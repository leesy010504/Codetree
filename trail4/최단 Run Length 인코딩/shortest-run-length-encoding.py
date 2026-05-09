A = input()
n = len(A)

def get_length(s):
    
    encoded_len = 0
    target = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == target:
            count += 1
        else:
            encoded_len += 1 + len(str(count))
            target = s[i]
            count = 1
            
    encoded_len += 1 + len(str(count))
    return encoded_len

min_len = float('inf')
    
for i in range(n):
    shifted_a = A[n-i:] + A[:n-i]
    current_len = get_length(shifted_a)
    min_len = min(min_len, current_len)
        
print(min_len)