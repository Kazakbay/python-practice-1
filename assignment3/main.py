import os
import sys
import csv
import json


def main():
    print("Checking file...")
    filename = "students.csv"


    if not os.path.exists(filename):
        print(f"Error: {filename} not found. Please download the file from LMS.")
        sys.exit()
    else:
        print(f"File found: {filename}")

    print("Checking output folder...")
    output_dir = "output"


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Output folder created: {output_dir}/")



    students = []

    # Open and read the CSV
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    print(f"Total students: {len(students)}")
    print("First 5 rows:")
    print("-" * 30)

    # Print the first 5 rows
    for row in students[:5]:
        print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
    print("-" * 30)



    sorted_students = sorted(students, key=lambda x: float(x['final_exam_score']), reverse=True)
    top10 = sorted_students[:10]

    print("-" * 30)
    print("Top 10 Students by Exam Score")
    print("-" * 30)

    # Print top 10 students
    for i in range(len(top10)):
        rank = i + 1
        student = top10[i]
        print(
            f"{rank}. {student['student_id']} | {student['country']} | {student['major']} | Score: {float(student['final_exam_score'])} | GPA: {student['GPA']}")
    print("-" * 30)


    top_10_list = []
    for i in range(len(top10)):
        student = top10[i]
        top_10_list.append({
            "rank": i + 1,
            "student_id": student["student_id"],
            "country": student["country"],
            "major": student["major"],
            "final_exam_score": float(student["final_exam_score"]),
            "GPA": float(student["GPA"])
        })

    # Create the result dictionary
    result = {
        "analysis": "Top 10 Students by Exam Score",
        "total_students": len(students),
        "top_10": top_10_list
    }

    # Save to JSON
    output_path = os.path.join(output_dir, "result.json")
    with open(output_path, "w", encoding='utf-8') as json_file:
        json.dump(result, json_file, indent=4)

    # Print Summary
    print("=" * 30)
    print("ANALYSIS RESULT")
    print("=" * 30)
    print(f"Analysis : {result['analysis']}")
    print(f"Total students : {result['total_students']}")
    print(f"Top 10 saved to {output_dir}/result.json")
    print("=" * 30)
    print(f"Result saved to {output_dir}/result.json")


if __name__ == "__main__":
    main()
