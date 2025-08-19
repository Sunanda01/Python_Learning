'''
Compare Semester 1 vs Semester 2 marks to find who improved/declined.
Highlight differences only in Math and Science subjects.
'''
import pandas as pd
data_sem1 = {
    'student': ['A', 'B', 'C', 'D'],
    'math': [78, 90, 65, 88],
    'science': [80, 85, 70, 92],
    'english': [75, 88, 60, 85]
}

data_sem2 = {
    'student': ['A', 'B', 'C', 'D'],
    'math': [82, 85, 70, 88],
    'science': [85, 80, 72, 95],
    'english': [78, 88, 65, 90]
}

df_sem1 = pd.DataFrame(data_sem1).set_index('student')
df_sem2 = pd.DataFrame(data_sem2).set_index('student')

print("Semester 1 Marks:\n", df_sem1, "\n")
print("Semester 2 Marks:\n", df_sem2, "\n")

# Compare Semester 1 vs Semester 2 marks to find who improved/declined.
diff=df_sem1.compare(df_sem2,align_axis="index",keep_equal=True)
print(diff)

# Highlight differences only in Math and Science subjects
print(df_sem1.compare(df_sem2,align_axis="index")[['math','science']])
print(diff[['math','science']])