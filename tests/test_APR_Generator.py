import pytest
import APR_Generator
from Sample_Data_Structure import Students

students = Students

@pytest.mark.parametrize("All_Assignments", students )
def test_assignment_filter(All_Assignments):
    passed_assignments = 0
    expected_passed_assignments = 0
    failed_assignments = APR_Generator.assignment_filter(All_Assignments)
    for assignment in failed_assignments:
        if assignment > 60:
            passed_assignments += 1
            assert expected_passed_assignments != passed_assignments
    assert expected_passed_assignments == passed_assignments