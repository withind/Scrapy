def read_line(line):
  sample = {}
  n = len(line)
  for i in range(n):
    if line[i]!='0':
      sample[i] = int(line[i])
  return sample

print (read_line('10011100101'))

