class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1 # это будет первый элемент меньше чем предыдущий, считая с конца
        # [9, 5, 2, 3, 1] -> 2
        for i in reversed(range(1, len(nums))):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break

        # если такой элемент есть, то находим тот, что чуть больше него
        # именно в правой половине (треб. задачи к сортировке). Так как они там все
        # отсортированы
        # [.., 3, 1] исходя из условий пред. цикла, то достаточно найти первый который больше
        if pivot >= 0:
            for i in reversed(range(pivot + 1, len(nums))):
                if nums[i] > nums[pivot]:
                    # меняем местами
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break

        # меняем порядок всех элементов справа от pivot на обратный
        # если pivot нет (-1), то есть список отсортирован по убыванию (если см. слева
        # направо), то просто пересортировуем весь список в обратном порядке
        left, right = pivot + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
