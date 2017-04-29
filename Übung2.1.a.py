
def delete(seq,index):
    if (0 <= index < len(seq)):
        seq.pop(index)
        return seq
    else:
        print("The index is invalid")

""" list.pop([i])
    Remove the item at the given position in the list, and return it.
    If no index is specified a.pop() removes and returns the last item in the list.
    (The square brackets around the i in the method signature denote that the parameter is optional
    not that you should type square brackets at that position. 
    You will see this notation frequently in the Python Library Reference.)"""

def get(seq,index):
    if (0 <= index < len(seq)):
        return seq[index]
    else:
        print("The index is invalid")

def concat(seq1,seq2):
    return seq1+seq2


# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# seq1.append(seq2) == [11,22,33,[44,55]]  !!!
# seq1 + seq2 == [11,22,33,44,55]
# (gives you a new list, wont change the originals)

seq1= [11,22,33]
seq2= [44,55,66]

print(" seq1 :",seq1,"\n","seq2 :",seq2)
print("deleting the element at index 1 in seq2")
deletedSeq= delete(seq2,1)
print("Seq2 :",deletedSeq)

getReturn = get(seq1,1)
print("returning the 2. element in seq1 :",getReturn)

newList = concat(seq1,seq2)
print("seq1 + seq2 :",newList)
