studentscore = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

studentgrades = {}
x = studentgrades.__setitem__
for i in studentscore:
  # print(studentscore[i])
  if studentscore[i] >= 91 <= 100:
    q = 'outstanding'
    x(i, q)
  elif studentscore[i] >= 81 <= 90:
    q = 'exceed expectation'
    x(i, q)
  elif studentscore[i] >= 71 <= 80:
    q = 'accept'
    x(i, q)
  else:
    q = 'failed'
    x(i, q)

print(studentgrades)
