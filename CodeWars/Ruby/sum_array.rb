def sum_array(arr)
  if arr.nil?
    return 0
  end
  if arr.length <=1
    return 0
  end
  arr.sort!
  i = 1
  sum = 0
  while i < arr.length-1 do
    sum += arr[i]
    i += 1
  end
  return sum
end

arr = nil
puts sum_array(arr)
