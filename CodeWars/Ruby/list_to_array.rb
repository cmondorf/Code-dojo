list = {'value'=>1, 'next'=>{'value'=>2, 'next'=>{'value'=>3, 'next'=>nil}}}

def list_to_array(list)
  list.each do |head, tail|
    if tail == nil
      return
  end

end

puts list_to_array(list)
