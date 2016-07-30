def prime_factors(n)
  factors = []
  factor = 2
  division = 0
  while division != 1 do
    # if n%factor == 0
    #   while n%factor == 0 do
    #     factor += 1
    #   end
    # end
    if n / factor != 1
      n = n/factor
      factors <<  factor
      division = n
    end
  end
  return factors
end


puts prime_factors(12)
puts prime_factors(9)
