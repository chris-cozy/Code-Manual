--use a double dash to comment out lines
--when coding in pico 8 using lua, all lowercase


--basic variable declaration
test_var=0
test_var2=1

--object declaration
player={
    sp=1,
    health=100,
    living=true,
}

--accessing object variables
footoo= player.sp

--if statement style
if test_var == 1 then
    return true
end

if test_var2>1 then
    print("foo")
elseif test_var2 == 1 then
    print("foofoo")
else
    print("foofoofoo")
end

--function declaration
function foo()
    --creating local variables in a function
    local x=50 local y=70
    local z="foo"
end

--you can also treat functions like variables
function _init()

end
_init=foo
