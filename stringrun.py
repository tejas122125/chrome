code  = """import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Player.csv')

batting_hand_counts = df['Batting_Hand'].value_counts()
batting_hand_counts.plot(kind='bar')
plt.title('Batting Hand Distribution')
plt.xlabel('Batting Hand')
plt.ylabel('Count')
plt.savefig('chart.png')"""
exec(code)