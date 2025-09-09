// https://leetcode.com/problems/two-sum/
// Reprak11

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)
	for pos, value := range nums {
		currentValue := target - value
		pos2, found := numMap[currentValue]
		if found {
			return []int{pos2, pos}
		}
		numMap[value] = pos
	}
	return []int{-1, -1}
}

