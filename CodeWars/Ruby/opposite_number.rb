#opposite
def opposite(input_number)
  abs_value = input_number.to_f.abs
 if abs_value == input_number.to_f
   return input_number.to_f * (- 1)
 else
   return abs_value
 end
end

puts opposite(1)

puts opposite(14)

puts opposite(-34)
