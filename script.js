
document.getElementById("currencyForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const amount = document.querySelector(".amount input").value;
    const from = document.querySelector("#fromCurrency").value;
    const to = document.querySelector("#toCurrency").value;

    if (from === to) {
      document.querySelector("#aa").innerText = `${amount} ${from} = ${amount} ${to}`
    } else {

      const url = `http://127.0.0.1:5000/convert?from=${from}&to=${to}&amount=${amount}`;

      const response = await fetch(url);
      const data = await response.json();
      if(response['status'] === 500){
        document.querySelector(".msg").innerText = `Couldn't Converted`

        document.querySelector(".aa").innerText = `Couldn't Converted`;
        document.querySelector(".aa").style.background = "#279300ff";
      }else{
        document.querySelector(".msg").innerText = `1 ${from} = ${data["rate"]} ${to}`
        
        document.querySelector(".aa").innerText = `${amount} ${from} = ${data.converted_amount} ${to}`;
        document.querySelector(".aa").style.background = "#279300ff";
      }
    }
});
