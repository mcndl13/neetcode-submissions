class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum_of_scores = 0

        for op in operations:

            if op == "+":
                record.append(record[-1] + record[-2])

            elif op == "D":
                record.append(record[-1] * 2)
            
            elif op == "C":
                record.pop()

            else:
                record.append(int(op))
                

        for score in record:
            sum_of_scores += score

        return sum_of_scores