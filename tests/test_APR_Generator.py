import pytest
from APR_Generator import assignment_filter
from Sample_Data_Structure import Students

students = Students

<<<<<<< HEAD
#def test_apr_generator(current_grade: int, student_name: str, assigned_class: str, days_missed: int):

=======
@pytest.mark.parametrize("All_Assignments", students )
def test_assignment_filter(All_Assignments):
    passed_assignments = 0
    expected_passed_assignments = 0
    failed_assignments = assignment_filter(All_Assignments)
    for assignment in failed_assignments:
        if assignment > 60:
            passed_assignments += 1
            assert expected_passed_assignments != passed_assignments
    assert expected_passed_assignments == passed_assignments
>>>>>>> a3ad3707527ecc767ddc42e1beedf0b0535510ff
