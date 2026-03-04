'''
Plot histogram of student scores.
Bin size = 5.
Add vertical line for mean score using plt.axvline().
Title: "Distribution of Exam Scores".
'''
import matplotlib.pyplot as plt
import numpy as np
scores = np.random.randint(40, 100, 50)  # 50 students' marks between 40–100
plt.hist(scores,bins=5,color="purple",edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Marks Range")
plt.ylabel("No of Students")
mean_score=np.mean(scores)
plt.axvline(mean_score,color="red",linestyle="--",label=f"Mean = {mean_score:.1f}")
plt.legend()
plt.show()
