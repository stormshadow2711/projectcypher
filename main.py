from checker.strategy_factory import StrategyFactory

def main():
    print("Welcome to the Password Evaluation Tool!")
    password = input("Enter a password: ")
    
    # Check password strength
    strength_checker = StrategyFactory.get_strategy("strength")
    strength_level = strength_checker.evaluate(password)
    print(f"Password strength: {strength_level}")
    
    # Calculate time to crack the password
    time_to_crack_calculator = StrategyFactory.get_strategy("time_to_crack")
    time_to_crack = time_to_crack_calculator.evaluate(password)
    print(f"Estimated time to crack the password: {time_to_crack}")

if __name__ == "__main__":
    main()
