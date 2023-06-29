
savings = 0;
toolList = "";
tool = "";
buyTool = "";


toolBox= {
0:{
    'tool': 'teeth',
    'cost': 0,
    'income': 1,
    'inTheBox': 'true'
},
1:{
    'tool': 'pair of scissors',
    'cost': 5,
    'income': 5,
    'inTheBox': 'false'
},
2:{
    'tool': 'used mower',
    'cost': 25,
    'income': 50,
    'inTheBox': 'false'
},
3:{
    'tool': 'new mower',
    'cost': 250,
    'income': 100,
    'inTheBox': 'false'
},
4:{
    'tool': 'team of robot students',
    'cost': 500,
    'income': 250,
    'inTheBox': 'false'
}};

#print(toolBox);

# function buildToolList() {
#   for (i = 0; i < 5; i++) {
#     if (toolBox[i].inTheBox === true) {
#       toolList = toolList + "[" + i + "] " + toolBox[i].tool + "\n"
#     }
#   }
#   console.log(toolList);
# }

def buildToolList():
    i=0;
    global toolList;
    for tool in toolBox:
        if toolBox[i]['inTheBox'] == 'true':
            toolList = toolList + "[" + str(i) + "] " + toolBox[i]['tool'] + "\n"
        i=i+1;

    print(toolList);

   
# function incrementSavings(tool) {
#   savings = savings + toolBox[tool].income;
#   console.log("Congrats! You earned " + toolBox[tool].income +
#     " dollar(s) cutting grass with your " + toolBox[tool].tool + ".\n");

# }

def incrementSavings(tool):
    global savings;
    savings = savings + int(toolBox[tool]['income']);
    print("Congrats! You earned " + str(toolBox[tool]['income']) +
     " dollar(s) cutting grass with your " + toolBox[tool]['tool'] + ".\n");


# function buyATool(tool) {
#   const nextTool = parseInt(tool) + 1;

#   if (tool < 4 && toolBox[nextTool].inTheBox === false && savings >= toolBox[nextTool].cost) {
#     console.log("You have " + savings + " dollars in  your savings. Would you like to buy a " + toolBox[nextTool].tool + "?:")
#     buyTool = prompt("(y/n)");
#     if (buyTool === 'y') {
#       savings = savings - toolBox[nextTool].cost;
#       toolBox[nextTool].inTheBox = true;

#     }
#   }
# }

def buyATool(tool):
    global savings;
    global buyTool;
    nextTool = tool + 1;

    # print(tool);
    # print(savings);
    # print(toolBox[nextTool]['cost']);
    # print(savings >= toolBox[nextTool]['cost']);

    if tool < 4 and toolBox[nextTool]['inTheBox'] == 'false' and savings >= toolBox[nextTool]['cost']:
        print("You have " + str(savings) + " dollars in your savings. Would you like to buy a " + toolBox[nextTool]['tool'] + "?:")
        buyTool = input("(y/n)");

        if buyTool == 'y':
            savings = savings - toolBox[nextTool]['cost'];
            toolBox[nextTool]['inTheBox'] = 'true';    

# function main() {

#   const username = prompt('What is your name? ');
#   console.log(`Your name is ${username} and you are a landscaper!`);

#   while (savings < 1000 || toolBox[4].inTheBox === false) {

#     //pick a tool to use
#     buildToolList();
#     console.log("You have " + savings + " dollar(s) in your savings.\n")
#     console.log("Here are the tools in your toolbox. Which one would you like to use today?: ")
#     tool = prompt("");

#     //confirm tool is in the box and increment savings
#     if (toolBox[tool].inTheBox === true) {
#       incrementSavings(tool);
#       //clear tool list
#       toolList = "";

#       //offer a chance to buy a tool
#       buyATool(tool);
      
#       console.log("---------------------------------------------------------------");

#     }
#     else {
#       console.log("Uh oh. You picked a tool that isn't in your toolbox.")
#       toolList = "";
#     }
#   }
#   console.log("---------------------------------------------------------------");
# console.log("Congrats! You earned " + savings + " dollars! Now you can retire!");
# console.log("---------------------------------------------------------------");
# console.log("---------------------------THE END------------------------------");
# console.log("---------------------------------------------------------------");
# }


def main():

    global savings;
    global tool;
    global toolList;

    username = input('What is your name? ');
    print('Your name is ' + username + ' and you are a landscaper!');

    while savings < 1000 or toolBox[4]['inTheBox'] == 'false':
        
        #pick a tool to use
        buildToolList();
        print("You have " + str(savings) + " dollar(s) in your savings.\n")
        print("Here are the tools in your toolbox. Which one would you like to use today?: ")
        tool = int(input(""));

        #confirm tool is in the box and increment savings
        if toolBox[tool]['inTheBox'] == 'true':
            incrementSavings(tool);
            
            #clear tool list
            toolList = "";

            #offer a chance to buy a tool
            buyATool(tool);
        
            print("---------------------------------------------------------------");

        else: 
            print("Uh oh. You picked a tool that isn't in your toolbox.")
            toolList = "";
        
    print("---------------------------------------------------------------");
    print("Congrats! You earned " + str(savings) + " dollars! Now you can retire!");
    print("---------------------------------------------------------------");
    print("---------------------------THE END------------------------------");
    print("---------------------------------------------------------------");

main();