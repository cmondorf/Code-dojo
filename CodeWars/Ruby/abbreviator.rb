
# Write a function that takes a string and turns any and all "words" (see below)
# within that string of length 4 or greater into an abbreviation following the same rules.
#
# A "word" is a sequence of alphabetical characters. By this definition,
# any other character like a space or hyphen (eg. "elephant-ride") will
# split up a series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the
# number of removed characters, then the last letter (eg. "elephant ride" => "e6t-r2e").

class Abbreviator

  def self.abbreviate(string)
    # abbreviate the string

    # check if input string is longer than 4 letters
    
  end

end





puts Abbreviator.abbreviate("banana")
# "b4a"
puts Abbreviator.abbreviate("double-barrel")
# "d4e-b4l"
puts Abbreviator.abbreviate("You, and I, should speak.")
# "You, and I, s4d s3k."
