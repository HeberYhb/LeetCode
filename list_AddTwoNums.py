# Definition for singly-linked list.
class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    d=0     #标记是否有进位
    l3=[]
    while(l1!=None or l2!=None or d!=0):
        if(l1==None):
            l1=ListNode(0)
        if(l2==None):
            l2=ListNode(0)
        if(l1==None and l2==None and d!=0):
            l3.append(d)
        tmpS=l1.val+l2.val+d
        if(tmpS<10):
            l3.append(tmpS)
            d=0
        else:
            tmpS=tmpS%10
            l3.append(tmpS)
            d=1
        l1=l1.next
        l2=l2.next
    return l3