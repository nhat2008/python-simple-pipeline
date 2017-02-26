from pipeline import Pipeline
import unittest
import functions as functions


class PipelineTest(unittest.TestCase):
    def test_result(self):
        person = {
            'basic_information':
                {
                    'name': 'Nguyen Minh Nhat',
                    'year': '1900',
                    'address': {
                        'city': 'Ho Chi Minh',
                        'ward': '6',
                        'distrist': 'Tan Binh',
                        'street': 'Nghia Phat Street'
                    }
                }
        }
        list_str_function = ['get_information_from_persion', 'get_address', 'get_street']
        pipeline = Pipeline(functions=functions)
        result = pipeline(list_str_function, person)
        self.assertIsNotNone(result)
        self.assertEqual(result['result'], 'Nghia Phat Street')
        self.assertEqual(result['error'], '')


if __name__ == '__main__':
    unittest.main()
