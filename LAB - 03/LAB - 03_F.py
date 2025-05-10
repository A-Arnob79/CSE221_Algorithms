def post_order(in_order, pre_order):
  if not in_order or not pre_order: return []

  root = pre_order[0]
  if root in in_order: r_i = in_order.index(root)
  else: return []

  in_order__L = in_order[:r_i]
  in_order__R = in_order[r_i + 1:]

  pre_order__L = pre_order[1: r_i + 1]
  pre_order__R = pre_order[r_i + 1:]

  post_order__L = post_order(in_order__L, pre_order__L)
  post_order__R = post_order(in_order__R, pre_order__R)

  return post_order__L + post_order__R + [root]

num = int(input())
in_order = input().split()
pre_order = input().split()
in_order = [int(x) for x in in_order]
pre_order = [int(y) for y in pre_order]

x = post_order(in_order, pre_order)
print(*x)
