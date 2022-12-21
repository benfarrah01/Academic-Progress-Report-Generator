import pytest
import superuser

@pytest.mark.parametrize("total_value, k",[(71, 100), (69, 100)])
def test_superuser_compared_to_student(total_value, k):

    superuser_score = superuser.compare_stu_super(total_value)

    student_percent = total_value/k

    if student_percent >= .7:
        assert superuser_score == False
    else:
        assert superuser_score == True

