## Recursion

- A function that calls itself is called a recursive function.
- Identification -> Decision Space and Recursive Tree -> Choices and Decisions 
- Decision Space: The space of all possible decisions that can be made at a given point in the algorithm.
- Recursive Tree: A tree that represents the recursive calls made by the algorithm.
- Base Case: The condition that stops the recursion.
- Recursive Case: The condition that continues the recursion.

## Recursive Tree

- Head -> Node with Input and Output
- Branches -> Choices
- Leaf -> Decisionas

eg: number of subsets of 'ab'
Branches -> whether to include a or not, whether to include b or not

```
        o/p  i/p
         " " "ab"
        /      \
    " ","b"  "a","b"
     /  \    /  \
"","" "b","" "a","" "ab",""

```
taking outputs -> "","b","a","ab"

- Subsets > Subsequences > Substrings
- Subsets: All possible combinations of elements of a set. (order doesn't matter)
- Subsequences: ordered contiguos sequence of elements of a set.
- Substrings: ordered sequence of characters of a string.

- example: set = {a,b,c}
- subset = {{},a,b,c,ab,ac,bc,abc} or {ba,ca,cb} (order doesn't matter)
- subsequence = {{},a,b,c,ab,ac,bc,abc}
- substring = {a,b,c,ab,abc,bc}

  