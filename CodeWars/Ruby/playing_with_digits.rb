def dig_pow(n, p)
    n_array = []
    n.to_s.each_char {|char| n_array << char}
    intermediate_result = 0
    index = 0
    n_array.each do |digit|
      intermediate_result += digit.to_i**(p+index)
      index += 1
    end
    target = intermediate_result/n.to_f
    if target % 1 == 0
      return target.to_i
    else
      return -1
    end
end

puts "1 = #{dig_pow(89, 1)}"
puts "-1 = #{dig_pow(92, 1)}"
puts "2 = #{dig_pow(695, 2)}"
puts "51 = #{dig_pow(46288, 3)}"
