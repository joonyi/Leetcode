"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""
from TreeNode import TreeNode
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        curA = headA
        while curA:
            s.add(curA)
            curA = curA.next

        curB = headB
        while curB:
            if curB in s:
                return curB
            curB = curB.next

        return None

    """
    Approach 3: Two Pointers
    Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. 
    Then let them both traverse through the lists, one node at a time.
    When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); 
    similarly when pBpB reaches the end of a list, redirect it the head of A.
    
    If at any point pApA meets pBpB, then pApA/pBpB is the intersection node.
    To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and 
    B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), pBpB would 
    reach the end of the merged list first, because pBpB traverses exactly 2 nodes less than pApA does. 
    
    By redirecting pBpB to head A, and pApA to head B, we now ask pBpB to travel exactly 2 more nodes than 
    pApA would. So in the second iteration, they are guaranteed to reach the intersection node at the 
    same time.
    
    If two lists have intersection, then their last nodes must be the same one. So when pApA/pBpB 
    reaches the end of a list, record the last element of A/B respectively. If the two last elements 
    are not the same one, then the two lists have no intersections.
    
    """
    def getIntersectionNode2(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None

        # the idea is if you switch head, the possible difference between length would be countered.
        # On the second traversal, they either hit or miss.
        # if they meet, pa or pb would be the node we are looking for,
        # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None