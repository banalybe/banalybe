puts "input1"
text = gets.chomp
puts "input2"
redact = gets.chomp
words = text.split(" ")
words.each do |word|
  if word == redact
    print "REDACTED "
  else
    print word + " "
    end
end
