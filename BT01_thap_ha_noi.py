n = int(input('nhập số dĩa:'))
def thaphanoi(n, cot_goc, cot_cuoi, trung_gian):
  if n == 1:
    print("Di chuyển dĩa 1 từ cột",cot_goc,"đến cột",cot_cuoi)
    return
  thaphanoi(n-1, cot_goc, trung_gian, cot_cuoi)
  print ("Di chuyển dĩa ",n,"từ cột",cot_goc,"đến cột",cot_cuoi)
  thaphanoi(n-1, trung_gian, cot_cuoi, cot_goc)
print(thaphanoi(n,"gốc","cuối","trung gian"))