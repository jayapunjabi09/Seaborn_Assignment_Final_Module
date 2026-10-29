import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

swiggy = pd.DataFrame({
    "order_id": range(1, 21),
    "payment_method": ["UPI", "Card", "Cash", "UPI", "UPI", "Card", "Cash", "UPI", "Card", "UPI",
                       "Cash", "UPI", "Card", "UPI", "Cash", "Card", "UPI", "UPI", "Card", "Cash"]
})

sns.countplot(data=swiggy, x="payment_method")
plt.title("Number of Orders by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.show()