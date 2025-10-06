import unittest
import os
import csv

def load_results(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) races, values are dicts
        inner keys are (str) horse, values are (str) race times
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''
    
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open

    pass

        
def get_horse_results(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: race (str), horse (str), and fastest time (int) 
        max is the maximum value of speed for a horse in that race, horse is the corresponding horse with that time

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        TIP: You will need to modify time to a float. 
    '''
    
    pass
        


def get_avg_speed(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are races and vals are floats rounded to nearest whole number
        vals are the average values for all horses in the race

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        TIP: You'll have to use the round function for your average.
    '''
    pass
        
            

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.race_dict = load_results('race_results.csv')
        self.max_tup_list = get_horse_results(self.race_dict)
        self.month_avg_dict = get_avg_speed(self.race_dict_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

#def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
