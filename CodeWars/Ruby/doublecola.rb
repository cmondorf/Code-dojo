def whoIsNext(names, r)
  # your code
  next_in_line = 0
  adding = names.length
  while adding <= r do
    add_this = Array.new(2, names[next_in_line])
    names = names + add_this
    next_in_line += 1
    adding += 2
  end
  return names[r]
end



puts whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1)#=="Sheldon"
