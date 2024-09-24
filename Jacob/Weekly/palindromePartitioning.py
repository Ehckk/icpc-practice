# Jacob Stephens - September 23, 2024
# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def main():

            # initiatlize variables
            queue = [[s]]
            level = 1 # index to split at - 1
            numPops = 0

            # there exists 2 to the power (len(s) - 1) partitions,
            # so stop when you have them all
            while len(queue) < 2**(len(s)-1):

                # bfs through tree using queue
                parent = queue.pop()
                numPops += 1

                # one child does not split at level
                queue.insert(0, parent)

                # one child splits at level
                queue.insert(0, splitAtI(parent, level-1))
                
                # increment splitting index if all children have been popped
                if numPops == 2**(level-1):
                    level += 1
                    numPops = 0
                    
            # filter out non-palindromic partitions
            palindromePartitions = filterNonPalindromes(queue)

            # final answer
            print(f"out", palindromePartitions)
            return palindromePartitions

        # this function splits a list of strings after the ith character
        def splitAtI(item, i):

            idxInItem = 0
            for substr in item:

                # get to target string in list
                if i >= len(substr):
                    i -= len(substr)
                    idxInItem += 1

                # split target string at i
                else:
                    # return entire list again with new split
                    res = item[:idxInItem] + [substr[:i+1], substr[i+1:]] + item[idxInItem+1:]
                    return res


        # this function takes all partitions and returns only palindromic partitions
        def filterNonPalindromes(queue):
            
            palindromePartitions = []

            # assume particion is a palindrome, but exit if one substring in partition is not a palindrome
            for partition in queue:
                partitionIsPalindrome = True

                for substr in partition:
                    if not isPalindrome(substr):
                        partitionIsPalindrome = False
                        break
                
                # append to output list if all substrings in partition are palindromes
                if partitionIsPalindrome:
                    palindromePartitions.append(partition) 

            return palindromePartitions

        # standard palindrom check given string
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
    
