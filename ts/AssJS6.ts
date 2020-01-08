const inlist = [[["firstName", "Vasanth"], ["lastName", "Raja"], ["age", 24], ["role", "JSWizard"]], [["firstName", "Sri"], ["lastName", "Devi"], ["age", 28], ["role", "Coder"]]];

function transform(list){
let valu={};
let i=0;
const final=[];

for(const ab of list)
{
	for(const [a,b] of ab)
    {
        valu[a] =b;
    }
    final[i] = valu;
    valu={};
    i+=1;
}
console.log(JSON.stringify(final));
}
