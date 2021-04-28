class Bread():
    def __init__(self,ty_bread,butter,black_pepper,cucumber,corn):
        self.ty_bread = ty_bread
        self.butter = butter
        self.black_pepper = black_pepper
        self.cucumber = cucumber
        self.corn = corn
    
    def feedback(self):
        print("thanks for visiting our shop ")
        input("please enter your rating  from 1-5 ") 
          
      
    def serve(self):
        print("your order is ready ")


print("Welcome to our Bread shop ")
name = input("please enter your name ")
bread = input("please choose your Bread Rolls (Semmeln oder Brötchen)/Farm Bread (Landbrot)/Five Seed Bread (Fünfkornbrot) / Pretzels (Brezel)/Pumpernickel (Pumpernickel)/Sunflower Seed Bread (Sonnenblumenbrot)/ three Seed Bread (Dreikornbrot) / Whole grain rye bread (Katenbrot) ")
butter = input("mention Yes/No ")
black_pepper = input("please mention if pepper is required Yes or No ")
cucumber = input("please mention if cucumber is required Yes or No")
corn = input("please mention if corn is required Yes or No ")

plate = Bread(bread,butter,black_pepper,cucumber,corn)
plate.serve()
print("Dear ",name)
plate.feedback()



