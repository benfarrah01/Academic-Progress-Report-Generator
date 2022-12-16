import pytest
import APR_Generator
from Sample_Data_Structure import Students

@pytest.mark.parametrize("All_Assignments, current_grade,student_name,assigned_class,days_missed", {})
def test_assignment_filter(All_Assignments):
    output = APR_Generator.assignment_filter(Students)
    expected_output = True
    if output == type(list):
        output = True
    assert expected_output == output

def test_apr_generator(current_grade: int, student_name: str, assigned_class: str, days_missed: int):

