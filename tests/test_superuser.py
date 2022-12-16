import pytest
import superuser

@pytest.mark.parametrize("total_value, k", [])
def test_superuser_compared_to_student(total_value, k):

    superuser_score = superuser.compare_stu_super(total_value)
