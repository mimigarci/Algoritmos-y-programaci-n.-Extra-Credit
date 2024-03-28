class Functions:
  def __init__(self):
    pass

  def manage_options(options):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
        
    option = input("Ingrese el número de su opción: ")
    while not option.isnumeric() or int(option)-1 not in range(len(options)):
        option = input("Ingreso inválidos, ingrese el número de su opción: ")
    
    return int(option)
