
let list = [["make", "Ford"], ["model", "Mustang"], ["year", 1964]];

function listtoobject(arr){
const final={};
for(const [key, value] of arr)
{
	final[key]=value;
}
const valu=JSON.stringify(final);
console.log(valu);
}
