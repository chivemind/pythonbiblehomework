import random

#Create general properties of Coin class
#Send dictionary info from specific types of coins into kwargs
class Coin:
    def __init__(self, rare = False, clean = True, heads=True,**kwargs):
        
        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

#Create a way to make every type of coin's value change depending on rarity
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

#Revert every type of coin to original color when clean
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rust_color
        
#Create a Constructor to Rust
    def rust(self):
        self.color = self.rust_color
        
#Create a Constructor to Clean coin
    def clean(self):
        self.color = self.clean_color
        
#Create a Constructor to Spend coin
    def __del__(self):
        print("Coin spent")
        
#Create a Constructor to Flip coin
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
        
        if choice == True:
            print("Heads!")
        else:
            print("Tails!")

#Create a way to clean up text when printed
    def __str__(self):
        if self.original_value >= 1:
            return"${}coin".format(int(self.original_value))
        else:
            return"{}p Coin".format(int(self.original_value*100))

#Create Pound class that inherits values from Coin class
#Give Pound coin a dictionary containing specific data (clean/rust color, value, etc)
class One_Pound(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_color":"gold",
            "rust_color":"green",
            "num_edges":1.0,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5,
            }

#Use parent "super" class "Coin" to take data from dictionary and set up the rest
#Unpack data from dictionary using kwarg **
        super().__init__(**data)

#Create Pence class
class One_Pence(Coin):
    def __init__(self):
        
        data = {
            "original_value":.01,
            "clean_color":"bronze",
            "rust_color":"brown",
            "num_edges":1.0,
            "diameter":20.3,
            "thickness":1.52,
            "mass":3.56,
            }

        super().__init__(**data)
        
#Create Five_Pence class
class Five_Pence(Coin):
    def __init__(self):
        
        data = {
            "original_value":.05,
            "clean_color":"silver",
            "rust_color":None,
            "num_edges":1.0,
            "diameter":18.0,
            "thickness":1.77,
            "mass":3.25,
            }

        super().__init__(**data)
#Polymorphism applies here because the "Five Pence" coin is made of silver and doesn't rust, so the Rust principle from Parent class doesn't apply
#Create a Constructor to override Parent Rust & Clean constructors        
        def rust(self):
            self.color = self.clean_color
            
        def clean(self):
            self.color = self.clean_color
            
#Create Ten Pence coin
class Ten_Pence(Coin):
    def __init__(self):
        
        data = {
            "original_value":.10,
            "clean_color":"silver",
            "rust_color":None,
            "num_edges":1.0,
            "diameter":24.5,
            "thickness":1.85,
            "mass":6.5,
            }

        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color
            
        def clean(self):
            self.color = self.clean_color
            
#Create Twenty Pence coin
class Twenty_Pence(Coin):
    def __init__(self):
        
        data = {
            "original_value":.20,
            "clean_color":"silver",
            "rust_color":None,
            "num_edges":7.0,
            "diameter":21.4,
            "thickness":1.7,
            "mass":5.0,
            }

        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color
            
        def clean(self):
            self.color = self.clean_color
            
#Create 50 Pence coin
class Fifty_Pence(Coin):
    def __init__(self):
        
        data = {
            "original_value":.50,
            "clean_color":"silver",
            "rust_color":None,
            "num_edges":7.0,
            "diameter":27.3,
            "thickness":1.78,
            "mass":8.0,
            }

        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color
            
        def clean(self):
            self.color = self.clean_color
            
#Create Two Pound coin
class Two_Pound(Coin):
    def __init__(self):
        data = {
            "original_value":2.00,
            "clean_color":"gold",
            "rust_color":"green",
            "num_edges":1.0,
            "diameter":28.4,
            "thickness":2.50,
            "mass":12.00,
            }
            
        super().__init__(**data)
        
coins = [One_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(),
         Fifty_Pence(), One_Pound(), Two_Pound()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]
    
    string = "{} - Color:{}, Value:{}, Diameter(mm):{}, Thickness(mm):{}, Num. of Edges:{}, Mass(g):{}".format(*arguments)
    print(string)
    
    