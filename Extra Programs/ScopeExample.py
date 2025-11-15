State="Telangana"

def visit_State():
    State="Karnataka"
    def visit_StateO():
      State="Kerala"
      print(f"I'm in : {State}")
    visit_StateO()
    print(f"But I am from :{State}")

visit_State()
print(f"{State} is good")