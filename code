import pickle
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description):
        self.transactions.append({'amount': amount, 'category': category, 'description': description})

    def filter_expenses(self, threshold):
        return [t for t in self.transactions if t['amount'] > threshold]

    def save_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.transactions, f)

    def load_data(self, filename):
        with open(filename, 'rb') as f:
            self.transactions = pickle.load(f)

    def plot_monthly_spending(self):
        categories = {}
        for t in self.transactions:
            categories[t['category']] = categories.get(t['category'], 0) + t['amount']
        
        plt.bar(categories.keys(), categories.values())
        plt.xlabel('Categories')
        plt.ylabel('Spending Amount')
        plt.title('Monthly Spending')
        plt.show()


# Example usage
tracker = FinanceTracker()
tracker.add_transaction(150, 'Food', 'Grocery shopping')
tracker.add_transaction(200, 'Entertainment', 'Movie night')
tracker.add_transaction(50, 'Food', 'Lunch')
tracker.save_data('transactions.pkl')
tracker.load_data('transactions.pkl')
print("Filtered Expenses over $100:", tracker.filter_expenses(100))
tracker.plot_monthly_spending()
