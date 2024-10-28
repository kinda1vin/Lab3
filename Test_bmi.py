import submoudleLab2.bmi as bmi

print("Test_bmi")

def test_bmi_overweight() : 
    assert bmi.calculate_bmi(1.73, 90) == 1
    
def test_bmi_normal_weight() :
    assert bmi.calculate_bmi(1.73, 70) == 0

def test_bmi_underweight() :
    assert bmi.calculate_bmi(1.73, 50) == -1
    
