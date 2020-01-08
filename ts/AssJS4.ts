
const valu=["GUVI","I","am","Geek"];

function firstlast(list){
	const emlist={};
	emlist[list[0]]=list[list.length-1];
	const final=JSON.stringify(emlist);
	console.log(final);
}