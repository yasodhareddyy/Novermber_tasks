from collections import defaultdict

def top_k_students(positive_feedback, negative_feedback, report, student_id, k):
    feedback_points = defaultdict(int)
    for i in range(len(report)):
        words = report[i].split()
        for word in words:
            if word in positive_feedback:
                feedback_points[student_id[i]] += 3
            elif word in negative_feedback:
                feedback_points[student_id[i]] -= 1

    sorted_students = sorted(feedback_points.keys(), key=lambda x: (feedback_points[x], -x), reverse=True)

    return sorted_students[:k]

# Example usage:
positive_feedback = ["smart", "brilliant", "studious"]
negative_feedback = ["not"]
report = ["this student is studious", "the student is smart"]
student_id = [1, 2]
k = 2

result = top_k_students(positive_feedback, negative_feedback, report, student_id, k)
print(result)

