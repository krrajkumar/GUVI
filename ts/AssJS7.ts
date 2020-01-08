const expected = {foo: 5, bar: 6};
const actual = {foo: 5, bar: 6};
function ObjectsEqual(actual, expected)
{
 if(JSON.stringify(actual) == JSON.stringify(expected))
 {
 console.log("PASSED");
 }
 else
 {
 console.log("FAILED");
 }
}
ObjectsEqual(actual, expected);