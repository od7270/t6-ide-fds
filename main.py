import logging
import sys
import traceback

from src.calculator import add, subtract, multiply, divide


# -----------------------------
# Logging configuration
# -----------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# -----------------------------
# Calculator controller
# -----------------------------

def calculate(a, b, choice):
    logger.debug(
        "calculate() called with a=%s, b=%s, choice=%s",
        a,
        b,
        choice
    )

    if choice == "1":
        logger.info("Performing addition")
        return add(a, b)

    elif choice == "2":
        logger.info("Performing subtraction")
        return subtract(a, b)

    elif choice == "3":
        logger.info("Performing multiplication")
        return multiply(a, b)

    elif choice == "4":
        logger.info("Performing division")
        return divide(a, b)

    else:
        logger.warning("Invalid operation selected: %s", choice)
        return "Invalid choice."


# -----------------------------
# Main program
# -----------------------------

def main():

    print("===== Simple Calculator =====")

    # Command-line arguments
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        choice = sys.argv[3]

        logger.debug("Using command-line arguments")

    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice: ")

    logger.debug(
        "Input received: a=%s, b=%s, choice=%s",
        a,
        b,
        choice
    )

    try:
        # Use this breakpoint to practice:
        # n - step over
        # s - step into
        # c - continue
        # p - print
        # pp locals() - inspect local variables
        # w - show call stack
        # u - move up the stack
        # d - move down the stack
        breakpoint()

        result = calculate(a, b, choice)

        logger.info("Calculation completed successfully")

        print("\nResult:", result)

    except Exception:
        logger.error("An error occurred during calculation")

        print("\nAn error occurred:")
        traceback.print_exc()


if __name__ == "__main__":
    main()