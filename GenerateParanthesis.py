class Solution(object):
    array = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n <=0:
            return ""
        str = ""
        leftRemain = n
        rightRemain = n
        self.printParenthesis(leftRemain, rightRemain, str)
        return self.array

    def printParenthesis(self,leftRemain, rightRemain, str):

        if rightRemain == 0:
            self.array.append(str)
            return

        if leftRemain > 0:

            self.printParenthesis(leftRemain - 1, rightRemain,str+"(")

            if leftRemain<rightRemain:

                self.printParenthesis(leftRemain, rightRemain - 1, str+")")
        else:

            self.printParenthesis(leftRemain, rightRemain -1, str+")")


print Solution().generateParenthesis(1)