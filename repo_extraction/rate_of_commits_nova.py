import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def scientific_notation_formatter(x, pos):
    return "{:.1e}".format(x)

file_path = "nova_authors.txt"

df = pd.read_csv(file_path, delimiter=";", names=["Commit", "Author", "Date"]).sort_values(by='Date')
df['Count'] = range(1, len(df) + 1)
print(df.head(10))

ax = sns.lineplot(x='Date', y='Count', data=df)
ax.xaxis.set_major_formatter(FuncFormatter(scientific_notation_formatter))

plt.xlabel('Time')
plt.ylabel('Commit number')
plt.title('Rate of commits over time')
plt.tight_layout()
plt.savefig("nova_rate_of commits.pdf")
plt.close()

