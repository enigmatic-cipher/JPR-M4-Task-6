"""
Given a string as input, find the first index of X in the string. Then print the string from the beginning to the first index of X and then after X to the end of the string.
Input-> "WOWXMAS"
Output-> First:WOW Second:MAS
"""

st = "WOWXMAS"
ln = len(st)
for i in range(0,ln):
  ch = st[i]
  if (ch=="X"):
    print(f"first:{st[0:i]}")
    print(f"Second:{st[i+1:ln]}")
    