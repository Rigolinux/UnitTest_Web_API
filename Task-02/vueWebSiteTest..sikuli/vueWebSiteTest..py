
if exists("1726791582033.png"):
    click("1726791582033.png");
    type("https://vuejs.org/");
    type(Key.ENTER);
wait(0.5);

if exists("1726707879561.png"):
    click("1726707864914.png")

click("1726706798060.png");


# if this alert display
if exists("1726707940058.png"):
    click("1726708085741.png");


# search an element in the body
searchFunction = "searchFunction.png"

while not exists(searchFunction):
    wheel(WHEEL_DOWN, 2)  
    wait(0.2)  
print("Function founded");

click("1726708728706.png");

if exists("1726708756287.png"):
    click("1726708832506.png");
    type("Props");
    type(Key.ENTER);
    if exists("1726709195250.png"):
        print("Element Founded");
wait(1);

print("Exit Test.");

vuelogo = "1726788548390.png";

while exists(vuelogo):
    click("1726788488588.png");
    wait(0.2);  

