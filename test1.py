#程式邏輯題目第一題
input_grades = [35, 46, 57, 91, 29]

def fix_grades(input_grades):
    corrected_grades = []
    for grade in input_grades:
        reversed_grade = int(str(grade)[::-1])
        corrected_grades.append(reversed_grade)
    return corrected_grades

corrected_grades = fix_grades(input_grades)
print(f"修正後的分數：{corrected_grades}")