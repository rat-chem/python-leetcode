# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None

        iterator = head
        n_check = head

        count = 0

        while count < n and n_check:
            count += 1
            n_check = n_check.next

        skip = False
        head_check = False

        while n_check:
            n_check = n_check.next
            if skip:
                iterator = iterator.next
            skip = True
            head_check = True

        if not head_check:
            head = head.next
        else:
            iterator.next = iterator.next.next

        return head

def initList(head: ListNode, arr: []):
    for val in arr:
        if head.val == 0:
            head = ListNode(val, None)
            continue
        temp = head 
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val, None)
    return head
    
def printList(head: ListNode):
    while head:
        print(head.val, end = " ")
        head = head.next
    print()

def checkTestCases(testList: ListNode, answerList: []) -> bool:
    testListIter = testList
    testListCheck = []

    while testListIter:
        testListCheck.append(testListIter.val)
        testListIter = testListIter.next

    print(testListCheck)
    print(answerList)

    if testListCheck == answerList:
        return True
    else:
        return False


def main():
    testCases = [
        [
            [1, 2, 3, 4, 5], 2, [1, 2, 3, 5]
        ],
        [
            [1], 1, []
        ],
        [
            [1, 2], 1, [1]
        ],
    ]

    solution = Solution()
    count = 1

    for test in testCases:
        if checkTestCases(
                solution.removeNthFromEnd(
                    initList(ListNode(), test[0]), test[1]),
                test[2]):
            print("test case " + str(count) + " passed")
        else:
            print("test case " + str(count) + " failed")
        count += 1
        print()

if __name__ == "__main__":
    main()
