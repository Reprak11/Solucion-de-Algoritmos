// https://leetcode.com/problems/two-sum/
// Reprak11
func isValueInArray(nums []int, currentValue int, currentPos int) (pos2 int, found bool) {
	for pos, value := range nums {
		if (currentPos != pos) && (value == currentValue) {
			return pos, true
		}
	}
	return -1, false
}

func twoSum(nums []int, target int) []int {
	isThere := false
	secondPos := -1
	for pos, value := range nums {
		secondPos, isThere = isValueInArray(nums, target-value, pos)
		if isThere == true {
			return []int{pos, secondPos}
		}
	}
	return []int{-1, -1}
}
