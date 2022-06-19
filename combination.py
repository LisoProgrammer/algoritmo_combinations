
def combinacion(n_nums, n_select):
  combination_n = factorial(n_nums)/(factorial(n_select)*factorial(n_nums - n_select))
  return combination_n
