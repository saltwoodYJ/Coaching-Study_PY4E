def count_word(string, check) :
  count = 0
  checklen = len(check) # 찾을 단어의 길이
  checkindex = 0
  for x in string :
    if x == check[checkindex] : # 현재 탐색중인 단어와 찾아야할 단어가 같다면
      checkindex = checkindex + 1 # 찾아야할 단어 갱신
      if checkindex == checklen : # 만약 찾아야할 단어를 다 찾았다면
        count = count + 1 # 카운트해주고
        checkindex = 0 # 찾아야할 단어 초기화
    else : # 탐색중인 단어와 찾아야할 단어가 다르다면
      checkindex = 0 # 찾아야할 단어 초기화
  print(count) # 갯수 출력


a ="""안녕하세요. 힘들어요. 너무 더워요. 그래도 행복해야해요. 왜냐하면 행복하면 더위를 잊을수 있어요.
"""

count_word(a, "요.")