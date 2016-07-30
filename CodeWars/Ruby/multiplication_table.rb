def multiplication_table(row, col)
  table = Array.new
  row_counter = 1
  col_counter = 1
  current_row = Array.new
  while row_counter <= row do
    col.times do
      current_row << row_counter * col_counter
      col_counter += 1
    end
    table[row_counter-1] = current_row
    row_counter += 1
    col_counter = 1
    current_row = Array.new
  end
return table
end

puts multiplication_table(3,3)
puts multiplication_table(2,2)
