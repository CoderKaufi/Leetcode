import random

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def insert(head, val):
    Node = ListNode(val)

    # pokud je to první Node a zároveň musí být větší než 0
    if head.next == None and val > head.val:
        head.next = Node
        return head
    # hledání místa
    current = head
    while current.next != None and current.next.val <= val:
        current = current.next
    # né vždycky doputuje číslo na konec, proto nemůže být Node.next defaultní, jinak by to přerušilo list
    Node.next = current.next
    current.next = Node
    return head

def iterate(head):
    current = head
    while current != None:
        print(current.val)
        current = current.next


# jelikož je ten list sorted tak nemusíme mít mezipaměť v listu, ale můžeme vyhazovat co chceme
def delete_duplicates(head):
    current = head
    if not head:
        return head
    while current.next != None:
        while current.val == current.next.val:
            current.next = current.next.next
            if current.next == None:
                break
            
        current = current.next

    return head

l = ListNode()

l = insert(l, 0)
l  = insert(l, 1)
l  = insert(l, 1)
l  = insert(l, 2)
l  = insert(l, 2)
l = insert(l, 9)
l = insert(l, 11)
l = insert(l, 11)
l = insert(l, 11)
l = insert(l, 11)
l = insert(l, 11)
l = insert(l, 11)
l = insert(l, 11)
l = insert(l, 11)
l = insert(l, 67)

l = delete_duplicates(l)
iterate(l)

