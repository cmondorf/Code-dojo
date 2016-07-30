def makeNegative(num)
  if num > 0
    return - num
  else
    return num
  end
end

puts "testing"

puts makeNegative(1); # return -1
puts makeNegative(-5); # return -5
puts makeNegative(0); # return 0
