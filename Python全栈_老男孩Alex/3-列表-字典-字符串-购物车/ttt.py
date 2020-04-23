data={
  '北京':{
        "昌平":{
              "沙河":["oldboy","test"],
              "天通苑":["链家","我爱我家"],
        },
        "朝阳":{
              "望京":["奔驰","默默"],
              "国贸":["CICC","HP"],
              "东直门":["Advent","飞信"],
        },
        "海淀":{
            "望京": ["奔驰", "默默"],
            "国贸": ["CICC", "HP"],
            "东直门": ["Advent", "飞信"],
        },
  },
  '山东':{
        "德州":{},
        "青岛":{},
        "济南":{},
  },
  '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
  },
}

while True:
  for i in data:
    print(i)

  choice=input("选择进入1>>:")
  if choice in data:
    while True:
      for i2 in data[choice]:
          print("\t",i2)
      choice2 = input("选择进入>>2:")
      if choice2 in data[choice]:
        while True:
          for i3 in data[choice][choice2]:
              print("\t\t", i3)
          choice3 = input("选择进入>>3:")
          if choice3 in data[choice][choice2]:
            for i4 in data[choice][choice2][choice3]:
                print("\t\t",i4)
            choice4 = input("最后一层，按q返回上一级：")
            if choice4 == "b":
                pass #什么也不做,占位符，让代码不出错
          if choice3 =="q":
             break
      if choice2 == "q":
        break