class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def main():
            queue = [[s]]

            level = 1
            numPops = 0

            while len(queue) < 2**(len(s)-1):
                parent = queue.pop()
                
                queue.insert(0, parent)
                queue.insert(0, splitAtI(parent, level-1))
                numPops += 1


                if numPops == 2**(level-1):
                    level += 1
                    numPops = 0
                    
            print(queue)
            palindromePartitions = filterNonPalindromes(queue)

            print(palindromePartitions)
            return palindromePartitions

        def splitAtI(item, i):

                
            idxInItem = 0
            for substr in item:
                if i >= len(substr):
                    i -= len(substr)
                    idxInItem += 1

                else:
                    print(i)
                    print(substr)

                    res = item[:idxInItem] + [substr[:i+1], substr[i+1:]] + item[idxInItem+1:]

                    return res

        def filterNonPalindromes(queue):
            
            palindromePartitions = []

            

            for partition in queue:
                partitionIsPalindrome = True

                for substr in partition:
                    
                    if not isPalindrome(substr):
                        # if one substring is not a palindrome, the whole partition is invalid
                        partitionIsPalindrome = False
                        break
                
                if partitionIsPalindrome:
                    palindromePartitions.append(partition) 


            return palindromePartitions


        def isPalindrome(substr):

            i = 0
            j = len(substr)-1
            while i < j:
                if substr[i] != substr[j]:
                    return False
                i += 1
                j -= 1
            return True

        return main()





            
                
