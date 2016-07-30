def is_square num
  if num < 0
    return false
  end
  sqrt = Math::sqrt(num)
  if sqrt%1 == 0
    return true
  else
    return false
  end
end

puts is_square (-1)
