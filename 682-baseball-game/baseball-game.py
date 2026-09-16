class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:

            if op not in ["+", "D", "C"]:
                stack.append(int(op))
        
            elif op == "+":
                stack.append(stack[-2] + stack[-1])
            
            elif op == "D":
                stack.append(stack[-1] * 2)
            
            elif op == "C":
                stack.pop()
                
        return sum(stack)
