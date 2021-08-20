member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],[8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

def sales_management(names, records) :
  member_dict = dict()

  for name in names :
    total = 0
    count = 0
    for record in member_records[member_names.index(name)] :
      total = total + record
      count = count + 1
    member_dict[name] = total / count

  ranking= sorted(member_dict, key= lambda x : member_dict[x],reverse = True)

  get_bonus = []
  get_counsel = []

  for member in ranking :
    if (ranking.index(member) == 0 or ranking.index(member) == 1) :
      if member_dict.get(member) > 5 :
        get_bonus.append(member)
    if (ranking.index(member) == 4 or ranking.index(member) == 5) :
      if member_dict.get(member) <= 3 :
        get_counsel.append(member)

  for member in get_bonus :
    print(f"보너스 대상자 {member}")
  for member in get_counsel :
    print(f"면담 대상자 {member}")


sales_management(member_names, member_records)