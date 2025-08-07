"""
ASSIGNMENT: Login and Registration Portal System

OBJECTIVE:
Create a simple command-line user management system that allows/prompts users to register new accounts, 
login to existing accounts, and optionally verify their accounts for a fee.

REQUIREMENTS:

1. SYSTEM SETUP:
   - Create a verification cost of 1500 (stored in a variable)
   - Initialize an empty variable "users_db" to store user data for all users
   - Display a welcome portal with clear instructions (provided in code below)

2. MAIN MENU:
   - Present users with a formatted welcome message showing available commands
   - Accept user input for either "login" or "register" (case-insensitive)
   - Handle invalid commands with appropriate error messages

3. REGISTRATION FUNCTIONALITY:
   - Prompt user for username, password, and initial balance
   - Check if username already exists in "users_db" (prevent duplicates)
   - Store new user with the following data structure:
     * username (string)
     * password (string)
     * balance (float)
     * is_verified (boolean, default: False)
   - Display success message and user information after creation

4. VERIFICATION SYSTEM (Post-Registration):
   - After successful registration, offer optional account verification
   - Show verification cost and prompt user for yes/no decision
   - If user chooses "yes":
     * Check if user has sufficient balance
     * If sufficient: deduct verification cost and set is_verified to True
     * If insufficient: display error message with current balance and required amount
   - Regardless of verification choice (whether the user wishes to verify or not), display "Login successful!" and user info

5. LOGIN FUNCTIONALITY:
   - Prompt user for username and password
   - Validate that username exists in the system
   - Verify password matches stored password
   - Display appropriate success or error messages:
     * Success: "login successful!" + user information
     * Username not found: f"user {username} does not exists"
     * Wrong password: f"password mismatch for {username}"

6. DATA STRUCTURE:
   Each user should have the following details:

    -> "username"
    -> "password"
    -> "balance"
    -> "is_verified"
   

7. OUTPUT FORMATTING:
   - Include clear command instructions
   - Display user information after successful operations

TECHNICAL REQUIREMENTS:
- Use appropriate data types (string, float, boolean, dict, list)
- Implement proper input validation
- Use preferred data type you think can handle storage of user details and users_db
- Handle case-insensitive input where appropriate
- Use conditional statements for flow control
- Implement proper error handling for edge cases

EXPECTED BEHAVIOR EXAMPLES:

Registration Flow:
1. User selects "register"
2. Creates username, password, enters balance
3. System confirms creation and shows user data
4. System offers verification option
5. User can accept/decline verification
6. System processes verification (if chosen) and shows final status

Login Flow:
1. User selects "login" 
2. Enters existing username and password
3. System validates credentials
4. Shows success message with user data OR appropriate error message

ERROR CASES TO HANDLE:
- Duplicate username registration
- Login with non-existent username
- Login with incorrect password  
- Insufficient balance for verification
- Invalid menu commands

STARTER CODE STRUCTURE:
- Initialize verification_amount variable
- Create empty users_db (use your preferred data type choice based on your thought)
- Build registration and login conditions
- Add verification system logic

This assignment tests your understanding of:
- Data types and data structures
- User input handling and validation
- Conditional logic and flow control
- String manipulation and formatting
- Basic error handling
- Program organization and user experience design
"""

# TODO: Implement the login and registration portal system based on the requirements above

verification_amount = 1500
users_db = [{"username":"temitope","password":4444,"balance":4000.0,"is_verified":True},{"username":"bankat","password":4444,"balance":4000.0,"is_verified":True}]            # Initialize user database with appropraite data-type


command = input( """
   *---------------------------------------*
   |      Login and Register Portal        |
   |   ________________________________    |
   |  commands:                            |
   |   enter "login" to login              |
   |   enter "register" to register        |
   *---------------------------------------*

"""
)

# Your implementation here...

if command == "register" or command == "login":
	if command == "register":
		user_name = input("Create Username: ").lower()
		pin = int(input("Create Password: "))
		balance = float(input("Enter Deposit: "))
		is_verified = False
		new_user = {"username":user_name,"password":pin,"balance":balance,"is_verified":False}
		if not any(d["username"] == new_user["username"] for d in users_db):
			print("User Registered Successfully!")
			users_db.append(new_user)
			print(users_db)
			verify = input(f"Verify your account? yes or no?:\nVerification fee: {verification_amount}: ").lower()
			if verify == "yes" and new_user["balance"] >= verification_amount:
				cost = users_db[-1]["balance"] - verification_amount
				is_verified = True
				new_user["is_verified"] = is_verified
				new_user["balance"] = cost
				print("Verification Updated Sucessfully!")
				print("Login Successful")
				print(users_db)
			elif verify == "no":
				print("Login Sucessful!")
				print(users_db)
			else:
				print("Insufficient Funds:", users_db[-1]["balance"])
				print(f"Verification fee is: {verification_amount}")
				print("Login Successful!")
				print(users_db)
		else:
			print(f"User {user_name} Already Exists")
	elif command == "login":
		user_name = input("Enter Username: ").lower()
		pin = int(input("Enter Password: "))
		registered_user = {"username":user_name,"password":pin}
		if any(d["username"] == registered_user["username"] and d["password"] == registered_user["password"] for d in users_db):
			print("Login Successful")
			print(users_db)
		elif any(d["username"] == registered_user["username"] and d["password"] != registered_user["password"] for d in users_db):
			print(f"Password mismatch for {user_name}")
		else:
			print(f"User {user_name} does not exist!")
else:
	print("Invalid Command")
	
