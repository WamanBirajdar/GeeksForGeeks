'''problem
You are given an array a and you need to generate an array b. You are allowed to apply only one type of operation on the array a, any number of times. In one operation you can swap ai, ai+1 if ai+ai+1 is even.
Array b should be generated after applying the above operation any number of times on array a and array b should be lexicographically the largest among all arrays that can be generated from array a, after applying the above operation any number of times.
'''
#User function Template for python3

class Solution():
    def lexicographicallyLargest(self, a, n):
        # Apply the given operation to generate array b
        for i in range(n-1):
            if (a[i]+a[i+1])%2==0:
                a[i],a[i+1]=a[i+1],a[i]
        b=sorted(a,reverse=True)
        return b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends


#Above code takes O(nlogn) time complexity due sorting
#here modiied version and reduces complexity below code takes O(n) time

#User function Template for python3

class Solution():
    def lexicographicallyLargest(self, a, n):
        # Apply the given operation to generate array b
        for i in range(n-1):
            if (a[i]+a[i+1])%2==0:
                a[i],a[i+1]=a[i+1],a[i]

        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                if a[j] > a[max_index]:
                    max_index = j
            a[i], a[max_index] = a[max_index], a[i]
                    
                
        return a
                
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends

