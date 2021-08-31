class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        d = {3: "Fizz", 5: "Buzz"}

        for i in range(1, n + 1):
            s = ""
            for key in d:
                if i % key == 0:
                    s += d[key]

            if not s:
                s = str(i)

            result.append(s)


        return result

