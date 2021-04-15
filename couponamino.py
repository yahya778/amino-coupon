
 
print("""        \\\    ///wW  Ww\\\  ///   .-.        
    /)  ((O)  (O))(O)(O)((O)(O)) c(O_O)c      
  (o)(O) | \  / |  (..)  | \ || ,'.---.`,     
   //\\  ||\\//||   ||   ||\\||/ /|_|_|\ \    
  |(__)| || \/ ||  _||_  || \ || \_____/ |    
  /,-. | ||    || (_/\_) ||  ||'. `---' .`    
 -'   ''(_/    \_)      (_/  \_) `-...-'""")

import amino
client = amino.Client()
email = input("enter your email:")
password = input("enter your password")
client = amino.Client() 
client.login(email=email, password=password)

amino.socket.claim_new_user_coupon()
 
