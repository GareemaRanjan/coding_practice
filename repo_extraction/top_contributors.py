import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "nova_authors.txt"

freq = (
    pd.read_csv(file_path, delimiter=";", names=["Commit", "Author", "Date"])
    .groupby("Author")
    .size()
    .sort_values(ascending=False)[2:]
)

total_authors = len(freq)
df = freq[:int(total_authors/100)].reset_index()
df.columns = ['Author', 'Frequency']



sns.barplot(x='Author', y='Frequency', data=df)

plt.xlabel('Author')
plt.ylabel('Frequency')
plt.title('Top 1% Authors in Nova')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("nova_authors.pdf")
plt.close()