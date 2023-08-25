# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def from_list(cls, values):
        if len(values) == 0:
            return ListNode()
        elif len(values) == 1:
            return ListNode(values[0])
        else:
            return ListNode(values[0], cls.from_list(values[1:]) )
    

    def to_list(self,):
        if self.next is None:
            return [self.val]
        else:
            return [self.val] + self.next.to_list()
        
    def __repr__(self) -> str:
        return str(self.to_list())

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None and list2 is None:
            return 
        elif list1 is None:
            return list2
            # greater_node = None
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            smaller_node = list1
            greater_node = list2
        else:
            smaller_node = list2
            greater_node = list1

        
        if smaller_node.next is None and greater_node.next is None:
            return ListNode(smaller_node.val, ListNode(greater_node.val))
        else:
            return ListNode(smaller_node.val, self.mergeTwoLists(smaller_node.next, greater_node))
        
        


if __name__ == "__main__":
    test_cases = {
        ((1,2,3),(1,1,3)) : [1,1,1,2,3,3],
        ((),(0,)) : [0],
        }

    node = ListNode.from_list((1,2,3))
    print(node)


    for test, result in test_cases.items():
        node1 = ListNode.from_list(test[0])
        node2 = ListNode.from_list(test[1])
        merged = Solution().mergeTwoLists(node1, node2)
        assert merged.to_list() == result