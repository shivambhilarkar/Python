
def largest(num):
  num_str = str(num)
  i = 9
  while i >= 0:
    if str(i) in num_str:
      return i
    i -= 1


def smallest(num):
  num_str = str(num)
  i = 0
  while i <= 9:
    if str(i) in num_str:
      return i
    i += 1


def pairs_from(num):
  if num == 2:
    return 1
  if num >= 3:
    return 2
  return 0


T = int(input())
for c in range(T):
  N = int(input())
  nums = list(map(int, input().split()))
  assert(len(nums) == N)
  bitscores = [""]*N
  for i in range(len(bitscores)):
    c_scr = str(11*largest(nums[i]) + 7*smallest(nums[i]))
    if len(c_scr) > 2 :
      c_scr=c_scr[-2:]
    bitscores[i]=c_scr

  odd_pose=[0]*10
  even_pose=[0]*10

  for i in range(len(bitscores)):
    index=int(bitscores[i][0])
    if (i+1) % 2 == 0:
        even_pose[index] += 1
    else:
        odd_pose[index] += 1

  count_pairs=[0]*10

  for i in range(10):
    if even_pose[i] <= 1 and odd_pose[i] <= 1:
      continue
    count_pairs[i] += pairs_from(even_pose[i]) + pairs_from(odd_pose[i])
    count_pairs[i]=min(2, count_pairs[i])
  print(sum(count_pairs))
