Test.describe("Basic tests")
Test.assert_equals(beggars([1,2,3,4,5],1),[15])
Test.assert_equals(beggars([1,2,3,4,5],2),[9,6])
Test.assert_equals(beggars([1,2,3,4,5],3),[5,7,3])
Test.assert_equals(beggars([1,2,3,4,5],6),[1,2,3,4,5,0])
Test.assert_equals(beggars([1,2,3,4,5],0),[])