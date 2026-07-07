"""
Smart Network Analyzer

Main entry point of the application.
"""

APP_NAME = "Smart Network Analyzer"
APP_VERSION = "0.1.0"


def main():
    print("=" * 40)
    print(APP_NAME)
    print(f"Version {APP_VERSION}")
    print("=" * 40)
    print()
    print("Application started successfully.")
    print(main.__doc__)

if __name__ == "__main__":
    main()