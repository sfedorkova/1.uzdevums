teksts = input ("Ievadi tekstu: ")
def reverseSentence(teksts):
  sar1 = teksts.split(";")
  if len(sar1)>2:
    sar1.reverse()
    teksts = ""
    for elements in sar1:
      teksts += elements + ""
    print(teksts)
  else:
    teksts = "parak iss teikums"
    print(teksts)
  return teksts
reverseSentence(teksts)