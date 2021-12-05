require 'socket'

s = TCPSocket.new 'localhost', 6001

s.puts "I'm a client!"

line = s.gets
puts line