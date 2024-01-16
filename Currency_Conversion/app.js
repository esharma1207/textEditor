let rate1 = document.querySelector(".rate1");
let rate2 = document.querySelector(".rate2");
let resultbutton = document.querySelector(".result");
let select = document.querySelectorAll(".options select");
let sel1 = select[0];
let sel2 = select[1];
let inputs = document.querySelectorAll(".input input")
let inp1 = inputs[0];
let inp2 = inputs[1];

let rates = {};
let URL = "http://data.fixer.io/api/latest?access_key=8ff9f619f39c5a50e67aa78f7faffeb7";

fetchRates();

async function fetchRates(){
    let res = await fetch(URL);
    res = await res.json();
    rates = res.rates;
    populateOptions();


}

async function populateOptions(){
    let val = "";
    Object.keys(rates).forEach(code =>{
        let str = `<option value = "${code}">${code}</option>`;
        val += str;
    })
    select.forEach((s) => (s.innerHTML = val));
}

function convert(value, init_curr, target_curr)
{
    let v = (value/rates[init_curr]) * rates[target_curr];
    let v1 = v.toFixed(3);
    return v1 == 0.0 ? v.toFixed(5) : v1;

}

function displayRate(){
    let v1 = sel1.value;
    let v2 = sel2.value;
    let val = convert(1, v1, v2);
    rate1.innerHTML = `1 ${v1} equals `;
    rate2.innerHTML = `${val} ${v2}`;

}

resultbutton.addEventListener("click",() =>{
    let initial_curr = sel1.value;
    let initial_val = parseFloat(inp1.value);
    let target_curr = sel2.value;
    if(isNaN(initial_val)){
        alert("Enter a number");

    }
    else{
        let cval = convert(initial_val, initial_curr, target_curr);
        inp2.value = cval;
    }

}
 );
 select.forEach(s => s.addEventListener("change", displayRate));

 document.querySelector(".swap").addEventListener("click", () => {
    let in1 = inp1.value;
    let in2 = inp2.value;
    let out1 = sel1.value;
    let out2 = sel2.value;

    inp2.value = in1;
    inp1.value = in2;
    sel2.value = out1;
    sel1.value = out2;

    displayRate();

 })


