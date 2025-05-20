# SHIRTS = write a function called shirt that accepts a few paramaters
# and arguments. Call the function using postional and keyword arguments

def make_shirt(size, branding): # defining the function with 2 paramaters
    """Shirt size and branding"""
    print(f"""The size of the T-Shirt is {size.upper()} and the branding is """
          f"""{branding.title()}""")

make_shirt('large', 'nike') # calling the function with positional arguments
make_shirt(size='large', branding='nike')
# calling the function with keyword arguments