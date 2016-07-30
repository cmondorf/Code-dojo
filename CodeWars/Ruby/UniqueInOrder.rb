def unique_in_order(iterable)
  output = Array.new
  if iterable.empty?
    return output
  end
  counter = 0
  output << iterable[counter]
  while counter < iterable.length
    if output.last == iterable[counter + 1]
      counter += 1
    else
      if iterable[counter + 1] != nil
        output << iterable[counter + 1]
      end
      counter += 1
    end
  end
  return output
end


puts unique_in_order('AAAABBBCCDAABBB') #== ['A', 'B', 'C', 'D', 'A', 'B']
puts unique_in_order('ABBCcAD')         #== ['A', 'B', 'C', 'c', 'A', 'D']
puts unique_in_order([1,2,2,3,3])       #== [1,2,3]
