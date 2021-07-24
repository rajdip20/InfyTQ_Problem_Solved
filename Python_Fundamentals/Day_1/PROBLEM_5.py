''' JIT University offering degree courses to students has decided to provide
scholarship based on the following details:

Branch of study     |       Score (%)    |      Scholarship %   |       Remarks
                    |                    |                      |
Arts                |      Score is at   |           50         |   The student is
                    |       least 90     |                      |   eligible only for
                    |                    |                      |   one scholarship%
                    |                    |                      |   even if both the
Arts                |      Score is an   |           5          |   score conditions
                    |      odd number    |                      |   are valid for the
                    |                    |                      |   given branch of
Engineering         |      Score is      |           50         |   study. In such
                    |      more          |                      |   cases, students
                    |      than 85       |                      |   are eligible for
                    |                    |                      |   the highest
Engineering         |      Score is      |           5          |   scholarship%
                    |      divisible     |                      |   applicable
                    |      by 7          |                      |   among the two.

 If there are 500 students who have joined the university, write a code to
calculate and display the final fees to be paid by each student.
You may accept the branch of study, score and course fee as inputs for each
student and calculate the final fees to be paid by each student based on
formulae given below:
Scholarship amount=course fee * (scholarship%)
Final fee= course fee - scholarship amount '''

while True:
    branch = input("Arts or Engineering?[A/E] ")
    score = int(input("Enter the student's score: "))
    fees = int(input("Enter the fees for the course: "))
    scholarships = [0, 0]

    if branch.upper() == 'A':
        if score >= 90:
            scholarships[0] = 0.5
        if score % 2 != 0:
            scholarships[1] = 0.05
    elif branch.upper() == 'E':
        if score > 85:
            scholarships[0] = 0.5
        if score % 7 == 0:
            scholarships[1] = 0.05

    max_scholarship = max(scholarships)
    final_fee = fees - fees * max_scholarship
    print(final_fee)
    ch = input("Do you want to continue?[Y/N] ")

    if ch.upper() == 'N':
        break
