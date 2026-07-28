from client import VendorQuoteComparatorClient

def main():
    client = VendorQuoteComparatorClient()
    res = client.compare_quotes(quotes=[{'vendor': 'A', 'price': 100}, {'vendor': 'B', 'price': 80}])
    print(f"Result for cheapest_vendor: {res['cheapest_vendor']}")

if __name__ == "__main__":
    main()
