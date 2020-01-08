const valu = { name: "ISRO", age: 35, role: "Scientist" };
function objecttoarray(valu) {
    const arrayobject = [];
    for (const prop in valu) {
        arrayobject[arrayobject.length] = [prop, valu[prop]];
        console.log(arrayobject);
    }
}
