def duplicate_encode(word)
  #your code here
  output = String.new
  word.upcase!
  characters = Hash.new
  word.each_char do |chr|
    if characters.key?(chr) == false
      characters[chr] = 0
    end
    characters[chr] += 1
  end
  word.each_char do |chr|
    if characters[chr] == 1
      output << '('
    else
      output << ')'
    end
  end
  return output
end

duplicate_encode("hello")
