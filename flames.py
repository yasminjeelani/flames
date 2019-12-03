def removeCommanOccouranceInNames():
    name1 = input("Enter name1: ").lower().replace(" ","")
    name2 = input("Enter name2: ").lower().replace(" ","")
    for i in name1:
        for j in name2:
           if i==j:
                name1 = name1.replace(i,"",1)
                name2 = name2.replace(j,"",1)
                break

    return name1+name2


def findRelation():
    newname = removeCommanOccouranceInNames()
    count = len(newname)
    if count>0:
        relation =  ['Friend','Love','Affection','Marriage','Enemies','Sibling']
        while len(relation)>1:
            relation_index = (count%len(relation))-1
            if relation_index >=0:
                left = relation[:relation_index]
                right = relation[relation_index+1:]
                relation = right+left
            else:
                relation = relation[:len(relation)-1]
        print("Relationship is : ",relation[0])
    else:
        print("Enter a different name")


if __name__ == '__main__':
    findRelation()
