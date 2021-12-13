# Write code to remove duplicates from an unsorted linked list.

def remove_dups(n):
    m = {}
    previous = None
    while n:
        if n in m:
            previous.next = n.next
        else:
            m[n] = 1
            previous = n

        n = n.next
        