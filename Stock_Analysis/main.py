from agents.manager_agent import chat_with_agent

def main():

    print("=" * 70)
    print("        📈 AI STOCK ANALYSIS ASSISTANT")
    print("=" * 70)

    print("\nFeatures Available:")
    print("• Analyze any NSE-listed company")
    print("• Compare two companies")
    print("• View latest company news")
    print("• Manage portfolio")
    print("• Analyze portfolio")
    print("• Follow-up conversations with memory")

    print("\nExamples:")
    print("• Analyze Infosys")
    print("• Compare Infosys and TCS")
    print("• What is the PE ratio of Reliance?")
    print("• Add Infosys to my portfolio")
    print("• Show portfolio")
    print("• Analyze portfolio")

    while True:

        user_query = input(
            "\nAsk a question (type 'exit', 'quit' or 'bye' to quit): "
        )
        if user_query.strip().lower() in ["exit", "quit", "bye"]:
            print("\nThank you for using AI Stock Analysis Assistant!")
            break

        print("\nGenerating analysis...\n")

        try:
            response = chat_with_agent(user_query)

            print(response)

        except Exception as e:

            print("\n" + "=" * 70)
            print("❌ Oops! Something went wrong.")
            print("=" * 70)

            print(f"\nError: {e}")

            print("\nPlease try again or use a different query.")

if __name__ == "__main__":
    main()
    