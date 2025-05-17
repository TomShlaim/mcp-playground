from mcp.server.fastmcp import FastMCP

mcp = FastMCP("food")

def make_jasmino_request(serving = "Pita Kebab") -> str:
    #go to jasmino
    #Wait the line
    #order
    #pay
    #get the receipt
    #return the receipt

    return f"You got your {serving} at jasmino"

def make_rambam_request(serving = "Pita Shwarma") -> str:
    #go to rambam
    #Wait the line
    #order
    #pay
    #get the receipt
    #return the receipt

    return f"You got your {serving} at rambam"

@mcp.tool(description="Order a specific food item from Jasmino and receive a receipt.")
async def get_jasmino(serving : str) -> str:
    return make_jasmino_request(serving)

@mcp.tool(description="Order a specific food item from Rambam and receive a receipt.")
async def get_rambam(serving: str) -> str:
    return make_rambam_request(serving)

if __name__ == "__main__":
    mcp.run(transport='stdio')