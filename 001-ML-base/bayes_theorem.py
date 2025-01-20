





def bayes_theorem(p_a, p_b_given_a, p_b):
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

# P(A)
p_a = 0.10

# P(B|A)
p_b_given_a = 0.07

# P(B|not A)
p_b = 0.05

# calculate P(A|B)
result = bayes_theorem(p_a, p_b_given_a, p_b)

# summarize
print('P(A|B) = %.2f%%' % (result * 100))