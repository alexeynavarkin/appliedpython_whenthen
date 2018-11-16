from unittest import TestCase

from whenthen import whenthen


class BaseTest(TestCase):
    def test_base(self):
        @whenthen
        def test(num):
            return num

        @test.when
        def test(num):
            if num == 8:
                return True

        @test.then
        def test(num):
            return "Gotcha"


        self.assertEqual("Gotcha", test(8))
        self.assertEqual(0, test(0))

    def test_multiple_conditions(self):
        @whenthen
        def test(num):
            return num

        @test.when
        def test(num):
            if num == 8:
                return True

        @test.then
        def test(num):
            return "Gotcha 8"

        @test.when
        def test(num):
            if num == 101:
                return True

        @test.then
        def test(num):
            return "Gotcha 101"

        self.assertEqual("Gotcha 8", test(8))
        self.assertEqual("Gotcha 101", test(101))
        self.assertEqual(0, test(0))

    def test_multiple_functions(self):
        @whenthen
        def test(num):
            return num

        @test.when
        def test(num):
            if num == 8:
                return True

        @test.then
        def test(num):
            return "Gotcha 8"

        @whenthen
        def test_2(num):
            return num

        @test_2.when
        def test_2(num):
            if num == 101:
                return True

        @test_2.then
        def test_2(num):
            return "Gotcha 101"

        self.assertEqual("Gotcha 8", test(8))
        self.assertNotEqual("Gotcha 101", test(101))
        self.assertEqual("Gotcha 101", test_2(101))
        self.assertNotEqual("Gotcha 8", test_2(8))
        self.assertEqual(0, test(0))
        self.assertEqual(0, test_2(0))

    def test_wrong_order_1(self):
        @whenthen
        def test(num):
            return num

        with self.assertRaises(ValueError):
            @test.then
            def test(num):
                return "Gotcha"

    def test_wrong_order_2(self):
        @whenthen
        def test(num):
            return num

        @test.when
        def test(num):
            if num == 8:
                return True

        with self.assertRaises(ValueError):
            @test.when
            def test(num):
                if num == 8:
                    return True

    def test_wrong_order_3(self):
        @whenthen
        def test(num):
            return num

        @test.when
        def test(num):
            if num == 8:
                return True

        @test.then
        def test(num):
            return "Gotcha"

        with self.assertRaises(ValueError):
            @test.then
            def test(num):
                return "Gotcha"